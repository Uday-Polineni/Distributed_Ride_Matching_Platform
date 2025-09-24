from kafka import KafkaProducer, KafkaConsumer
import json

def get_producer():
    return KafkaProducer(
        bootstrap_servers="a.b.c.d:9092",   # you IP here
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

def get_consumer(topic, group_id):
    return KafkaConsumer(
        topic,
        bootstrap_servers="a.b.c.d:9092",   # you IP here
        group_id=group_id,
        value_deserializer=lambda v: json.loads(v.decode("utf-8"))
    )
