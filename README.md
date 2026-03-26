# ☕ Coffee Shop – Moderne Django Webseite

Eine vollständige, moderne Coffee-Shop-Webseite mit Django 5.

## Features

- **Modernes Design**: Responsive, dunkler Modus, Parallax-Hero, Mikro-Interaktionen
- **Statische Seiten**:
  - Startseite mit Featured-Produkten, Events und Blog-Artikeln
  - Menü (Kaffee-Produkte) mit WhatsApp-Bestell-Button
  - Über uns (Team & Philosophie)
  - Events (Live-Musik, Verkostungen)
  - Galerie (Lightbox)
  - Blog (Kaffee-Wissen, Rezepte) mit Detailseiten
  - Kontakt (Google Maps, Öffnungszeiten, Social Links)
  - Reservierungsformular (Frontend, DB-Model vorhanden)
- **Modelle**: Product, Event, Article, GalleryImage, Reservation (Admin-Registrierung)
- **Dark Mode** mit localStorage-Persistenz
- **WhatsApp-Integration** für Bestellungen
- **Barrierefreiheit**: Alt-Texte, Lazy Loading, semantisches HTML

## Schnellstart

1. Voraussetzungen:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install django pillow
   ```

2. Migrationen anwenden:
   ```bash
   python manage.py migrate
   ```

3. Entwicklungsserver starten:
   ```bash
   python manage.py runserver
   ```

4. Im Browser öffnen: http://127.0.0.1:8000/

5. Admin-Panel unter http://127.0.0.1:8000/admin/ (Benutzer anlegen: `python manage.py createsuperuser`)

## Projektstruktur

- `coffee_shop/` – Django-Projekt (Settings, URLs, WSGI)
- `shop/` – Haupt-App
  - `models.py` – Datenmodelle
  - `views.py` – Ansichten
  - `urls.py` – Routen
  - `admin.py` – Admin-Interface
  - `templates/shop/` – HTML-Templates
  - `static/shop/` – CSS (`custom.css`), JS (`main.js`), Bilder

## Deployment

- Setze Umgebungsvariablen (SECRET_KEY, DEBUG, ALLOWED_HOSTS).
- Führe `python manage.py collectstatic` aus.
- Für Production: Debug=False, sichere ALLOWED_HOSTS, Datenbank konfigurieren (SQLite oder PostgreSQL).
- Render, PythonAnywhere oder andere Hosts unterstützt.

## Anpassungen

- Inhalte im Admin eingeben: Produkte, Events, Blog-Artikel, Galerie-Bilder.
- Farben/Styles in `shop/static/shop/css/custom.css` anpassen.
- Texte in Templates bearbeiten.
- WhatsApp-Nummer in `base.html` und `menu.html` anpassen (`49123456789`).

## Lizenz

MIT – frei nutzbar und erweiterbar.

Guten Appetit und genieß den Kaffee! ☕
