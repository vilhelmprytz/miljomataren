FROM python:3.9-slim-buster

WORKDIR /var/www/app

# pipenv virtual environment
RUN mkdir .venv

# install dependenceis
RUN pip install --upgrade pip
RUN pip install pipenv
RUN apt-get update && apt-get install libpq-dev gcc -y

COPY . /var/www/app

RUN pipenv install --deploy

ENV PATH="/var/www/app/.venv/bin:$PATH"
EXPOSE 5000

CMD [ "/var/www/app/entrypoint.sh" ]
