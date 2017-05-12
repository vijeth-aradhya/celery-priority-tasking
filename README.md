# celery-priority-tasking
This is a prototype to schedule jobs in the backend based on some priority using Rabbitmq and Celery.

## Video Transcoding Simulation
In this sample project, the powers of Celery and RabbitMQ in prioritized tasking can be seen. The simulation for transcoding a video to 
- 360p resolution takes 5 seconds
- 480p resolution takes 10 seconds
- 720p resolution takes 15 seconds
- 1080p resolution takes 20 seconds

Of course this isn't even close to the real scencario, but it's good enough to observe the prioritized tasking.

## Execution
- First, go into the directory `cd celery-priority-tasking/celery_sample_project` and run `pip install -r requirements.txt`.
- Run `python main.py` for starting up Flask.
- Then, in another terminal, run `celery worker -c [number of workers] -A tasks --loglevel=info &`.
- Open up a browser and start simulating!

## Preview
With 3 celery workers, there is a small preview video [here](https://youtu.be/tM82eQMa2KE)

## Install dependencies for RabbitMQ
To install dependencies on Debian machines, use the script provided or otherwise modify it accordingly for other operating systems.

## Tutorials
- [Celery](https://www.fullstackpython.com/task-queues.html) [full stack python]
- [Task Queues](https://www.fullstackpython.com/task-queues.html) [full stack python]
- [How to integrate RabbitMQ with Celery?](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#broker-rabbitmq)
