from celery import Celery
from kombu import Exchange, Queue


app = Celery(
    'tasks',
    broker='pyamqp://guest@localhost',
    backend='redis://localhost/0',
    include=['tasks.image_aux', 'tasks.video_aux']
)

default_queue_name = 'default'
default_exchange_name = 'default'
default_routing_key = 'default'
default_exchange = Exchange(default_exchange_name, type='direct')

sunshine_queue_name = 'sunshine'
sunshine_routing_key = 'sunshine'

moon_queue_name = 'moon'
moon_routing_key = 'moon'

default_queue = Queue(
    default_queue_name,
    default_exchange,
    routing_key=default_routing_key
)

sunshine_queue = Queue(
    sunshine_queue_name,
    default_exchange,
    routing_key=sunshine_routing_key
)

moon_queue = Queue(
    moon_queue_name,
    default_exchange,
    routing_key=moon_routing_key
)

app.conf.task_queues = (default_queue, sunshine_queue, moon_queue)

app.conf.task_default_queue = default_queue_name
app.conf.task_default_exchange = default_exchange_name
app.conf.task_default_routing_key = default_routing_key

app.conf.task_routes = {
    'tasks.image_aux.*': {'queue': 'sunshine'},
    'tasks.video_aux.*': {'queue': 'moon'},
}

