# -*- coding:utf-8 -*-

from pykafka import KafkaClient
host = '192.168.20.203:9092,192.168.20.204:9092,192.168.20.205:9092'
client = KafkaClient(hosts=host)
topic=client.topics['test_kafka_topic']
balanced_consumer = topic.get_balanced_consumer(consumer_group='test_kafka_topic',auto_commit_enable=True,
                                                     zookeeper_connect='192.168.20.201:2181,192.168.20.202:2181,192.168.20.203:2181')
for messgage in balanced_consumer:
    print(messgage)
    if messgage is not None:
        print(messgage.offset)
        print(messgage.value)