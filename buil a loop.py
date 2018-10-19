from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://www.centris.ca/en/plexes~for-sale~montreal-island?view=Thumbnail') 

links = browser.find_elements_by_class_name('a-more-detail')
hrefs=list(map(lambda link: link.get_attribute('href'), links))

i=0
while i < len(hrefs):
     browser.get(hrefs[i])
     

p1mrev = 305

if p1mrev > 300:
     print('is worth looking into')
     
else:
     print ('p1 is not worth it')

     if p1mrev is (True or False):
          i += 1
