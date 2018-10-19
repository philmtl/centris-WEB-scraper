from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://www.centris.ca/en/login?returnUrl=%2f') 
time.sleep(3)
username = browser.find_element_by_id('loginradius-login-emailid')
password = browser.find_element_by_id('loginradius-login-password')
username.send_keys("moreaup50@hotmail.com")
password.send_keys("creative1")
login_attempt = browser.find_element_by_xpath('//*[@id="loginradius-submit-login"]')
login_attempt.submit()
time.sleep(3)
browser.get('https://www.centris.ca/en/my-searches')
time.sleep(2)
browser.find_element_by_css_selector('a.btn:nth-child(1)').click()



