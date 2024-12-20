from datetime import datetime, timezone

from make87_messages.text.text_plain_pb2 import PlainText
from make87 import initialize, get_subscriber, resolve_topic_name


def main():
    initialize()
    topic_name = resolve_topic_name(name="INCOMING_MESSAGE")
    topic = get_subscriber(name=topic_name, message_type=PlainText)

    def callback(message: PlainText):
        received_dt = datetime.now(tz=timezone.utc)
        publish_dt = message.timestamp.ToDatetime().replace(tzinfo=timezone.utc)
        print(
            f"Received message '{message.body}'. Sent at {publish_dt}. Received at {received_dt}. Took {(received_dt - publish_dt).total_seconds()} seconds."
        )

    topic.subscribe(callback)


if __name__ == "__main__":
    main()
