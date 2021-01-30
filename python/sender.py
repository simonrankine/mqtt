import time
import logging

from paho.mqtt.client import Client, MQTTMessage
from paho.mqtt import MQTTException
from typing import Dict, Any

from log import setup_logging


logger = logging.getLogger(__name__)


def on_connect(client: Client, userdata: Any, flags: Dict[str, Any], rc: int) -> None:
    logger.info("Connection established")
    client.subscribe("$SYS/#")


def on_message(client: Client, userdata: Any, msg: MQTTMessage) -> None:
    print(f"{msg.topic}: {str(msg.payload)}")


def connect(client: Client, retry_time: int = 5) -> None:
    """
    Safely start the connection to the MQTT broker

    Args:
        client: paho MQTT Client instance
        retry_time: Time to wait before re-trying in seconds. Retry disabled if 0.
    Raises:
        MQTTException: Connection failed with rety_time 0
    """
    assert retry_time > 0, "Retry time must be positive"

    connected = False
    while not connected:
        try:
            client.connect("localhost")
            logger.info("Client connected")
        except MQTTException as e:
            if retry_time == 0:
                # Re-throw if no retry
                raise e
            else:
                logger.warn("Failed to connect: {str}")
                logger.info("Retrying in 5 seconds")
                time.sleep(5)
        else:
            connected = True


def main() -> None:
    client = Client()
    connect(client)
    client.publish("example", "Test Message")


if __name__ == '__main__':
    try:
        setup_logging()
        main()
    except Exception as e:
        logger.critical(f"Un-handled exception: {str(e)}")
