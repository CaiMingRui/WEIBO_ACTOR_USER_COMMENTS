#!/bin/bash

cd /home/caimingrui/SJWJ/weibo/Weibo_actors #设置你的电脑里这个star文件的路径
python killall.py
ps -ef | grep "python" | awk '{print $2}' | xargs kill -9
ps -ef | grep "python2.7" | awk '{print $2}' | xargs kill -9
cd /home/caimingrui/SJWJ/weibo/Weibo_actors #设置你的电脑里这个star文件的路径
sh no.sh
