import sys
import os
from confluent_kafka import(
    Consumer, Message, KafkaError, KafkaException
)
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
consumer = Consumer(**CONF)
# Subscribe to topics
consumer.subscribe([CLOUDKARAFKA_PRODUCER_TOPIC])

# Func for reading messages as they appear in the topic
while True:
    msg = consumer.poll(timeout=1.0)
    if msg is None:
        continue
    if msg.error():
        # Error or event
        if msg.error().code() == KafkaError._PARTITION_EOF:
            # End of partition event
            sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                (msg.topic(), msg.partition(), msg.offset()))
        elif msg.error():
            # Error
            raise KafkaException(msg.error())
    else:
        # Proper message
        sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' %
                            (msg.topic(), msg.partition(), msg.offset(),
                            str(msg.key())))
        print(msg.value())