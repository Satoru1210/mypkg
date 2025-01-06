#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Satoru Homma
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from zodiac_msgs.msg import ZodiacInfo

def main():
    rclpy.init()
    node = Node("listener")

    def cb(msg):
        node.get_logger().info(f"日付: {msg.date}, 曜日: {msg.weekday}, 星座: {msg.zodiac}")

    node.create_subscription(ZodiacInfo, "zodiac", cb, 10)

    rclpy.spin(node)

if __name__ == "__main__":
    main()

