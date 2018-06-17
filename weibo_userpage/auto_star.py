# -*- coding:utf-8 -*-
import os
import time

error_flags = False

if __name__ == '__main__':
    trytime = 0
    while(error_flags == False):
        trytime = trytime+1
        print "第"+str(trytime)+"次尝试"
        os.system('python2.7 ./userpage.py')
        os.system('python2.7 ./kill.py')
    print "第"+str(trytime)+"次尝试","任务结束"

