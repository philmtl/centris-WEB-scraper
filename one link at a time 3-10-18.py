from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://www.centris.ca/en/plexes~for-sale~montreal-island')


## copy starting here
links = browser.find_elements_by_class_name('a-more-detail')
hrefs=list(map(lambda link: link.get_attribute('href'), links))
hreflist= hrefs #sxpath . teplits it into a list from all the 12 links per page
p1 = (hreflist[0])

browser.get(p1)
p1price = browser.find_element_by_xpath('//span[@id="BuyPrice"]').text # id must be in "" not ''
p1revenue = browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Potential gross revenue'])[1]/following::td[1]").text

#make into integer
p1price = p1price.replace("$", "")
p1price= p1price.replace(",","")
p1price = int(p1price)
p1revenue = p1revenue.replace("$", "")
p1revenue = p1revenue.replace(",", "")
p1revenue = int(p1revenue)

if p1revenue < 10000:
     print ("p1 revenue is wrong")

    
class url_is_not_centris(object):

  def __call__(self, driver):
    return 'centris.ca' not in driver.current_url

##for handle in browser.window_handles:
if handle != main_window_handle:
          browser.switch_to_window(handle)
          wait = WebDriverWait(browser, 10)
          element = wait.until(url_is_not_centris())
# p1tax = browser.find_element_by_xpath(' ').text
               #remax quebec
          if 'www.remax-quebec.com' in browser.current_url:
               p1tax= browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[7]/div[2]/div[5]/ul[2]/li[3]/label[2]').text
                # Sutton
          elif 'www.suttonquebec.com' in browser.current_url:
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
          elif 'vendirect.ca' in browser.current_irl:
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[7]/div[1]/ul[1]/li[3]').text
               #mrealestate
          elif 'mrealestate.com' in browser.current_irl:
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
          elif 'kwprestige.com' in browser.current_irl:
               p1tax= browser.find_element_by_xpath('/html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[5]/div[2]').text
               #the montreal real estate
          elif 'themontrealrealestate.com' in browser.current_irl:
               print ("p1 no tax info")
               #royal lepage
          elif 'www.royallepage.ca' in browser.current_irl:
               p1tax = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div[2]/div/section/div[2]/div[2]/ul/li[3]/span[2]').text
               #remax du cartier
          elif 'remaxducartier.com' in browser.current_irl:
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/aside[2]/div[2]/table[1]/tfoot[1]/tr[1]/td[1]').text
               #engel&volkers
          elif 'evcanada.com' in browser.current_irl:
               print ("p1 no tax info")
          elif 'http://andrewmitchell.ca' in browser.current_irl:
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
               #du proprio
          elif 'propriodirect.com' in browser.current_irl:
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[7]/div[1]/div[1]/ul[1]/li[3]/span[2]').text
               #guillou
          elif 'guillou.ca' in browser.current_irl:
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[5]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div[2]').text
               #remax samiraagnaou
          elif 'samiraagnaou.com' in browser.current_irl:
               p1tax = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[2]/div/div[2]/div[2]/table[4]/tbody/tr[2]/th[2]').text
               #remax rosa
          elif 'rosariarossini.com' in browser.current_irl:
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[14]/div[2]/div[3]/div[2]').text    
               #via capital
          elif 'viacapitalevendu.com' in browser.current_irl:
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[3]/div[1]/div[6]/div[2]/div[1]/div[1]/div[3]').text
          elif 'century21.ca' in browser.current_irl:
               p1tax = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/article[1]/section[5]/ul[1]/li[4]/span[2]').text
                                                     
            
p1tax = p1tax.replace("$", "")
p1tax = p1tax.replace(",","")
p1tax = int(p1tax)
print (p1tax)         

                    

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

