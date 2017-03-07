#coding:utf-8
from selenium import webdriver
import time
import base64

browser=webdriver.Chrome() #浏览器
kch = "311084030"   #课程号
#kch = "311151030"     #课程号
kxh = "01"			  #课序号

def isElementExist(_browser, _string, _type):
	flag=True
	browser=_browser
	try:
		if _type == 'name':
			browser.find_element_by_name(_string)
		elif _type == 'xpath':
			browser.find_element_by_xpath(_string)
		elif _type == 'text':
			browser.find_element_by_link_text(_string)
		return flag
	except:
		flag=False
		return flag
            
def phase1():
	#打开网址，并登录
	browser.get("http://202.115.47.141/login.jsp")
	s1 = base64.decodestring('')
	s2 = base64.decodestring('')
	while False == isElementExist(browser, "zjh", "name"):            #若打开失败则重新打开
			browser.get("http://202.115.47.141/login.jsp")
	browser.find_element_by_name("zjh").send_keys(s1)
	browser.find_element_by_name("mm").send_keys(s2)
	browser.find_element_by_id("btnSure").click()
	phase2()

def phase2():
	#打开选课管理界面
	path = "//*[@id='divCoHome']/table/tbody/tr/td[2]/table/tbody/tr[1]//*[@class='hometopBg1']/tbody/tr/td/a"
	browser.switch_to_default_content()
	browser.switch_to_frame("bottomFrame")
	browser.switch_to_frame("mainFrame")
	while False == isElementExist(browser, path, "xpath"):		#失败刷新页面， 回退到phase1
		browser.refresh()
		phase1()
	browser.find_element_by_xpath(path).click()
	phase3()
	
def phase3():	
	#打开选课方案界面
	browser.switch_to_default_content()
	browser.switch_to_frame("bottomFrame")
	browser.switch_to_frame("menuFrame")
	path = "//*[@id='Xkgl']//*[@class='content2']/tbody/tr[2]/td/a"
	while False == isElementExist(browser, path, "xpath"):	     #失败刷新页面, 回退到phase1
		browser.refresh()
		phase1()
	browser.find_element_by_xpath(path).click()
	phase4()
	
def phase4():
	#搜索课程
	browser.switch_to_default_content()
	browser.switch_to_frame("bottomFrame")
	browser.switch_to_frame("mainFrame")
	text = '自由选择'
	while False == isElementExist(browser, text, "text"):	     #失败刷新页面, 回退到phase2
		browser.refresh()
		phase2()
	browser.find_element_by_link_text(text).click()
	browser.switch_to_frame("inforUpContent")
	while False == isElementExist(browser, "kch", "name"):	     #失败刷新页面, 回退到phase2
		browser.refresh()
		phase2()
	browser.find_element_by_name("kch").send_keys(kch)
	browser.switch_to.parent_frame()
	browser.find_element_by_xpath("//*[@title='确定']").click()
	phase5()

def phase5():
	#选择课程
	browser.switch_to_frame("inforUpContent")
	value = kch+'_'+kxh
	path = "//*[@value='%s']"%value
	while False == isElementExist(browser, path, "xpath"):	     #失败刷新页面, 回退到phase2
		browser.refresh()
		phase2()
	browser.find_element_by_xpath(path).click()
	browser.switch_to.parent_frame()
	browser.find_element_by_xpath("//*[@title='确定']").click()
	
def main(): 

	phase1()
		
	#等待用户输入退出
	waitkey=raw_input()
	browser.quit()
	
if __name__ == '__main__':
    main()