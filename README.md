# Discord Rich Presence Desktop

Aplicación de escritorio para Windows que muestra una actividad personalizada en Discord. Permite crear perfiles, rotar textos y actividades, y mantener la conexión desde la bandeja del sistema.

> **Importante:** la aplicación se conecta mediante el token de una cuenta de usuario. La automatización de cuentas de usuario puede infringir los Términos de servicio de Discord y provocar la suspensión de la cuenta. Úsala bajo tu responsabilidad y nunca compartas el token.

[English version](#english)

## Funciones

- Perfiles para actividades de jugando, transmitiendo, escuchando, viendo o compitiendo.
- Rotación de detalles, textos y perfiles con intervalos configurables.
- Estado personalizado, emoji y estado de conexión de Discord.
- Imágenes desde una URL o archivo local; hasta dos botones con enlaces.
- Temporizador transcurrido o cuenta regresiva.
- Aviso cuando compartir actividad está desactivado.
- Ejecución en la bandeja del sistema e inicio opcional con Windows.

## Requisitos

- Windows 10 u 11 con WebView2.
- Python 3.11 o superior.

## Instalación y uso

~~~bash
git clone https://github.com/UiUyHerrera/discord-rich-presence-desktop.git
cd discord-rich-presence-desktop
pip install -r requirements.txt
python app.py
~~~

Al iniciar, configura el token de Discord. La aplicación lo guarda en %APPDATA%\EstadoDiscord\token.txt; también acepta la variable de entorno DISCORD_TOKEN. Para iniciar minimizada en la bandeja, ejecuta python app.py --oculto.

## Pruebas y ejecutable

~~~bash
pip install -r requirements-dev.txt
python -m pytest
pyinstaller --noconsole --onefile --name EstadoDiscord --icon ui/icono.ico --add-data "ui;ui" app.py
~~~

El ejecutable se genera en dist/EstadoDiscord.exe.

## Arquitectura

La interfaz usa HTML, CSS y JavaScript en una ventana de [pywebview](https://pywebview.flowrl.com/). Python expone la API de la interfaz y administra la conexión al gateway de Discord, la actividad, la rotación, la configuración, las imágenes y la integración con Windows. Las pruebas cubren actividad, configuración y rotación.

## English

A Windows desktop application for displaying a custom Discord activity. It supports activity profiles, rotating text and profiles, and background operation from the system tray.

> **Important:** the app connects using a user account token. Automating user accounts may violate Discord's Terms of Service and can result in account suspension. Use it at your own risk and never share your token.

### Features

- Profiles for playing, streaming, listening, watching, and competing activities.
- Configurable rotation of activity details, text, and profiles.
- Custom status, emoji, and Discord online status.
- Images from a URL or local file, plus up to two linked buttons.
- Elapsed-time or countdown timers.
- Notice when activity sharing is disabled.
- System-tray operation and optional startup with Windows.

### Requirements

- Windows 10 or 11 with WebView2.
- Python 3.11 or newer.

### Install and run

~~~bash
git clone https://github.com/UiUyHerrera/discord-rich-presence-desktop.git
cd discord-rich-presence-desktop
pip install -r requirements.txt
python app.py
~~~

Configure the Discord token when the app starts. It is stored in %APPDATA%\EstadoDiscord\token.txt; the DISCORD_TOKEN environment variable is also supported. Run python app.py --oculto to start minimized to the system tray.

### Tests and executable

~~~bash
pip install -r requirements-dev.txt
python -m pytest
pyinstaller --noconsole --onefile --name EstadoDiscord --icon ui/icono.ico --add-data "ui;ui" app.py
~~~

The executable is created at dist/EstadoDiscord.exe.

### Architecture

The interface uses HTML, CSS, and JavaScript in a [pywebview](https://pywebview.flowrl.com/) window. Python exposes the interface API and manages the Discord gateway connection, activity payload, rotation, configuration, images, and Windows integration. Tests cover activity, configuration, and rotation.
