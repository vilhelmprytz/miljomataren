# miljomataren-api

## Deployment Instructions

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

## Project limitations

### Lack of automated vehicle information

Ideally, the user should only have to enter the registration number of their vehicle and fuel consumption, CO2 emissions and yearly milage of the vehicle should automatically be fetched from [Transportstyrelsen](https://transportstyrelsen.se) (or any other public database). The problem with this is that most APIs are not open to the public and using them induces quite a large cost. We cannot simply afford to do this under the limitations of the project which is why the user has to manually input details about their vehicle. If this application would be commercialized, this would definitely be implementable.

### Fuel consumption on the paper is not real world fuel consumption

This project only uses GPS positioning as well as vehicle information to determine the realtime cost, fuel consumption and CO2 emissions. For a short drive, this isn't an accurate representation of real-world usage. Cars are considerably less fuel-efficient when the engine is cold, thus short trips, where the engine doesn't have time to warm up, will be very inefficient. Our model doesn't reflect that.

Secondly, people drive differently. Aggressive driving and bad planning also leads to less fuel efficiency and is not reflected in this project.

## License

Licensed under the terms of the GNU GPL-3.0 License. See the [license](LICENSE) file.

## Project Authors ✨

- [Vilhelm Prytz](https://github.com/vilhelmprytz), vilhelm@prytznet.se
- [Felix Lindblad](https://github.com/felixlindblad)
- [Ludwig Sjöberg](https://github.com/ludwigsjo)

This API is a component of a larger project. The API is mainly written by Vilhelm Prytz.
