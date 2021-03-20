# lowe (backend)
FROM python:3.9-slim-buster
LABEL author="Vilhelm Prytz" maintainer="vilhelm@prytznet.se"

COPY . /var/www/app
RUN apt-get update && apt-get install iproute2 libpq-dev gcc -y
WORKDIR /var/www/app

RUN mkdir .venv
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --deploy

ENV PATH="/var/www/app/.venv/bin:$PATH"

EXPOSE 5000
CMD [ "/var/www/app/entrypoint.sh" ]
