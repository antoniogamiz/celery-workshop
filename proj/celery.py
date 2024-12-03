from celery import Celery

app = Celery('proj',
             broker='amqp://',
             backend='redis://',
             include=['proj.tasks'])

app.conf.update(result_expires=3600)

if __name__ == '__main__':
    app.start()
