#coding:utf-8
import sys
import json
import os
import shutil
reload(sys)
sys.setdefaultencoding("utf-8")

#将明星分类到相应的电影id文件夹内
name_id={}

with open("../data/list","r") as read:
    for i in read.readlines():
        text = i.split('	')
        id = text[0]
        name = text[1].replace('\n','')
        name_id[name]=id
    for key in name_id:
        if not os.path.exists("../movie_actor/"+str(name_id[key])):
            os.mkdir("../movie_actor/"+str(name_id[key]))
        if os.path.exists("../movie_actor/"+str(name_id[key])+"/"+key+".json"):
            print key,"ok"
            continue

        if not os.path.exists("../actor_info/"+key+".json"):
            # print key+"不存在"
            with open("../unexists",'a') as w:
                w.write(name_id[key]+'	'+key+"\n")
            continue
        shutil.copy("../actor_info/"+key+".json","../movie_actor/"+str(name_id[key])+"/")
