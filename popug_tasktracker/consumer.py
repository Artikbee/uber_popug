import pika, json, django, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from tasks.models import CustomUser

params = pika.URLParameters('amqp://guest:guest@localhost:5672/')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='task.user_created')


def callback(ch, method, properties, body):
    print('Received in task')
    data = json.loads(body)
    CustomUser.objects.create(
        public_id=data['public_id'],
        name=data['name'],
        role=data['role'],
        email=data['email']
    )
    print(body)


channel.basic_consume(queue='task.user_created', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
