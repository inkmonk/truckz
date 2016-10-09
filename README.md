Set your local db credentials in application.cfg.py
Then run the following

```bash
pip install -r requirements.txt
python manage.py db upgrade
python datagen.py
python wsgi.py
```