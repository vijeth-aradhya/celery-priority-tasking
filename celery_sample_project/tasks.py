from celery import Celery
import time

celery_app = Celery('tasks', backend='amqp', broker='amqp://')

# celery worker -c 3 -A tasks --loglevel=info &

###

# Idea of the sample project is to simulate transcoding of a video into
# different dimensions using celery priority task queues, and actually
# test if it is priority based.

# example: transcode_360p.apply_async(priority=1)

###


@celery_app.task
def transcode_360p():
    # Simulate transcoding a video into 360p resolution
    print 'BEGIN:   Video transcoding to 360p resolution!'
    time.sleep(5)
    print 'END:   Video transcoded to 360p resolution!'


@celery_app.task
def transcode_480p():
    # Simulate transcoding a video into 480p resolution
    print 'BEGIN:   Video transcoding to 480p resolution!'
    time.sleep(10)
    print 'END:   Video transcoded to 480p resolution!'


@celery_app.task
def transcode_720p():
    # Simulate transcoding a video into 720p resolution
    print 'BEGIN:   Video transcoding to 720p resolution!'
    time.sleep(15)
    print 'END:   Video transcoded to 720p resolution!'


@celery_app.task
def transcode_1080p():
    # Simulate transcoding a video into 1080p resolution
    print 'BEGIN:   Video transcoding to 1080p resolution!'
    time.sleep(20)
    print 'END:   Video transcoded to 1080p resolution!'
