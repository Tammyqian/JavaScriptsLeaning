from pykafka import KafkaClient

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
