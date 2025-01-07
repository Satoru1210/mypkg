#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Satoru Homma
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime, timedelta

rclpy.init()
node = Node("zodiac_publisher")
pub = node.create_publisher(String, "zodiac", 10)

current_date = datetime.now()

def check_zodiac(date):
    zodiac_dates = [
        ((1, 1), (1, 19), "Capricorn(やぎ座)"),
        ((1, 20), (2, 18), "Aquarius(みずがめ座)"),
        ((2, 19), (3, 20), "Pisces(うお座)"),
        ((3, 21), (4, 19), "Aries(おひつじ座)"),
        ((4, 20), (5, 20), "Taurus(おうし座)"),
        ((5, 21), (6, 20), "Gemini(ふたご座)"),
        ((6, 21), (7, 22), "Cancer(かに座)"),
        ((7, 23), (8, 22), "Leo(しし座)"),
        ((8, 23), (9, 22), "Virgo(おとめ座)"),
        ((9, 23), (10, 22), "Libra(てんびん座)"),
        ((10, 23), (11, 21), "Scorpio(さそり座)"),
        ((11, 22), (12, 21), "Sagittarius(いて座)"),
        ((12, 22), (12, 31), "Capricorn(やぎ座)"),
    ]
    for start, end, sign in zodiac_dates:
        if start <= (date.month, date.day) <= end:
            return sign
    return "Unknown"

def cb():
    global current_date
    date = current_date.strftime('%Y-%m-%d')
    weekday = current_date.strftime('%A')
    zodiac = check_zodiac(current_date)

    msg = String()
    msg.data = f" 日付: {date}, 曜日: {weekday}, 星座: {zodiac}"
    pub.publish(msg)

    current_date += timedelta(days=1)

def main():
    node.create_timer(0.5, cb)  
    rclpy.spin(node)

if __name__ == "__main__":
    main()
