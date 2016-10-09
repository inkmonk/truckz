Set your local db credentials in `application.cfg.py`.

Then run the following

```bash
pip install -r requirements.txt
python manage.py db upgrade
python datagen.py
python wsgi.py
```

If you are making any changes to models, then you need to run `python manage.py db migrate` to generate a migration file and then run `python manage.py db upgrade` to apply that migration.