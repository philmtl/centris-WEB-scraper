from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
insurence = int(1500)

#logs into centris https://www.thetaranights.com/login-to-a-website-using-selenium-python-python-selenium-example/

from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()

browser.get('https://www.centris.ca/en/plexes~for-sale~montreal-island?view=Thumbnail')
links = browser.find_elements_by_class_name('a-more-detail')
hrefs=list(map(lambda link: link.get_attribute('href'), links))
##map will take a list and a function, run that function for each element in the list
#for href in hrefs:
def site(self, i):
     site = (hrefs[i])
     i = hrefs[0]
     while i <= 11:
          i = i + 1


browser.get(site)

time.sleep(3)

p1price = browser.find_element_by_xpath('//span[@id="BuyPrice"]').text # id must be in "" not ''
p1revenue = browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Potential gross revenue'])[1]/following::td[1]").text

print (p1price)
print (p1revenue)
