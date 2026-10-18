# Estado de Discord

App de escritorio para Windows que pone una actividad personalizada en tu perfil de Discord ("Jugando a…", "Escuchando…", "Viendo…") con textos e imágenes propios, y la va rotando sola.

![La actividad tal como se ve en Discord](docs/actividad.png)

> **Ojo:** la app se conecta con el token de tu cuenta de usuario. Automatizar cuentas de usuario va contra los términos de Discord y puede terminar en una suspensión. Usala bajo tu responsabilidad.

## Qué hace

- Perfiles de actividad con tipo (jugando, transmitiendo, escuchando, viendo o compitiendo), textos, imágenes grande y chica, y botones con links.
- Rotación: cambia de texto cada tantos segundos y de perfil cada tantos minutos, con mínimos para no saturar a Discord.
- Imágenes desde una URL o desde un archivo de la compu. Si Discord no acepta la URL directa, la app la vuelve a subir.
- Queda en la bandeja del sistema, puede arrancar con Windows y no deja abrir dos copias a la vez.

![Ventana principal](docs/captura.png)

## Cómo está hecha

Python con una interfaz web dentro de una ventana nativa (pywebview) y un ícono en la bandeja (pystray). La conexión con Discord es un cliente propio del gateway sobre websockets, que manda la presencia y se reconecta solo si se corta.

```
app.py        ventana, bandeja y la API que usa la interfaz
nucleo/       gateway, perfiles, rotación, imágenes y opciones de Windows
ui/           HTML, CSS y JavaScript de la interfaz
tests/        tests de la rotación y del armado de actividades
```

## Instalarla

Lo más fácil es el [instalador](https://github.com/UiUyHerrera/discord-rich-presence-installer): se encarga de Python, de las dependencias y de los accesos directos.

A mano:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Al abrirla pide el token. Queda guardado en texto plano en `%APPDATA%\EstadoDiscord`, junto con los perfiles; si preferís no guardarlo, podés pasarlo en la variable de entorno `DISCORD_TOKEN`.

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest
```
