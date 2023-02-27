# Controlling Arduino using ROS via TCP
This package is used if an arduino board is serially connected to a localhost which has no ROS installed.
The Arduino will be then controlled using ROS remote server.

### The package has 3 main parts:

1. ***Arduino/serial_client/serial_client.ino*** to be flashed to the arduino board (Arduino IDE could be used)

2. ***local-host/tcpCliet_serialServer.py*** to run on the localhost where arduino is serially connected
```
tcpCliet_serialServer.py \
--tcp_port <TCP_PORT_ON_ROS_SERVER> \
--tcp_host <ROS_SERVER_IP> \
--serial_port <USB/SERIAL_PORT_WHERE_ARDUINO_IS_CONNECTED>
```
3. ***ROS/arduino_communication_server*** is a ROS package that should be installed on the ROS remote server
```
catkin build arduino_communication_server
```
and launched using a launch file
```
roslaunch arduino_communication_server publisher_tcpServer.launch
```
if everything is successfully installed and running, the arduino LED should start blinking corresponding to ROS stream.
