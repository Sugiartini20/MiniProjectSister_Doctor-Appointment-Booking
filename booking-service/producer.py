import pika

def send_notification(message):

    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )

    channel = connection.channel()

    channel.queue_declare(queue='notification')

    channel.basic_publish(
        exchange='',
        routing_key='notification',
        body=message
    )

    print("Notification sent!")

    connection.close()