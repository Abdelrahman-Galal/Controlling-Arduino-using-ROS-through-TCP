#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int8
import socket


def callback(msg):
    try:
        conn, addr = s.accept()
        conn.sendall(bytes(str(msg.data), encoding='ascii'))
        conn.close()
    except socket.timeout:
        print("Connection TimeOut")
    print(f'{msg.data}')


if __name__ == "__main__":
    rospy.init_node('serial_stream_server')
    HOST = rospy.get_param("/tcp_host", '0.0.0.0')
    PORT = rospy.get_param("/tcp_port")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(5)
    s.bind((HOST, PORT))
    s.listen()
    subscriber = rospy.Subscriber('serial_stream', Int8, callback)
    rospy.spin()

