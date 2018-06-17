# -*-coding:utf8-*-
from __future__ import division
from pypinyin import lazy_pinyin
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import re
import login
import urllib
import auto_star
# import auto_star
# import login
import os
import random
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
browser = webdriver.Firefox(executable_path='./geckodriver')
id_name = {}

trytime = 0

# def get_py():
#     global id_name
#     with open("./chinese_actors_all.csv",'r') as py:
#         text = py.readlines()
#         for i in text:
#             ch_py = []
#             mid = i.split("	")[0].replace("	","")
#             name = i.split("	")[1].replace("	","").replace("\n","")
#             list = lazy_pinyin(name.decode("utf-8"))
#             pyname = "".join(list)
#             ch_py.append(name)
#             ch_py.append(pyname)
#             id_name[mid] = ch_py
#

# def product_url():
#     global id_name
#     for i in id_name:
#         if "\xb7" in id_name[i][1]:
#             continue
#         else:
#             get_page(i,id_name[i][0],id_name[i][1])

def read_list():
    global trytime
    with open("./chinese_actors_all.csv", 'r') as py:
        text = py.readlines()
        trytime = trytime + 1
        for i in text:
            print i
            mid = i.split(",")[0].replace("	","")
            name = i.split(",")[1].replace("	","").replace("\n","")
            get_page(mid,name)

def get_page(mid,ch_name):
    global trytime
    with open("./Nfound_actor.txt",'r') as rr:
        Nona = rr.readlines()
        if ch_name+'\n' in Nona:
            print ch_name,"已搜索过，无结果"
            return
    with open("./finish_actor.txt",'r') as ff:
        fina = ff.readlines()
        if ch_name+"\n" in fina:
            print ch_name,"已完成"
            return
    if trytime % 15 == 0:
        print "sleep time..."
        sys.exit()
    # surl = "https://s.weibo.com/user/"+urllib.quote(ch_name)+"&Refer=weibo_user"
    surl = "https://s.weibo.com/weibo/"+urllib.quote(str(ch_name.decode("utf-8")))+"&Refer=STopic_box"
    browser.get(surl)
    try:
        WebDriverWait(browser, 15, 3).until(lambda browser: browser.find_element_by_class_name("star_dir "))
    except:
        pass
    try:
        browser.find_element_by_id("pl_weibo_directtop")
        print ch_name+"找到相关微博"
        url = browser.find_element_by_xpath\
            ("//div[@id='pl_weibo_directtop']/div[@class='WB_cardwrap pl_directarea S_bg2 clearfix']/div/div[@class='list_star clearfix']/div[@class='star_pic']/a").get_attribute('href')
        print "get",ch_name,url
        try:
            into_page(mid,ch_name,url)
        except Exception,e:
            print Exception,":",e,"这里这里这里这里这里这里"
        with open("./finish_actor.txt",'a') as finish:
            finish.write(ch_name+"\n")
        with open("./actor_url.txt",'a') as act:
            act.write(mid+"\001"+ch_name+"\001"+url+"\n")
        print ch_name+"ok"
    except Exception,m:
        print Exception,":",m
        print ch_name+"未找到置顶选项"
        with open("./Nfound_actor.txt",'a') as check:
            check.write(ch_name+'\n')
        return

def into_page(mid,ch_name,urle):
    url = urle.replace("refer_flag=1001030101_","profile_ftype=1&is_all=1#_0")
    browser.get(url)
    try:
        WebDriverWait(browser, 15, 3).until(lambda browser: browser.find_element_by_class_name('WB_innerwrap'))
    except Exception,g:
        print Exception,":",g
    downt = 0
    while (downt <= 6):
        try:
            browser.find_element_by_class_name('next')
            browser.execute_script("window.scrollTo(100000,document.body.scrollHeight);")
            break
        except:
            browser.execute_script("window.scrollTo(100000,document.body.scrollHeight);")
            time.sleep(5)
            pass
        # browser.execute_script("window.scrollTo(100000,document.body.scrollHeight);")
        # try:
        #     WebDriverWait(browser, 5, 1).until(lambda browser: browser.find_element_by_class_name('W_pages'))
        # except Exception, mm:
        #     print Exception, ":", mm
        downt = downt + 1
    time.sleep(3)
    print browser.current_url
    page = browser.page_source
    print "get page_source"
    with open("./actorpage/"+ch_name,'a') as savep:
        savep.write(page)

if __name__ == '__main__':
    try:
        login.login(browser)
        read_list()
        auto_star.error_flags = True
    except Exception,a:
        print Exception, ":", a
        try:
            while True:
                browser.close()
        except Exception,e:
            print Exception,":",e
    finally:
        browser.quit()
        sys.exit()
