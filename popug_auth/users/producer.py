import pika, json

params = pika.URLParameters('amqp://guest:guest@localhost:5672/')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    data = {
        'name': body.get('name'),
        'role': body.get('role')
    }
    channel.basic_publish(
        exchange='',
        routing_key='task',
        body=json.dumps(data),
        properties=properties
    )
    channel.basic_publish(
        exchange='',
        routing_key='billing',
        body=json.dumps(data),
        properties=properties
    )

