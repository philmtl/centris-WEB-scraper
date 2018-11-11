## need selenium 
import pdb
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
##map will take a list and a function, run that function for each element in the list
#for href in hrefs:
print(hrefs)
main_window_handle = ''

for href in hrefs:
    print(href)
    browser.get(href)
    if main_window_handle:
        browser.switch_to_window(main_window_handle)

    # pdb.set_trace()
    #we need to add +1 to loop or fix some other way
    p1price = browser.find_element_by_xpath('//span[@id="BuyPrice"]').text # id must be in "" not ''
    p1price = p1price.replace("$", "")
    p1price = p1price.replace(" ", "")
    p1price= p1price.replace(",","")
    p1price = float(p1price)
    #need to add a try block or somthing when theres no revenue
    try:
        p1revenue = browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Potential gross revenue'])[1]/following::td[1]").text
        p1revenue = p1revenue.replace("$", "")
        p1revenue = p1revenue.replace(",", "")
        p1revenue = p1revenue.replace(" ", "")
        p1revenue = float(p1revenue)
    except: 
        print("no  potential revenue")
    details = browser.find_element_by_css_selector('.details .btn') # find the element btn INSIDE element details
    main_window_handle = browser.current_window_handle
    main_window_handle_1 = browser
    details.click()
    time.sleep(3)
    
    class url_is_not_centris(object):

     def __call__(self, driver):
         return 'centris.ca' not in driver.current_url

    ##for handle in browser.window_handles:
    for handle in browser.window_handles:
     if handle != main_window_handle:
          browser.switch_to_window(handle)
          wait = WebDriverWait(browser, 10)
          element = wait.until(url_is_not_centris())
               #remax quebec
          if 'www.remax-quebec.com' in browser.current_url:
               time.sleep(2)
               p1tax= browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[7]/div[2]/div[5]/ul[2]/li[3]/label[2]').text
                # Sutton
          elif 'www.suttonquebec.com' in browser.current_url:
               time.sleep(2)
               mtax = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/article[1]/div[4]/div[2]/div[1]/div[3]/ul[1]/li[4]/div[1]/table[1]/tbody[1]/tr[3]/td[2]').textstax = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/article[1]/div[4]/div[2]/div[1]/div[3]/ul[1]/li[4]/div[1]/table[1]/tbody[1]/tr[4]/td[2]').text
               mtax = mtax.replace("$", "")
               mtax = mtax.replace(",","")
               mtax = mtax.replace(".00","")
               mtax = int(mtax)
               stax = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/section[2]/div[1]/article[1]/ul[1]/li[2]/span[1]').text
               stax = stax.replace("$", "")
               stax = stax.replace(",","")
               stax = stax.replace(".00","")
               stax = int(stax)
               p1tax = stax + mtax
               #vendiect
          elif 'vendirect.ca' in browser.current_url:
               time.sleep(2)
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[7]/div[1]/ul[1]/li[3]').text
               #mrealestate
          elif 'mrealestate.com' in browser.current_url:
               time.sleep(2)
               mtax = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/section[2]/div[1]/article[1]/ul[1]/li[1]/span[1]').text
               mtax = mtax.replace("$", "")
               mtax = mtax.replace(",","")
               mtax = int(mtax)
               stax = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/section[2]/div[1]/article[1]/ul[1]/li[2]/span[1]').text
               stax = stax.replace("$", "")
               stax = stax.replace(",","")
               stax = int(stax)
               p1tax = stax + mtax
               #kwprestige
          elif 'kwprestige.com' in browser.current_url:
               time.sleep(2)
               p1tax= browser.find_element_by_xpath('/html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[5]/div[2]').text
               #the montreal real estate
          elif 'themontrealrealestate.com' in browser.current_url:
               time.sleep(2)
               print ("p1 no tax info")
               #royal lepage
          elif 'www.royallepage.ca' in browser.current_url:
               time.sleep(2)
               p1tax = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div[2]/div/section/div[2]/div[2]/ul/li[3]/span[2]').text
               #remax du cartier
          elif 'remaxducartier.com' in browser.current_url:
               time.sleep(2)
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/aside[2]/div[2]/table[1]/tfoot[1]/tr[1]/td[1]').text
               #engel&volkers
          elif 'evcanada.com' in browser.current_url:
               time.sleep(2)
               print ("p1 no tax info")
          elif 'http://andrewmitchell.ca' in browser.current_url:
               time.sleep(2)
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
               #du proprio
          elif 'propriodirect.com' in browser.current_url:
               time.sleep(2)
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[7]/div[1]/div[1]/ul[1]/li[3]/span[2]').text
               #guillou
          elif 'guillou.ca' in browser.current_url:
               time.sleep(2)
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[5]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div[2]').text
               #remax philipwenda
          elif 'philipwenda.com' in browser.current_url:
               time.sleep(2)
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/form[1]/div[3]/div[4]/div[11]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[2]').text 
          elif 'samiraagnaou.com' in browser.current_url:
               time.sleep(2)
               p1tax = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[2]/div/div[2]/div[2]/table[4]/tbody/tr[2]/th[2]').text
               #remax rosa
          elif 'rosariarossini.com' in browser.current_url:
               time.sleep(2)
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[14]/div[2]/div[3]/div[2]').text    
               #via capital
          elif 'viacapitalevendu.com' in browser.current_url:
               time.sleep(2)
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[3]/div[1]/div[6]/div[2]/div[1]/div[1]/div[3]').text
          elif 'century21.ca' in browser.current_url:
               time.sleep(2)
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/article[1]/section[5]/ul[1]/li[4]/span[2]').text
               # lidya boucher
          elif 'lyndaboucher.com' in browser.current_url:
               time.sleep(5)
               p1tax = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/aside[2]/div[2]/div/table[2]/tfoot/tr/td').text                                  
    p1tax = p1tax.replace("$", "")
    p1tax = p1tax.replace(" ", "")
    p1tax = float(p1tax)
    
    p1afterd = ((p1price)*(0.9))
    p1mort = (((p1afterd)/(100000))*5600)
    p1mrev = (((p1revenue) - (p1mort) - (p1tax)- (insurence))/12)          
    print (p1mrev) # monthly revenue
    browser.close(handle)
    

    
