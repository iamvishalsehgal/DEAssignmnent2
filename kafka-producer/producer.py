from kafka import KafkaProducer
import json

def kafka_python_producer_sync(producer, msg, topic):
    producer.send(topic, bytes(msg, encoding='utf-8'))
    print("Sending " + msg)
    producer.flush(timeout=60)


def success(metadata):
    print(metadata.topic)


def error(exception):
    print(exception)


def kafka_python_producer_async(producer, msg, topic):
    producer.send(topic, bytes(msg, encoding='utf-8')).add_callback(success).add_errback(error)
    producer.flush()


if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers='35.226.94.63:9092')  # use your VM's external IP Here!
    # value_serializer = lambda v: json.dumps(v).encode('utf-8')
    with open('C:/Users/48504/Desktop/JADSMaster/DataEngineering/games_details.json') as f:   # change this path to the path in your laptop
        json_data = json.load(f)

        # Process each JSON object in the file
    for data in json_data:
        print('Is this a JSON object? ', data)
        # Use your Kafka producer function here to send each JSON object
        kafka_python_producer_sync(producer, json.dumps(data), 'games_details')
    f.close()
