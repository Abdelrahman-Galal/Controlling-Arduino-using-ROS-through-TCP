import socket
import time
import serial
import argparse
import sys


def init_serial(port, baudrate=9600):
    try:
        serial_connection = serial.Serial(port, baudrate)
    except serial.serialutil.SerialException:
        print("Check Arduino is connected")
        serial_connection = None
    return serial_connection


def tcp_client(tcp_host, tcp_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((tcp_host, tcp_port))
            received_data = s.recv(1024)
    except:
        print("Connection issue encountered")
        received_data = None
    return received_data


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='TCP Client for ROS and Serial Server for Arduino')
    parser.add_argument('--tcp_host', type=str, help='Name/IP of TCP ROS server')
    parser.add_argument('--tcp_port', type=int, help='Port of TCP ROS server')
    parser.add_argument('--serial_port', type=str, help='USB Port where Arduino USB in connected example,"COM3"')
    parser.add_argument('--serial_baudrate', type=int, default='9600', help='Serial baudrate ')

    args = parser.parse_args()

    HOST = args.tcp_host
    PORT = args.tcp_port

    ser = init_serial(args.serial_port, args.serial_baudrate)

    if ser is None:
        sys.exit(1)

    while True:
        data = tcp_client(HOST, PORT)

        if data is None:
            time.sleep(1)
            continue

        print(f"Received {str(data, encoding='ascii')}")
        ser.write(data)
        time.sleep(1)
