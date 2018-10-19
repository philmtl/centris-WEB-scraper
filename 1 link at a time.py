from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://www.centris.ca/en/plexes~for-sale~montreal-island')


## copy starting here
links = browser.find_elements_by_class_name('a-more-detail')
hrefs=list(map(lambda link: link.get_attribute('href'), links))
hreflist= hrefs #splits it into a list from all the 12 links per page
p1 = (hreflist[0])
print (p1)

browser.get(p1)
p1price = browser.find_element_by_xpath('//span[@id="BuyPrice"]').text # id must be in "" not ''
p1revenue = browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Potential gross revenue'])[1]/following::td[1]").text
p1price = p1price.replace("$", "")
p1revenue = p1revenue.replace("$", "")

nump1rev = int(p1price)
print (nump1rev)




                    

p2 = (hreflist[1])
p3 = (hreflist[2])
p4 = (hreflist[3])
p5 = (hreflist[4])
p7 = (hreflist[5])
p8 = (hreflist[6])
p8 = (hreflist[7])
p9 = (hreflist[8])
p10 = (hreflist[9])
p11 = (hreflist[10])
p12 = (hreflist[11])

