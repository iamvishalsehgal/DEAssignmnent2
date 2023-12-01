from kafka import KafkaConsumer, TopicPartition


def read_from_topic(kafka_consumer, topic):
    print('Inside read from topic')
    print(kafka_consumer)
    print(topic)
    kafka_consumer.subscribe(topics=[topic])
    for msg in kafka_consumer:
        print("Message here ", msg)
        print(msg.value.decode("utf-8"))
        # print(msg.key.decode("utf-8"), " ", msg.value.decode("utf-8"))


def read_from_topic_with_partition(kafka_consumer, topic):
    kafka_consumer.assign([TopicPartition(topic, 1)])
    for msg in kafka_consumer:
        print(msg)


def read_from_topic_with_partition_offset(kafka_consumer, topic):
    print('Inside read_from_topic_with_partition_offset')
    partition = TopicPartition(topic, 0)
    kafka_consumer.assign([partition])
    last_offset = kafka_consumer.end_offsets([partition])[partition]
    for msg in kafka_consumer:
        if msg.offset == last_offset - 1:
            break


if __name__ == '__main__':
    consumer = KafkaConsumer(bootstrap_servers='35.226.94.63:9092',  # use your VM's external IP Here!
                             auto_offset_reset='latest',
                             consumer_timeout_ms=1000)
    print(consumer.topics())
    read_from_topic(consumer, 'games_details')
