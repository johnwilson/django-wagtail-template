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
4. Install other dependencies (`$ pipenv install psycopg2-binary gunicorn dj-database-url python-decouple`)
5. Install dependencies (`$ pipenv install --dev fabric3 flake8`)
6. Create a new project using this template
7. Rename env-sample to .env and edit
8. Remember to include the dokku server and system user in your .env
9. Install [dokku_client.sh](http://dokku.viewdocs.io/dokku/community/clients/#bash-zsh-etc-dokku_clientsh)


## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/johnwilson/django-wagtail-template/archive/master.zip --name=env-sample  <project_name> .

## Deployment to Dokku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ git remote add dokku dokku@<remote_server>:<app_name>
    $ fab -I -f fabfile.py setup
    $ git push dokku master

    $ dokku run python manage.py createsuperuser

## Backuping up using rclone

Use the `backup.sh` template to create a cron backup job. Modify it as necessary.

## Configured urls

Django admin `http://localhost:8000/admin/`

Wagtail admin `http://localhost:8000/cms/`

Wagtail pages `http://localhost:8000/pages/`

## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
- [wagtail](https://wagtail.io/)
- [dokku_client.sh](https://github.com/dokku/dokku/blob/master/contrib/dokku_client.sh)
