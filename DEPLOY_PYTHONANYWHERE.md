# Deploy auf PythonAnywhere (SQLite)

## Voraussetzungen
- PythonAnywhere-Konto (kostenlos)
- Git auf PythonAnywhere installiert (ist standardmäßig da)

## Schritte

1. **Code zum PythonAnywhere hochladen**
   - In PythonAnywhere: **Files** → Upload-Zip (oder per Git)
   - Alternativ im Bash:
     ```bash
     git clone https://github.com/dreyjey1993/coffee-shop-django.git
     cd coffee-shop-django
     ```

2. **Virtualenv erstellen und Pakete installieren**
   ```bash
   cd ~/coffee-shop-django
   python3.10 -m venv venv   # oder einfach `python -m venv venv`
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   *Hinweis: PythonAnywhere nutzt Python 3.10 standardmäßig.*

3. **Migrieren und statische Dateien sammeln**
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```
   - Beim collectstatic: `yes` eingeben oder `--noinput` nutzen.

4. **Web-App in PythonAnywhere einrichten**
   - Gehe zu **Web** → **Add a new web app**
   - Wähle: **Manual configuration** → **Python 3.11**
   - Bei **Enter the path to your project's WSGI configuration file**:  
     `/var/www/username_pythonanywhere_com_wsgi.py` (wird automatisch gesetzt)
   - Ersetze den Inhalt der WSGI-Datei mit:

     ```python
     import os
     import sys

     # Pfad zum Projekt (anpassen!)
     path = '/home/username/coffee-shop-django'
     if path not in sys.path:
         sys.path.append(path)

     os.environ['DJANGO_SETTINGS_MODULE'] = 'coffee_shop.settings'

     # Optional: SECRET_KEY setzen (empfohlen)
     # os.environ['SECRET_KEY'] = 'dein-geheimer-key-here'

     # Optional: DEBUG
     # os.environ['DEBUG'] = 'False'

     from django.core.wsgi import get_wsgi_application
     application = get_wsgi_application()
     ```
   - **Ersetze `username` mit deinem PythonAnywhere-Benutzernamen**.
   - Lege in **Web** → **Reload** die Seite neu.

5. **Statische Dateien konfigurieren**
   - In **Web** → **Static files**:
     - **URL**: `/static/`
     - **Path**: `/home/username/coffee-shop-django/staticfiles`
   - Optional für Media:
     - **URL**: `/media/`
     - **Path**: `/home/username/coffee-shop-django/media`
   - Dann **Reload** klicken.

6. **Deine Seite öffnen**
   - URL: `https://username.pythonanywhere.com/`

## Hinweise
- Für Production zufälligen `SECRET_KEY` per Environment Variable setzen.
- SQLite-Datei liegt im Projekt (`db.sqlite3`). Bei Problemen mit Schreibrechten: Besitzer setzen oder DB in `/var/www/...` verschieben.
- Django-Admin unter `/admin/` verfügbar, aber noch ohne Superuser. Create with: `python manage.py createsuperuser`.

---

Noch Fragen? Einfach melden! ☕
