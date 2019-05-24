# -*- coding: utf-8 -*-
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

msg_dict = {
    "sleep_time": 10,
    "db_config": {
        "database": "test_1",
        "host": "localhost",
        "user": "root",
        "password": "root"
    },
    "table": "msg",
    "msg": "Hello World"
}
msg = json.dumps(msg_dict)
producer.send('test_rhj', msg, partition=0)
producer.close()
