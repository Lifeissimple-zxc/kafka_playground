from dotenv import load_dotenv
from os import environ
# My thoughts
# KARAFKA_USER = "zkzuzyqf"
# KARAFKA_PASSWORD = "5Nnb4LMYwBp60g0IQeJmniYSLNJNBUcN"
# KARAFKA_AUTH_METHOD = "SASL/SCRAM-SHA-512" # TBD if needed
# KARAFKA_PORT = 9094
# KARAFKA_HOSTNAME = "dory.srvs.cloudkafka.com"
# KARAFKA_REGION = "amazon-web-services::us-east-1"
# KARAFKA_TOPIC = "zkzuzyqf-default"

##  https://mahaboob.medium.com/working-with-cloud-kafka-in-python-94d0825b4f71
# Setting up required variables
load_dotenv()
CLOUDKARAFKA_BROKERS = environ.get("CLOUDKARAFKA_BROKERS")
CLOUDKARAFKA_USERNAME = environ.get("CLOUDKARAFKA_USERNAME")
CLOUDKARAFKA_PASSWORD = environ.get("CLOUDKARAFKA_PASSWORD")
CLOUDKARAFKA_PRODUCER_TOPIC = environ.get("CLOUDKARAFKA_PRODUCER_TOPIC")
