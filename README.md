
# Celery Workshop


### RabbitMQ

To easily spin-up a RabbitMQ instance on your local machine, run:

```bash
docker run --rm -it --name broker -p 15672:15672 rabbitmq:3-management
```

This docker image includes the management plugin of rabbitmq. You can open it at `http://localhost:15672` with the credentials `guest:guest`.

To stop the broker, just run:

```bash
docker stop broker
```

[References](https://hub.docker.com/_/rabbitmq)
