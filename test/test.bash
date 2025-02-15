#!/bin/bash
# SPDX-FileCopyrightText: 2024 Satoru Homma
# SPDX-License-Identifier: BSD-3-Clause
dir=~                      
[ "$1" != "" ] && dir="$1" 

cd $dir/ros2_ws 
colcon build      
source $dir/.bashrc        

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '日付: 2025-01-20, 曜日: Monday, 星座: Aquarius(みずがめ座)'

