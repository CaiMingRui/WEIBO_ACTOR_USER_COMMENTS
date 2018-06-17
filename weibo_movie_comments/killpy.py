# -*- coding:utf-8 -*-
import os

def kill_py():
    print "杀死后台py"
    ret_text_list = os.popen("ps -e| grep python")
    pid_box = []
    for i in ret_text_list:
        pid_box.append(i.split()[0])
        print i
    for pid in pid_box:
        print pid
        os.system("kill -9 %s" % pid)
    print "猎杀完毕..."

if __name__ == '__main__':
    kill_py()
