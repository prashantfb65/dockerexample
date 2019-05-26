# Innovation Environment

This repository sets in the environment for different utilites.

1. RabbitMQ
2. Redis
3. PostgresSQL
4. Django Application
5. Flask Webservice
6. Jupyter Notebook

## Setup of environment variable

For Mac machine machine you could use the script already present

DB_PATH
NOTEBOOK_PATH

```bash
. ./set-env-var.sh
```

## Start the Environment

For this you will need `docker` and `docker-compose` installed on your machine.

`docker-compose up`

## Check if the services started Successfully
```bash
docker container ls
```

The output should have six containers running:
```bash
CONTAINER ID        IMAGE                          COMMAND                  CREATED              STATUS              PORTS                    NAMES
689d935482fa        jupyter/datascience-notebook   "tini -g -- start-no…"   51 seconds ago       Up 50 seconds       0.0.0.0:8888->8888/tcp   dockerexample_notebook_1
381b6b31c450        dockerexample_web_portal       "python user_interfa…"   About a minute ago   Up About a minute   0.0.0.0:8000->8000/tcp   dockerexample_web_portal_1
2e8ee55293bf        dockerexample_web_service      "/bin/sh -c 'python …"   About a minute ago   Up About a minute   0.0.0.0:5000->5000/tcp   dockerexample_web_service_1
5c39eb9e599d        redis                          "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:6379->6379/tcp   dockerexample_redis_1
b80bc97416ad        postgres                       "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:5432->5432/tcp   dockerexample_db_1
793e0dfe5091        rabbitmq:3.7-rc-management     "docker-entrypoint.s…"   About a minute ago   Up About a minute   15671/tcp, 0.0.0.0:24369 dockerexample_rabbitmq_1
```

## Services
This will start the six services

RabbitMQ: `http://localhost:45672/`

Redis

PostgresSQL

Flask Webservice `http://localhost:5000/`

Django Application `http://localhost:8000/`


Jupyter Notebook
```bash
notebook_1     | [I 19:23:00.212 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
notebook_1     | [I 19:23:00.212 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
notebook_1     | [I 19:23:00.217 NotebookApp] Serving notebooks from local directory: /home/jovyan
notebook_1     | [I 19:23:00.218 NotebookApp] The Jupyter Notebook is running at:
notebook_1     | [I 19:23:00.218 NotebookApp] http://(52447a97d19b or 127.0.0.1):8888/?token=3b2c14fa638fe69dde3da18d1d0b0534f62d6d4c09d3eaec
notebook_1     | [I 19:23:00.218 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

Copy the token to open the Jupyter Notebook
e.g.
http://localhost:8888/?token=`copied token`

http://localhost:8888/?token=3b2c14fa638fe69dde3da18d1d0b0534f62d6d4c09d3eaec

Note: Your notebooks will be stored in the environment variable (NOTEBOOK_PATH)


## Shut down the environment 
`docker-compose down`

All the services/utilities will shut down