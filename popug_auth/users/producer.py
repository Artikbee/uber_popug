import pika, json
from typing import NoReturn
#from popug_schema_registry.v1.user_create_dto import UserCreateDTO

params = pika.URLParameters('amqp://guest:guest@localhost:5672/')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method: str, body: dict) -> NoReturn:
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange='',
        routing_key='task.user_created',
        body=json.dumps(body),
        properties=properties
    )
    # channel.basic_publish(
    #     exchange='',
    #     routing_key='billing.user_created',
    #     body=json.dumps(body),
    #     properties=properties
    # )
