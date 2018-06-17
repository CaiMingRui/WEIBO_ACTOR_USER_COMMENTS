# -*- coding:utf-8 -*-
from __future__ import division
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import re
import auto_star
import login
import os
import random
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
uchtime = 1
browser = webdriver.Firefox(executable_path='./geckodriver')

def rebrowser():
    return browser

def init_spider():
    login.login(browser)
    # browser.get("http://weibo.com/")
    # while True:
    #     a = raw_input("deng lu")
    #     if(a=='Y' or a == 'y'):
    #         break

def load_req():
    years = os.listdir('./ok')
    for year in years:
        movies = os.listdir('./ok/'+str(year))
        for movie in movies:
            with open('./ok/'+str(year)+'/'+movie,'r') as mr:
                lines = mr.readlines()
                for line in lines:
                    username = re.findall("\[user_name\]\:(.*?)\[/user_name\]",line)[0]
                    userurl = re.findall("\[user_url\]\:(.*?)\[/user_url\]",line)[0]
                    userurl = userurl.replace('http://https','https')
                    exec_spider(year,username,userurl,movie)

def exec_spider(year,name,url,movie):
    global uchtime
    print "*******************************" + year, name + "************************************"
    url = url.replace('?refer_flag=1001205010_','?profile_ftype=1&is_all=1#_0')
    print url
    with open('./totle','a+') as check:
        finish = check.read()
        if(url in finish):
            print '用户已存在'
            return
        else:
            uchtime = uchtime+1
            if(uchtime%15 == 0):
                print "休息时间"
                sys.exit()
            get_page(year,name,url,movie)
            check.write(url+'\n')
            print "登记"+url+"成功"

