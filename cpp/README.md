# C++ MQTT Example

In order to use this example you need a C++ 11 or greater compatible compiler. It also requires the cmake build utility.

The Pahos MQTT C and C++ libraries are both required to build the project. Install them from:
- https://github.com/eclipse/paho.mqtt.cpp
- https://github.com/eclipse/paho.mqtt.c

To build the project run the following commands in this directory:

```sh
cmake .
make
```
This should produce an `mqtt-client` binary. This will listen to the "example" topic. The sender scripts in the [Python examples](../python) directory.
