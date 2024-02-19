"""
Producer for RabbitMQ to send the Action/Goal/Prompts to our 
AI Agent for processing. 
"""
import os
import pika

amqp_url = os.getenv('CLOUDAMQP_URL','invalid_amqp_config')


def publish(actions):
    """
    Send a message to our messaging queue
    """
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    send_to_hub_channel(connection, actions)
    connection.close()

def send_to_hub_channel(connection, actions):
    """ Send to the hub channel in the queue"""
    channel = connection.channel()
    channel.basic_publish(exchange='',routing_key='hub',
                          body=f"ACTION: {actions.action} PROMPT: {actions.prompt}")
    print(f""""Sent message on channel hub with content: ACTION:
           {actions.action} PROMPT: {actions.prompt}""")
