import pika, json

params = pika.URLParameters('amqp://guest:guest@localhost:5672/')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='auth')


def callback(ch, method, properties, body):
    print('Received in auth')
    print(body)


channel.basic_consume(queue='auth', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
