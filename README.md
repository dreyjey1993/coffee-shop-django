# Coffee Shop – Django Webseite

Eine einfache Coffee-Shop-Webseite mit Django 5. Enthält drei Seiten: Home (Start), Menü (Kaffeeauswahl) und Kontakt.

## Schnellstart

1. Voraussetzungen: Python 3.8+, Django installieren:
   ```bash
   pip install django
   ```

2. Datenbank-Migrationen durchführen:
   ```bash
   python manage.py migrate
   ```

3. Entwicklungsserver starten:
   ```bash
   python manage.py runserver
   ```

4. Im Browser öffnen: http://127.0.0.1:8000/

## Projektstruktur

- `coffee_shop/` – Django-Projekt (Einstellungen, URLs)
- `shop/` – App für die Seiten
- `shop/templates/shop/` – Templates (HTML)

## Anpassungen

- Inhalte in `shop/views.py` und Templates bearbeiten.
- Statische Dateien (CSS, Bilder) später unter `shop/static/` einfügen.
- Für Production: `DEBUG = False`, `ALLOWED_HOSTS` setzen,静态 sammeln.

## Lizenz

MIT – frei nutzbar und erweiterbar.

Viel Erfolg und genieße den Kaffee! ☕
