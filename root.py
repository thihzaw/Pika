#!/usr/bin/python
import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        '10.10.10.190',
        5672,
        credentials=pika.PlainCredentials('yuntao', 'EashAnicOc3Op')
    )
)


channel = connection.channel()
channel.basic_publish(
    exchange='plugin_data',
    routing_key='',
    body='http://127.0.0.1:8000/test.lua'
)
connection.close()

