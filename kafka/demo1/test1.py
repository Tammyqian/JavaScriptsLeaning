# -*- coding:utf-8 -*-

from pykafka import KafkaClient
host = '192.168.20.203:9092,192.168.20.204:9092,192.168.20.205:9092'
client = KafkaClient(hosts=host)
print(client.topics)
topic = client.topics["test_kafka_topic"]

for i in range(10):
    print(i)
    message = "test message test message" + str(i)
    message = bytes(message,encoding='utf-8')
    producer = topic.get_producer()
    producer.produce(message)

