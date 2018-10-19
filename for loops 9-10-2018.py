from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
insurence = int(1500)

#logs into centris https://www.thetaranights.com/login-to-a-website-using-selenium-python-python-selenium-example/

from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://www.centris.ca/en/login?returnUrl=%2f') 
time.sleep(5)
username = browser.find_element_by_id('loginradius-login-emailid')
password = browser.find_element_by_id('loginradius-login-password')
username.send_keys("moreaup50@hotmail.com")
password.send_keys("creative1")
login_attempt = browser.find_element_by_xpath('//*[@id="loginradius-submit-login"]')
login_attempt.submit()
time.sleep(2)
#get to searches
browser.get('https://www.centris.ca/en/my-searches')
time.sleep(3)
browser.find_element_by_css_selector('a.btn:nth-child(1)').click() # clicks view button


# go to link 1

links = browser.find_elements_by_class_name('a-more-detail')
hrefs=list(map(lambda link: link.get_attribute('href'), links))

for i in hrefs:
