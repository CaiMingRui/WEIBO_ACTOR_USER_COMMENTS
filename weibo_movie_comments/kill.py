# -*- coding:utf-8 -*-
import os

def kill_geckodriver():
    print "杀死后台Geckodriver..."
    ret_text_list = os.popen("ps | grep geckodriver")
    pid_box = []
    for i in ret_text_list:
        pid_box.append(i.split()[0])
        print i
    for pid in pid_box:
        print pid
        # os.system("kill -9 %s" % pid)
    print "猎杀完毕..."

def kill_firefox():
    print "杀死后台Firefox..."
    ret_text_list = os.popen("ps | grep firefox")
    pid_box = []
    for i in ret_text_list:
        pid_box.append(i.split()[0])
        print i
    for pid in pid_box:
        print pid
        # os.system("kill -9 %s" % pid)
    print "猎杀完毕..."

def kill_Web():
    print "杀死后台Web Content..."
    ret_text_list = os.popen("ps | grep Web")
    pid_box = []
    for i in ret_text_list:
        pid_box.append(i.split()[0])
        print i
    for pid in pid_box:
        print pid
        # os.system("kill -9 %s" % pid)
    print "猎杀完毕..."

if __name__ == '__main__':
    kill_geckodriver()
    kill_firefox()
    kill_Web()
