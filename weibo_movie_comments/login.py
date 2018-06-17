# -*- coding:utf-8 -*-
from __future__ import division
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")



def login(browser,username = '',password = unicode('').encode('utf-8')):
    browser.get("http://weibo.com/")
    browser.maximize_window()
    try:
        WebDriverWait(browser,30,3).until(lambda browser:browser.find_element_by_xpath('//div[@class="info_list username"]/div/input[@id="loginname"]'))
        userBtn = browser.find_element_by_xpath('//div[@class="info_list username"]/div/input[@id="loginname"]')
        userBtn.click()
        userBtn.clear()
        userBtn.send_keys(username)
        # time.sleep(2)
        passBtn = browser.find_element_by_xpath('//div[@class="info_list password"]/div/input[@type="password"]')
        passBtn.clear()
        passBtn.click()
        # ActionChains.move_to_element(userBtn).click()

        # time.sleep(2)
        # ActionChains.move_to_element(passBtn).click()
        passBtn.send_keys(password)
        time.sleep(1)
        Btn=browser.find_element_by_xpath("//div[@class='info_list login_btn']/a/span[@node-type='submitStates']")
        ActionChains(browser).move_to_element(Btn).perform()
        Btn.click()
        WebDriverWait(browser, 30, 3).until(lambda browser: browser.find_element_by_xpath('//div[@class="WB_innerwrap"]/div[@class="nameBox"]'))
        print "----------------------------have been logined and try to get search page-----------------------"
        time.sleep(10*random.random())
    except Exception,r:
        print '*******************************login('+username+') fail******************************'
        print Exception,":",r
        print '*******************************login('+username+') fail******************************'
