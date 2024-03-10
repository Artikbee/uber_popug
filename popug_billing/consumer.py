import pika, json, django, os
import random
from typing import NoReturn

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from bill.models import CustomUser, Task

params = pika.URLParameters('amqp://guest:guest@localhost:5672/')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='billing')


def callback(ch, method, properties, body) -> NoReturn:
    print('Received in CustomUser')
    data = json.loads(body)

    CustomUser.objects.create(
        name=data['name'],
        email='user@example.com',
        role=data['role'],
    )
    print(body)


def create_cost() -> int:
    cost = random.randint(1, 100)
    return cost


def callback_task(ch, method, properties, body):
    print('Received in Task')
    data = json.loads(body)

    Task.objects.create(
        title=data['title'],
        description=data['description'],
        cost=create_cost()
    )


channel.basic_consume(queue='billing', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='task', on_message_callback=callback_task, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
