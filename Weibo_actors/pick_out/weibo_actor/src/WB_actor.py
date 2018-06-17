#coding:utf-8
import sys
import re
import json
import os
reload(sys)
sys.setdefaultencoding("utf-8")


if not os.path.exists("../actor_info"):
        os.mkdir("../actor_info")
file_list = os.listdir("../data/actor/")
finish_list = os.listdir("../actor_info/")
num = 0
for i in file_list:
    num+=1
    print num,i
    if i+".json" in finish_list:
        print i,"ok"
        continue
    with open("../data/actor/"+i, 'r') as f:
        ZF_num = 0
        PL_num = 0
        good_num = 0
        text = f.read()
        fp = text.replace('\n', '').replace('\t', '')
        a = re.findall('<strong class=\".*?\">(.*?)</strong>', fp)
        follow_num = a[0]
        followers_num = a[1]
        weibo_num = a[2]
        print "follow_num:", follow_num
        print "followers_num:", followers_num
        print "weibo_num:", weibo_num
        b = re.findall('<div class="WB_handle">(.*?)</div>', fp)
        #print len(b)
        if(len(b)<=0):
            print "There is no message..."
            ZF_num = 0
            PL_num = 0
            good_num = 0
        else:
            for r in range(len(b)):
                ZF = re.findall('<span><em class="W_ficon ficon_forward S_ficon">.*?</em><em>(.*?)</em></span>', b[r])[0]
                PL = re.findall('<span><em class="W_ficon ficon_repeat S_ficon">.*?</em><em>(.*?)</em></span>', b[r])[0]
                good = re.findall('<span node-type="like_status" class="">.*?<em>(.*?)</em></span>', b[r])[0]
                if ZF == '转发':
                    ZF = 0
                if PL == '评论':
                    PL = 0
                if good == '赞':
                    good = 0
                ZF_num = ZF_num + int(ZF)
                PL_num = PL_num + int(PL)
                good_num = good_num + int(good)

        actor_info = {
            "weibo_num": weibo_num,
            "fans_num": followers_num,
            "focus_num": follow_num,
            "zf_num": ZF_num,
            "pl_num": PL_num,
            "good_num": good_num
        }
        with open("../actor_info/"+i+".json", "w")as f:
            json.dump(actor_info, f, ensure_ascii=False)