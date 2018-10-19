from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('http://andrewmitchell.ca/properties-for-sale/6e-avenue-lasalle-montreal-h8p2k7/')

mtax = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[3]/div[4]/div[1]/div[1]/div[1]/div[23]/div[2]/div[1]').text 
mtax = mtax.replace("$", "")
mtax = mtax.replace(",","")
mtax = mtax.replace("(2018)","")
mtax = int(mtax)
stax = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[3]/div[4]/div[1]/div[1]/div[1]/div[24]/div[2]/div[1]').text
stax = stax.replace("$", "")
stax = stax.replace(",","")
stax = stax.replace("(2018)","")
stax = int(stax)
p1tax = stax + mtax
print (p1tax)
