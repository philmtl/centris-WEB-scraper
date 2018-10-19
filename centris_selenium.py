from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class url_is_not_centris(object):

  def __call__(self, driver):
    return 'centris.ca' not in driver.current_url

browser = webdriver.Firefox()
browser.get('https://www.centris.ca/en/plexes~for-sale~montreal-island')




links = browser.find_elements_by_class_name('a-more-detail')
hrefs=list(map(lambda link: link.get_attribute('href'), links))


##map will take a list and a function, run that function for each element in the list
#for href in hrefs:
href = hrefs[0]
browser.get(href)    ## the href gives you what its equal too
##price=browser.find_element_by_id('BuyPrice')
details = browser.find_element_by_css_selector('.details .btn') # find the element btn INSIDE element details
main_window_handle = browser.current_window_handle
details.click()

for handle in browser.window_handles:
     if handle != main_window_handle:
          browser.switch_to_window(handle)
          wait = WebDriverWait(browser, 10)
          element = wait.until(url_is_not_centris())
          if 'www.proprietes-a-vendre-montreal.com' in browser.current_url:
               # run some code that will find the taxes andd revenue blabla
               print(browser.find_element_by_class_name('total_detail').text)
          elif 'www.remax-quebec.com' in browser.current_url:
               # run some code for Remax
               print(browser.find_element_by_class_name('Financials__Data').text) # taxes 
               print(browser.find_element_by_class_name('Financials__Data').text)




