# Python MQTT Examples

To use these examples you need to use Python >= 3.8.

Install dependencies using:

```sh
pip install -r requirements.txt
```

You will need to have an MQTT broker running locally. I used Mosquito: https://mosquitto.org/

This directory contains two scripts:
client.py: Will wait for messages on the "example" topic
server.py: Will send an example message on the "example" topic
