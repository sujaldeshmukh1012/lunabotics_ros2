#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import serial
from geometry_msgs.msg import Twist


class SerialBridge(Node):
    def __init__(self):
        super().__init__('serial_bridge')
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        self.ser.flush()
        self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)


    def cmd_vel_callback(self, msg):
        linear = msg.linear.x
        angular = msg.angular.z



        if linear > 0:
            command = "1\n"
        elif linear < 0:
            command = "2\n"
        elif angular > 0:
            command = "3\n"
        elif angular < 0:
            command = "4\n"
        else:
            command = "5\n"



        self.ser.write(command.encode('utf-8'))
        self.get_logger().info(f"Sent to Arduino: {command.strip()}")

def main(args=None):
    rclpy.init(args=args)
    node = SerialBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
