# miljomataren/lowe

Backend API written in Flask.

## Running the app locally

You need the following to run the app locally.

- Python 3.9
- [Pipenv](https://github.com/pypa/pipenv)
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [docker-compose](https://docs.docker.com/compose/install/)

Once you got it installed, you can setup a development environment locally.

```bash
pipenv install --dev
```

Configure any environment variables required for local development in `.env` file (use `config.py` as reference).

```bash
vim .env
```

You can then enter the virtual environment of the project.

```bash
pipenv shell
```

Use `docker-compose` to get a development PostgreSQL database running on your system.

```bash
docker-compose up -d
```

Finally, you can now run the app.

```bash
flask run
```

On some systems, you might need to install the `libpq-dev`/`libpq-devel` package before installing wth Pipenv. This is because pg-config is required in order to build the `psycopg2` Python package.
