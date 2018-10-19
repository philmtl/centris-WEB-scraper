# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.centris.ca/en/login?returnUrl=%2fen")
        driver.find_element_by_id("loginradius-login-emailid").click()
        driver.find_element_by_id("loginradius-login-emailid").clear()
        driver.find_element_by_id("loginradius-login-emailid").send_keys("moreaup50@hotmail.com")
        driver.find_element_by_id("loginradius-login-password").click()
        driver.find_element_by_id("loginradius-login-password").clear()
        driver.find_element_by_id("loginradius-login-password").send_keys("creative1")
        driver.find_element_by_id("loginradius-submit-login").click()
        time.sleep(2)
        driver.find_element_by_link_text("Hello moreaup50").click()
        time.sleep(1.5)
        ActionChains(driver).key_down(Keys.COMMAND).send_keys("t").key_up(Keys.COMMAND).perform
        driver.get('https://www.centris.ca/en/my-searches')
        time.sleep(2)
        driver.find_element_by_link_text('View .btn').click()
        
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
