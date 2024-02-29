"""
Producer for RabbitMQ to send the Action/Goal/Prompts to our 
AI Agent for processing. 
"""
import os
import pika

amqp_url = os.getenv('CLOUDAMQP_URL','invalid_amqp_config')

def publish(actions):
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    send_to_hub_channel(connection, actions)
    connection.close()

def get_amount_unanswered_messages():
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    message_count = get_unanswered_messages_in_hub_channel(connection)
    connection.close()
    return message_count

def send_to_hub_channel(connection, actions):
    channel = connection.channel()
    channel.basic_publish(exchange='',routing_key='hub',
                body=f"ACTION: {actions.name} PROMPT: {actions.prompt} SUCCESS CRITERIA: {actions.success_criteria}")

def get_unanswered_messages_in_hub_channel(connection):
    channel = connection.channel()
    queue = channel.queue_declare(queue='hub', passive=True)
    return queue.method.message_count
