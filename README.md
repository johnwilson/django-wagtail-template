# Heroku Django & Wagtail Starter Template

An utterly fantastic project starter template for Django 2.0.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Latest Python 3.6 runtime environment.

## How to Use

To use this project, follow these steps:

1. Create your working directory.
2. Create your environment (`$ pipenv shell --three`)
3. Install Wagtail (`$ pipenv install wagtail`)
4. Install Wagtail (`$ pipenv install psycopg2-binary gunicorn dj-database-url python-decouple`)
5. Install dependencies (`$ pipenv install --dev fabric3`)
6. Create a new project using this template
7. Rename env-sample to .env and edit
8. Remember to include the dokku server in your .env


## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=<path_to_this_template> --name=env-sample  <project_name> .

## Deployment to Dokku (or Heroku)

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ git remote add dokku dokku@<remote_server>:<app_name>
    $ fab -I -f fabfile.py setup
    $ git push dokku master

    $ dokku run python manage.py createsuperuser


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
- [wagtail](https://wagtail.io/)
