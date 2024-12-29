#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Satoru Homma
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def main():
    rclpy.init()
    node = Node("listener")

    def cb(msg):
        node.get_logger().info(f"listen: {msg.data}")

    node.create_subscription(String, "zodiac_topic", cb, 10)

    rclpy.spin(node)

if __name__ == "__main__":
    main()

