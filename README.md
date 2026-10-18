# Discord Status

A Windows desktop app that puts a custom activity on your Discord profile ("Playing…", "Listening to…", "Watching…") with your own text and images, and rotates it on its own.

![The activity as it shows in Discord](docs/actividad.png)

> **Heads up:** the app connects with your user account token. Automating user accounts is against Discord's terms and can get the account suspended. Use it at your own risk.

## What it does

- Activity profiles with a type (playing, streaming, listening, watching or competing), text, large and small images, and buttons with links.
- Rotation: changes the text every few seconds and the profile every few minutes, with minimums so Discord isn't flooded.
- Images from a URL or from a file on your computer. If Discord won't take the URL directly, the app uploads it again.
- Lives in the system tray, can start with Windows and won't open twice.

![Main window](docs/captura.png)

The interface is in Spanish.

## How it's built

Python with a web interface inside a native window (pywebview) and a tray icon (pystray). The connection to Discord is a small gateway client of its own over websockets, which sends the presence and reconnects by itself when the connection drops.

```
app.py        window, tray and the API the interface calls
nucleo/       gateway, profiles, rotation, images and Windows options
ui/           the interface's HTML, CSS and JavaScript
tests/        tests for the rotation and for building activities
```

## Installing

The easiest way is the [installer](https://github.com/UiUyHerrera/discord-rich-presence-installer): it takes care of Python, the dependencies and the shortcuts.

By hand:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

It asks for the token when it opens. The token is stored in plain text in `%APPDATA%\EstadoDiscord`, next to the profiles; if you'd rather not store it, pass it in the `DISCORD_TOKEN` environment variable.

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest
```
