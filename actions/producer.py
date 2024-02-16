import os
import pika

amqp_url = os.getenv('CLOUDAMQP_URL','invalid_config')
params = pika.URLParameters(amqp_url)

def publish(action, prompt):
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.basic_publish(exchange='',routing_key='hub',body=f"ACTION: {action} PROMPT: {prompt}")
    print(f"Sent message on channel hub with content: ACTION: {action} PROMPT: {prompt}")
    connection.close()