def get_page(year,name,url,movie):
    print "开始进入",name,url
    if ('/u/' in url):
        id = re.findall("https\://weibo\.com/u/(\d+)", url)[0]
    else:
        id = re.findall("https\://weibo\.com/([\w]+)", url)[0]
    browser.get(url)
    try:
        WebDriverWait(browser, 15, 3).until(lambda browser:browser.find_element_by_class_name('WB_frame_c'))
      # WebDriverWait(browser, 30, 3).until(lambda browser:browser.find_element_by_xpath('//div[@class="PCD_counter"]/div[@class="WB_innerwrap"]/table[@class="tb_counter"]/tbody/tr/td/a[@class="t_link S_txt1"]'))
    except:
        pass
    contents = []
    downt = 0
    while(downt<=6):
        # try:
        #     browser.find_element_by_class_name('WB_empty')
        #     break
        # except:
        #     pass
        try:
            # 定位页面底部的换页tab
            browser.find_element_by_class_name('next')
            break  # 如果没抛出异常就说明找到了底部标志，跳出循环
        except:
            browser.execute_script("window.scrollTo(100000,document.body.scrollHeight);")
            pass  # 抛出异常说明没找到底部标志，继续向下滑动
        # browser.execute_script("window.scrollTo(100000,document.body.scrollHeight);")
        try:
            WebDriverWait(browser, 5, 1).until(lambda browser: browser.find_element_by_class_name('W_pages'))
        except Exception,mm:
            print Exception,":",mm
        downt = downt+1
    homepaget = 1
    while(homepaget<=5):
        print homepaget

        # try:
        #     browser.find_element_by_class_name('WB_empty')
        #     contents.append(browser.page_source)
        #     break
        # except:
        #     pass
        downt = 0
        content = browser.page_source
        print browser.current_url
        if content not in contents:
            contents.append(content)
        homepaget = homepaget + 1
        time.sleep(10*random.random())
        try:
            nexc = browser.find_element_by_class_name('next')
            print "find next_page"
            nexc.click()
            time.sleep(5)
            try:
                WebDriverWait(browser, 15, 3).until(lambda browser: browser.find_element_by_class_name('WB_frame_c'))
            except Exception,g:
                print Exception,":",g
                pass
            while (downt <= 6):
                try:
                    # 定位页面底部的换页tab
                    browser.find_element_by_class_name('next')
                    break  # 如果没抛出异常就说明找到了底部标志，跳出循环
                except:
                    browser.execute_script("window.scrollTo(100000,document.body.scrollHeight);")
                    pass  # 抛出异常说明没找到底部标志，继续向下滑动

                downt = downt + 1
                try:
                    WebDriverWait(browser, 5, 1).until(lambda browser: browser.find_element_by_class_name('W_pages'))
                except Exception,nn:
                    print Exception,":",nn

        except Exception,ll:
            print Exception,":",ll,"ayahahduhasdgshafhdishfihdskjifhiusa"



    try:
        browser.refresh()
        WebDriverWait(browser, 15, 3).until(lambda browser:browser.find_element_by_class_name('WB_frame_c'))
    except:
        print '????'
    try:
        infoBtn = browser.find_element_by_xpath("//a[contains(@href,'info?mod=pedit_more')]")
        infoBtn.click()
    except:
        try:
            infoBtn = browser.find_element_by_xpath("//a[contains(@href,'about')]")
            infoBtn.click()
        except:
            browser.get('https://weibo.com/p/100505'+str(id)+'/info?mod=pedit_more')
            time.sleep(5)
            if '抱歉，你访问的页面地址有误，或者该页面不存在' in browser.page_source:
                browser.get('https://weibo.com/p/100505'+str(id)+'/about')

    try:
        browser.refresh()
        WebDriverWait(browser, 15, 3).until(lambda browser:browser.find_element_by_xpath("//a[contains(@href,'follow?from=page')]"))
    except:
        print '?????'
    print "进入资料页..."
    time.sleep(random.random()+10*random.random())
    infopage = browser.page_source
    infourl = browser.current_url
    print "资料页获取完毕..."
    try:
        followBtn = browser.find_element_by_xpath("//a[contains(@href,'follow?from=page')]")
        followBtn.click()
    except:
        browser.get(infourl.replace('about','follow'))
    try:
        browser.refresh()
        WebDriverWait(browser, 15, 3).until(lambda browser:browser.find_element_by_xpath('//div[@class="WB_frame"]/div[@id="plc_main"]'))
    except:
        print "??????"
        time.sleep(5)
    print "进入关注页..."
    times = 1
    followpages=[]
    followurl = browser.current_url
    while(times<=5):
        print browser.current_url
        try:
            times=times+1
            followpage = browser.page_source
            if followpage not in followpages:
            	followpages.append(followpage)
            try:
                browser.execute_script("window.scrollTo(100000,document.body.scrollHeight);")
                nextpage = browser.find_element_by_class_name("next")
                print "found nextpage"
                nextpage.click()
                time.sleep(5)
            except:
                print "try second way"
                nexturl = nextpage.get_attribute('href')
                allurl = nexturl
                browser.get(allurl)
            WebDriverWait(browser, 15, 3).until(lambda browser:browser.find_element_by_class_name('W_pages'))
        except Exception,b:
            print Exception,":",b
            pass
    print "关注获取完毕..."
    time.sleep(random.random()+10*random.random())

    if((os.path.exists('./page/'+str(year)+"/"+movie))==False):
        os.mkdir('./page/'+str(year)+"/"+movie)
    if ((os.path.exists('./page/' + str(year) + "/" + movie+"/"+name)) == False):
        os.mkdir('./page/' + str(year) + "/" + movie+"/"+name)
    with open('./page/'+str(year)+"/"+movie+"/"+name+"/infomation.html",'w') as sa:
        sa.write(infopage)
    for i in range(1,6):
        try:
            with open('./page/' + str(year) + "/" + movie + "/" + name + "/like_0"+str(i)+".html", 'w') as ff:
                ff.write(followpages[i-1])
        except:
            pass
    for i in range(1,6):
        try:
            with open('./page/' + str(year) + "/" + movie + "/" + name + "/content_0"+str(i)+".html", 'w') as gg:
                gg.write(contents[i-1])
        except:
            pass

def star():
    init_spider()
    load_req()

def autostar():
    try:
        star()
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

if __name__ == '__main__':
    autostar()
