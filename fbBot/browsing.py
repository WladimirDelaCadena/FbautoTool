import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
from random import randint

def postcontent():
	goFeed()
	posts = np.loadtxt("res/publ", dtype = 'str', delimiter = '\n')
	anypost = posts[randint(0,len(posts)-1)]
	anypost = unicode(anypost, errors='replace')
	publication = driver.find_element_by_id('pagelet_composer')
 	publication.click()
	time.sleep(2)
	pyautogui.typewrite(anypost)
	post_it = driver.find_element_by_xpath("//button/span[.=\"Publicar\"]")
	post_it.click()
	time.sleep(2)

def readnotification():
	goFeed()
	notification = driver.find_element_by_id('fbNotificationsJewel')
	notification.click()
	n = [2,5,8,11,14,17,20,23]
	h = n[randint(0,len(n)-1)]
	for i in xrange(0,h):
		pyautogui.press('tab')
		time.sleep(0.5)
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.press('esc')
	time.sleep(2)
def goFeed():
	driver.get('http://www.facebook.com')
	#home =  driver.find_element_by_class_name('_19eb')
	#home.click()
	time.sleep(2)

def share():
	goFeed()
	try:
		yspan = 100* randint(5,20)
		driver.execute_script("window.scrollTo(0,"+ str(yspan) + ")")
		time.sleep(1)
		sh = driver.find_element_by_link_text('Compartir')
		sh.click()
		time.sleep(1)
		sh1 =  driver.find_element_by_link_text('Compartir ahora (Amigos)')
		sh1.click()
		print 'Sharing done!!'
		return 1
	except:
		print 'Sharing not possible'
		return 0	


def photoBrowse():
	print 'browsing picture'
	pics_url = np.loadtxt("res/pics", dtype = 'str', delimiter = '\n')
	ch_url = pics_url[randint(0,len(pics_url)-1)]
	driver.get(ch_url)
	time.sleep(2)


def profileBrowse():
	print 'browsing profile'
	profile_url = np.loadtxt("res/profiles", dtype = 'str', delimiter = '\n')
	ch_profile = profile_url[randint(0,len(profile_url)-1)]
	driver.get(ch_profile)
	driver.execute_script("window.scrollTo(0,1000)")
	time.sleep(2)

def navigate(action):
	if action == 0:
		goFeed()
	if action == 1:
		readnotification()
	if action == 2:
		share()
	if action == 3:
		photoBrowse()
	if action == 4:
		profileBrowse()
	if action == 5:
		postcontent()
	
		
#Loging to fb	
usr ='@.com'
pwd = 'h'
options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver" , chrome_options=options)
driver.get('http://www.facebook.org')
time.sleep(2)
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
#
#Browsing
br = np.loadtxt("cls_ok.csv", dtype = 'str', delimiter = '\n')
for i in xrange(0,10):
	ac = br[i].split(',')
	print 'Current Session', ac
	for j in xrange(0,len(ac)):
		navigate(int(ac[j]))
	time.sleep(3)	
#driver.quit()
