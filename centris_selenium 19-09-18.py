from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


#logs into centris https://www.thetaranights.com/login-to-a-website-using-selenium-python-python-selenium-example/

from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://www.centris.ca/en/login?returnUrl=%2f') 
time.sleep(10)
username = browser.find_element_by_id('loginradius-login-emailid')
password = browser.find_element_by_id('loginradius-login-password')
username.send_keys("moreaup50@hotmail.com")
password.send_keys("creative1")
login_attempt = browser.find_element_by_xpath('//*[@id="loginradius-submit-login"]')
login_attempt.submit()

#get to favroits
browser.get('https://www.centris.ca/en/my-searches')
view = browser.find_element_by_partial_link_text('VIEW')



links = browser.find_elements_by_class_name('a-more-detail')
hrefs=list(map(lambda link: link.get_attribute('href'), links))


##map will take a list and a function, run that function for each element in the list
#for href in hrefs:
href = hrefs[0]
browser.get(href)    ## the href gives you what its equal too
details = browser.find_element_by_css_selector('.details .btn') # find the element btn INSIDE element details
main_window_handle = browser.current_window_handle
details.click()

class url_is_not_centris(object):

  def __call__(self, driver):
    return 'centris.ca' not in driver.current_url

for handle in browser.window_handles:
     if handle != main_window_handle:
          browser.switch_to_window(handle)
          wait = WebDriverWait(browser, 10)
          element = wait.until(url_is_not_centris())
          if 'www.proprietes-a-vendre-montreal.com' in browser.current_url:
               # run some code that will find the taxes andd revenue blabla

               ##price=browser.find_element_by_id('BuyPrice')
               print(browser.find_element_by_class_name('total_detail').text)
          elif 'www.remax-quebec.com' in browser.current_url:
               # run some code for Remax
               print(browser.find_element_by_class_name('Financials__Data').text) # taxes 
               print(browser.find_element_by_class_name('Financials__Data').text)




