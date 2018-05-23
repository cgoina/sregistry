#!/bin/bash

python manage.py collectstatic --noinput
service cron start

if grep -Fxq "PLUGINS_ENABLED+=[\"globus\"]" /code/shub/settings/config.py
then
    # When configured, we can start the endpoint
    echo "Starting Globus Connect Personal"
    export USER="tunel-user"
    /opt/globus/globusconnectpersonal -start &
fi

uwsgi uwsgi.ini
