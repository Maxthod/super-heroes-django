FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install --yes \
    nginx \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    && apt-get clean \
    pip install --upgrade pip
COPY ../requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
RUN mv .docker/nginx.conf /etc/nginx/conf.d/nginx.conf

EXPOSE 8888

ENTRYPOINT ["/usr/bin/env", "sh", ".docker/entrypoint.sh"]
CMD ["gunicorn", "superheroes.wsgi:application"]