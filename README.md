Set your local db credentials in `application.cfg.py`.

Then run the following

```bash
pip install -r requirements.txt
python manage.py db upgrade
python datagen.py
python wsgi.py
```

If you are making any changes to models, then you need to run `python manage.py db migrate` to generate a migration file and then run `python manage.py db upgrade` to apply that migration.


APP ARCHITECTURE
=================

The main file to be run is `wsgi.py`.

The application is created via `app_factory.py`. Follow the thread from there. 

The views can be registered inside the create_app function. 
Views are to be defined inside webapp/views. 

Views will refer models which are defined inside webapp/models.

Login is implemented automatically by Flask-Security. Just go to localhost:5000/login and enter
the credentials specified in datagen.py. It will log you in with admin privileges. 