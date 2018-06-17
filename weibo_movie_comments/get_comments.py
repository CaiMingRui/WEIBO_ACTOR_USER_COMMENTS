# -*- coding:utf-8 -*-
from __future__ import division
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import smtplib
from email.mime.text import MIMEText
from selenium.webdriver.common.action_chains import ActionChains
from xml.dom import minidom
import xml.dom.minidom
import re
import auto_star
import login
import datetime
import chardet
import os
import random
import json
import urllib
import time
import sys
import codecs
reload(sys)
sys.setdefaultencoding("utf-8")

browser = webdriver.Firefox()

def slowdown():
    for i in range(1, 4):  # at most 3 times
        browser.execute_script("window.scrollTo(100000,document.body.scrollHeight);")
        time.sleep(5)
        try:
            # 定位页面底部的换页tab
            browser.find_element_by_xpath('//span[@class="list"]/a[@action-type="feed_list_page_more"]')
            break  # 如果没抛出异常就说明找到了底部标志，跳出循环
        except:
            pass  # 抛出异常说明没找到底部标志，继续向下滑动

def save_talk(name,url,movie_id):
    checktime=0
    slowdown()  # 下滑的函数
    browser.execute_script("window.scrollTo(100000,document.body.scrollHeight);")
    ids = browser.find_elements_by_class_name("WB_feed_type")
    for id in ids:
        if checktime >= 50:
            print "Ka Ping...refresh"
            browser.refresh()
            time.sleep(20)
            checktime = 0
        talk = {}
        mid = id.get_attribute('tbinfo')
        talk['w_id'] = mid
        talk['movie_id'] = movie_id
        talk['score'] = 0
        print name,mid
        with open("./check/idcheck",'r') as checkid:
            idcheck = checkid.readlines()
            if mid+"\n" in idcheck:
                checktime=checktime+1
                time.sleep(2)
                continue
        try:
            clickt = browser.find_element_by_xpath('//div[@tbinfo=\"'+mid+'\"]//a[@class="WB_text_opt"]')
            clickt.click()
            print "open/open/open/open/open/open/open/open/open/open/open/open/open/open/open/open/open/open/open/open/open/open/open/open/"
            time.sleep(2)
        except Exception, e:
            print Exception, ":", e
        cc = browser.find_element_by_xpath('//div[@tbinfo=\"'+mid+'\"]')
        talk['time'] = browser.find_element_by_xpath('//div[@tbinfo=\"'+mid+'\"]//a[@node-type="feed_list_item_date"]').text
        talk['like_num'] = browser.find_element_by_xpath('//div[@tbinfo=\"'+mid+'\"]//span[@node-type="like_status"]/em[2]').text
        talk['forward'] = browser.find_element_by_xpath('//div[@tbinfo=\"'+mid+'\"]//span[@node-type="forward_btn_text"]/span/em[2]').text
        try:
            pathB ='//div[@tbinfo=\"'+mid+'\"]//div[@node-type="feed_list_content_full"]'
            talk['content'] = browser.find_element_by_xpath(pathB).text
        except Exception,e:
            print Exception,":",e
            print 'unknow......'
            talk['content'] = browser.find_element_by_xpath('//div[@tbinfo=\"'+mid+'\"]//div[@node-type="feed_list_content"]').text
        print talk
        with open("./save/" + name + ".json", 'a') as jf:
            json.dump(talk, jf, ensure_ascii=False)
            jf.write("\n")
        with open("./check/idcheck",'a') as saveid:
            saveid.write(mid+'\n')
        time.sleep(2)

def get_url(name,movie_id):
    browser.get("https://s.weibo.com/weibo/" + urllib.quote(name.replace('\n','')) + "&Refer=p")
    print "https://s.weibo.com/weibo/" + urllib.quote(name.replace('\n','')) + "&Refer=p"
    try:
        WebDriverWait(browser, 15, 3).until(lambda browser: browser.find_element_by_class_name("wbs_interest_dir"))
    except:
        pass
    try:
        browser.find_element_by_class_name("wbs_interest_dir")
        print name+"找到相关微博"
        # url = browser.find_element_by_xpath("//div[@class='wbs_interest_dir']/div[@class='interest_content']/div[@class='film_content']/div[@class='pic']/a").get_attribute('href')
        url = browser.find_element_by_class_name('film_content').find_element_by_xpath('//div[@class="pic"]/a').get_attribute('href')
        print "get",name.replace('\n',''),url
        browser.get(url + '/review?feed_filter=1')
        print browser.current_url
        try:
            WebDriverWait(browser, 20, 3).until(lambda browser: browser.find_element_by_class_name("WB_feed_v3"))
        except:
            pass
        print browser.current_url

        save_talk(name,url,movie_id)

        while(check_nextpage()):
            time.sleep(3)
            ClickBtn = browser.find_element_by_link_text("下一页")
            ClickBtn.click()
            time.sleep(10*random.random())
            # try:
            #     WebDriverWait(browser, 20, 3).until(lambda browser: browser.find_element_by_class_name("WB_feed_v3"))
            # except Exception,e:
            #     print Exception,":",e
            save_talk(name,url,movie_id)
    except Exception,e:
        print Exception,":",e


def check_nextpage():
    try:
        browser.find_element_by_link_text("下一页")
        print "found next PAGE"
        return True
    except:
        print "This is the last page"
        return False

def get_movieurl():
    with open("./a",'r') as r:
        text = r.readlines()
        for i in text:
            name = i.split("@@")[0]
            movie_id = i.split("@@")[1].replace('\n','')
            with open("./check/name_check",'r') as m:
                if name in m.readlines():
                    continue
            get_url(name,movie_id)
            with open("./check/name_check",'a') as dow:
                dow.write(name+'\n')
            print "finish one of it"
            sys.exit()

def star():
    auto_star.error_flags = 'alse'
    login.login(browser)
    get_movieurl()
    auto_star.error_flags = 'ok'

if __name__ == '__main__':
    star()


