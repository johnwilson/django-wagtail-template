from fabric.contrib.files import sed
from fabric.api import (
    env,
    local,
    sudo,
)
from decouple import config as conf


# Global env variables
env.user = conf("DOKKU_USER")
env.hosts = [conf("DOKKU_SERVER")]

app_name = conf("DOKKU_APP")


def setup_static():
    sudo("mkdir -p /home/dokku/{app}/storage/public".format(
        app=app_name
    ))
    sudo("chown -R dokku:dokku /home/dokku/{app}/storage".format(
        app=app_name
    ))
    sudo("dokku storage:mount {app} /home/dokku/{app}/storage/public:/app/public".format(
        app=app_name
    ))


def setup_media():
    sudo("mkdir -p /home/dokku/{app}/storage/media".format(
        app=app_name
    ))
    sudo("chown -R dokku:dokku /home/dokku/{app}/storage".format(
        app=app_name
    ))
    sudo("dokku storage:mount {app} /home/dokku/{app}/storage/media:/app/media".format(
        app=app_name
    ))


def setup_db():
    # Setup Database
    sudo("dokku postgres:create {app}".format(
        app=app_name
    ))
    sudo("dokku postgres:link {app} {app}".format(
        app=app_name
    ))


def setup():
    # create new app
    sudo("dokku apps:create {0}".format(app_name))
    
    # allowed hosts
    sudo("dokku config:set {app} ALLOWED_HOSTS={app}.{server}".format(
        app=app_name,
        server=conf("DOKKU_SERVER")
    ))

    # production env
    sudo("dokku config:set {app} DJANGO_SETTINGS_MODULE=config.prod".format(
        app=app_name
    ))

    # Set SECRET
    pw = local("pwgen -s 64 -n 1", capture=True)
    sudo("dokku config:set {app} SECRET_KEY='{pw}'".format(
        app=app_name,
        pw=pw
    ))
    
    setup_db()
    setup_media()
    setup_static()


def destroy():
    sudo("rm -rf /home/dokku/{0}/storage".format(app_name))
    sudo("dokku --force apps:destroy {0}".format(app_name))
    sudo("dokku --force postgres:destroy {0}".format(app_name))
    
