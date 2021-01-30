cmake_minimum_required(VERSION 3.11)

project (mqtt-client)

include_directories(mqtt)

add_executable(mqtt-client main.cpp)
target_link_libraries(mqtt-client paho-mqttpp3 paho-mqtt3as)
