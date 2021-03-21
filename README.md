# miljomataren

![License](https://img.shields.io/github/license/vilhelmprytz/miljomataren)

| Build     | Type                                                                             | Build Status                                                                                                                                         |
| --------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Travis CI | Code Style                                                                       | [![Travis CI](https://img.shields.io/travis/com/vilhelmprytz/miljomataren)](https://travis-ci.com/github/vilhelmprytz/miljomataren)                  |
| GitLab CI | [Container Registry](https://gitlab.com/vilhelm/miljomataren/container_registry) | [![Gitlab pipeline status](https://gitlab.com/vilhelm/miljomataren/badges/master/pipeline.svg)](https://gitlab.com/vilhelm/miljomataren/-/pipelines) |

Diploma project "miljömätaren". Fullstack web application deployable using Docker.

## Structure

| Codebase               |   Description    |
| :--------------------- | :--------------: |
| [abernathy](abernathy) | Next.js frontend |
| [lowe](lowe)           |  Flask backend   |
| [delos](delos)         |   Arduino code   |

## Deploying application

To deploy the application, [Docker](https://docs.docker.com/engine/install/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/) are both required.

Firstly, you need to configure the application. You can use the `.env.example` as reference, simply copy it to `.env` and modify it to suit your setup.

```bash
cp .env.example .env
vim .env
```

Once it's configured, use docker-compose to start the application.

```bash
docker-compose -f prod.yml up -d
```

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

This codebase is mainly written by Vilhelm Prytz.
