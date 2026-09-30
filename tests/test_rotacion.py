from nucleo.config import config_vacia, perfil_vacio
from nucleo.rotacion import Motor


def config_con(*perfiles, activo=None):
    c = config_vacia()
    c["perfiles"] = list(perfiles)
    c["perfil_activo"] = activo
    return c


def perfil(pid, detalles=("",), cada=30):
    p = perfil_vacio(pid)
    p["id"] = pid
    p["detalles"] = list(detalles)
    p["rotar_cada"] = cada
    return p


def test_cambio_de_perfil_reinicia():
    c = config_con(perfil("a"), perfil("b"), activo="a")
    m = Motor()
    assert m.paso(c, 100) is True
    assert m.perfil_id == "a" and m.inicio == 100
    assert m.paso(c, 101) is False
    c["perfil_activo"] = "b"
    assert m.paso(c, 150) is True
    assert m.perfil_id == "b" and m.indice == 0 and m.inicio == 150


def test_textos_rotan_segun_intervalo():
    c = config_con(perfil("a", ("uno", "dos"), cada=20), activo="a")
    m = Motor()
    m.paso(c, 0)
    assert m.paso(c, 19) is False
    assert m.paso(c, 20) is True and m.indice == 1
    assert m.paso(c, 39) is False
    assert m.paso(c, 40) is True and m.indice == 2


def test_intervalo_minimo_15_segundos():
    p = perfil("a", ("uno", "dos"), cada=1)
    c = config_con(p, activo="a")
    m = Motor()
    m.paso(c, 0)
    assert m.paso(c, 10) is False
    assert m.paso(c, 15) is True


def test_un_solo_texto_no_rota():
    c = config_con(perfil("a", ("uno", "")), activo="a")
    m = Motor()
    m.paso(c, 0)
    assert m.paso(c, 1000) is False


def test_rotacion_de_perfiles():
    c = config_con(perfil("a"), perfil("b"), perfil("c"), activo="a")
    c["rotar_perfiles"] = {"activo": True, "ids": ["a", "c"], "minutos": 1}
    m = Motor()
    m.paso(c, 0)
    assert m.paso(c, 59) is False
    assert m.paso(c, 60) is True and c["perfil_activo"] == "c"
    assert m.paso(c, 120) is True and c["perfil_activo"] == "a"


def test_rotacion_salta_a_perfil_de_la_lista():
    c = config_con(perfil("a"), perfil("b"), activo="b")
    c["rotar_perfiles"] = {"activo": True, "ids": ["a"], "minutos": 5}
    m = Motor()
    assert m.paso(c, 0) is True and c["perfil_activo"] == "a"


def test_sin_perfil_activo_no_rota():
    c = config_con(perfil("a"), perfil("b"))
    c["rotar_perfiles"] = {"activo": True, "ids": ["a", "b"], "minutos": 1}
    m = Motor()
    assert m.paso(c, 1000) is False and c["perfil_activo"] is None


def test_actividades_incluye_personalizado():
    c = config_con(perfil("a"), activo="a")
    c["perfiles"][0]["nombre"] = "Juego"
    c["personalizado"] = {"texto": "hola", "emoji": ""}
    m = Motor()
    m.paso(c, 0)
    acts = m.actividades(c, lambda u: None)
    assert [a["type"] for a in acts] == [4, 0]
