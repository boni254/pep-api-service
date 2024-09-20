import datetime
import json

import pika
from django.conf import settings


def publish_to_rabbitmq(message: dict):
    connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=settings.RABBITMQ_QUEUE)

    channel.basic_publish(
        exchange="", routing_key=settings.RABBITMQ_QUEUE, body=json.dumps(message, default=serialize_datetime)
    )

    connection.close()


def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")
