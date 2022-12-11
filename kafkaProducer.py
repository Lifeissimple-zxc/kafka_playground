import sys
import os
from confluent_kafka import Producer, Message
from const import (
   CLOUDKARAFKA_BROKERS, CLOUDKARAFKA_PASSWORD, CLOUDKARAFKA_PRODUCER_TOPIC, CLOUDKARAFKA_USERNAME 
)

CONF = {
    'bootstrap.servers': CLOUDKARAFKA_BROKERS,
    'group.id': "%s-consumer" % CLOUDKARAFKA_USERNAME,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'},
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'SCRAM-SHA-256',
    'sasl.username': CLOUDKARAFKA_USERNAME,
    'sasl.password': CLOUDKARAFKA_PASSWORD 
}


# Init producer, we use ** to unpack the dict we have created above
producer = Producer(**CONF)
# function for writing info on message delivery to stderr
def deliveryCallback(err, msg: Message):
    if err:
        sys.stderr.write(f"Message delivery failed: {err}")
        print("Failed :(")
    else:
        sys.stderr.write(f"Message delivered to {msg.topic()}, {msg.partition()}")
        print("Success!")

# Let's produce messages to our topic
sampleMsg = "I am a new message[3]!"
producer.produce(
    CLOUDKARAFKA_PRODUCER_TOPIC, sampleMsg, callback = deliveryCallback
)
sys.stderr.write(f"Waiting for {len(producer)} deliveries...")

producer.flush()