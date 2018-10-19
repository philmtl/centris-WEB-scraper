from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
insurence = int(1500)

#logs into centris https://www.thetaranights.com/login-to-a-website-using-selenium-python-python-selenium-example/

from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://www.centris.ca/en/plexes~for-sale~montreal-island?view=Thumbnail')
time.sleep(2)
p1mrev = browser.find_element_by_css_selector('div.thumbnailItem:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > a:nth-child(2)').click()

