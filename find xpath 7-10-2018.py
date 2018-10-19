from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


#logs into centris https://www.thetaranights.com/login-to-a-website-using-selenium-python-python-selenium-example/

from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('http://www.lyndaboucher.com/en/duplex-mercier-hochelaga-maisonneuve-montreal/mls/21817105') 
time.sleep(5)

p1tax = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/aside[2]/div[2]/div/table[2]/tfoot/tr/td').text
p1tax = p1tax.replace("$","")
p1tax = p1tax.replace(" ","")
print (p1tax)
