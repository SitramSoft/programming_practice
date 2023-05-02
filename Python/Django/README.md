# **Repository used for tracking my journey in learning Django framework**

## **Progress**

### 28.04.2023

* In order to have the outline working on a Django project, the root folder needs to be added as a separate folder to the workspace in VS Code. After that, run `cmd+shift+p` and select `Python: select Interpreter`. Choose the option with `('.venv')` from the project directory.
* `python manage.py migrate` - syncs the settings and apps with the django project
* Apps in Django are components
* `python manage.py createsuperuser` - creating a superuser in the `auth` application to be able to log in from `admin` application from Django
* `python manage.py startapp app_name` - create a new app in Django called `app_name`
* `python manage.py makemigrations` - Syncs the database with the model. Command needs to be run in conjunction with `migrate` command
* `python manage.py shell` - Open an interactive shell inside a Django project.
  * `from app.models import Class` - imports a class created by the used in one of the applications
  * `class_name.objects.all()` - Lists all created objects of that class created by user inside the database
  * `class_name.objects.create(field_1='', field_2='')` - creates objects of the type `class_name` inside the database
* Deleting all files and and folders except `__init__.py` from `migrations` folder inside an app and the sqlite db removes all data from from an app. Deleting the database removes also the users
* model reference fields from Django official documentation can be found [here](https://docs.djangoproject.com/en/4.2/ref/models/fields/)
* `views.py` from an app contains the function or classes that affect the view of page. All functions that create a vew have to be added in `urlpatterns` from views.py in the project root directory.

### 27.04.2023

* Started [Python Django Web Framework - Full Course for Beginners](https://www.youtube.com/watch?v=F5mRW0jo-U4) from [freeCodeCamp.org](https://www.freecodecamp.org/)
* Methods for creating Python virtual environments:
  * `virtualenv dir_name` - creates a virtual environment in `dir_name` using whatever python version is installed by default.
  * `virtualenv dir_name -p python3` - creates a virtual environment in `dir_name` using python version specified in path
  * `virtualenv . -p python3` - creates a virtual environment in current dir, using a specific python version specified in path
* Virtual environments are activated with `source bin/activate` and deactivated with `deactivate`
* `pip freeze` - outputs installed packages in a requirements format.
* `django-admin startproject name .` - creating a new django project
* `python manage.py runserver 192.168.0.113:8000` - runs the webserver of a django project. Make sure the IP of the pc that is accessing the django server is added in `src/settings.py` in the `ALLOWED_HOSTS`