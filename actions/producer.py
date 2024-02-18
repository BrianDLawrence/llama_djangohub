"""
Producer for RabbitMQ to send the Action/Goal/Prompts to our 
AI Agent for processing. 
"""
import os
import pika

amqp_url = os.getenv('CLOUDAMQP_URL','invalid_amqp_config')

def publish(action, prompt):
    """
    Send a message to our messaging queue
    """
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    channel = connection.channel()
    channel.basic_publish(exchange='',routing_key='hub',body=f"ACTION: {action} PROMPT: {prompt}")
    print(f"Sent message on channel hub with content: ACTION: {action} PROMPT: {prompt}")
    connection.close()


