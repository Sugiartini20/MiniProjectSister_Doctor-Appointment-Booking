import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='notification')

def callback(ch, method, properties, body):
    print("[NOTIFICATION RECEIVED]")
    print(body.decode())

channel.basic_consume(
    queue='notification',
    on_message_callback=callback,
    auto_ack=True
)

print("Waiting for notification...")
channel.start_consuming()