#!/bin/bash

# Install rabbit-mq

# required ports
sudo apt-get install erlang +ssl
sudo apt-get install rabbitmq-server

# OPTIONAL - install the librabbitmq C library (it's faster thant the default amqp)
sudo pip install librabbitmq

# Install Celery

sudo pip install Celery

