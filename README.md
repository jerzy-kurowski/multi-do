## Multi Do Project

Simple, but scalable and production ready demo project

### Installation Guide

You need following to run this project:

- [Docker with Docker Compose](https://docs.docker.com/compose/install/)

Once you have installed the above and have cloned the repository, you can follow the following steps to get the project up and running:

1. Build and run docker container using docker-compose:

```bash
docker-compose -f local.yml up --build fastapi
```

The server should now be running on `http://localhost:8000` and the API documentation should be available at `http://localhost:8000/docs`.

