# coding:utf-8
# pip install pyvirtualdisplay
# pip install selenium
# 
# from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import platform

def oskillproc(osname):
    if osname=='Windows':
        os.system('taskkill /F /IM google/chrome.exe')
    else:
        os.system('pkill google/chrome')
        
def oscheckproc(osname):
    if osname=='Windows':
        tmpstr=os.popen('tasklist | find "google/chrome"').read()
    else:
        tmpstr=os.popen('ps aux | grep google/chrome | grep -v grep').read()
    return tmpstr==''

osname=platform.system()
oskillproc(osname)

# if osname=='Linux':
#     print('Linux Detected!')
#     display = Display(visible=0, size=(1920, 1080))
#     display.start()
        
import uuid
tmpnode = uuid.getnode()
macasname = uuid.UUID(int = tmpnode).hex[-12:]
macasname = str(uuid.uuid1())

while 1:
    try:
        nowtime=time.time()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--no-sandbox")
        #chrome_options.add_extension("~/alexa.crx")
        chrome = webdriver.Chrome(chrome_options=chrome_options)
        chrome.execute_script('''window.open('https://www.alexamaster.net/Master/67977','_blank')''')
        ##chrome.get('chrome-extension://cknebhggccemgcnbidipinkifmmegdel/html/welcome.html')
        ##chrome.find_element_by_id("accept").click()
        chrome.get('http://ebesucher.de/surfbar/ebcccac.nom%s'%macasname)
        while time.time()-nowtime < 1800:
            if oscheckproc(osname):
                raise Exception('firefox proc not living')
            time.sleep(10)
            pass
        try:
            chrome.quit()
        except Exception as e:
            print(e)
        oskillproc(osname)
    except Exception as e:
        oskillproc(osname)
        print(e)
