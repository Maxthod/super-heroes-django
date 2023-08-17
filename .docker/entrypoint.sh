#!/usr/bin/env sh
export SPRING_APPLICATION_NAME=super-heroes-backend
export SPRING_CONFIG_PASSWORD=OjQES8Vlwgz92t4SfSeXcYuOR
export SPRING_CONFIG_LABEL=onboard/super-heroes-django
export SPRING_CONFIG_URL=https://config-server.config.dev.duvalhub.com
export SPRING_CONFIG_USERNAME=config-server
export SPRING_PROFILES_ACTIVE=dev

python manage.py collectstatic

nginx
exec "$@"