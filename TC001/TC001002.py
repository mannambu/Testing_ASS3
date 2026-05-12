# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC001002(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c001002(self):
        driver = self.driver
        driver.get("https://school.moodledemo.net/")
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("Student")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("moodle25")
        driver.find_element_by_id("loginbtn").click()
        driver.find_element_by_link_text("My courses").click()
        driver.find_element_by_xpath("//div[@id='course-info-container-39-4']/div/div/a/span[3]/span[2]").click()
        driver.find_element_by_xpath("//a[@onclick='']").click()
        driver.find_element_by_id("single_button69e742cb945857").click()
        driver.find_element_by_id("q131:1_sub2_answer").click()
        driver.find_element_by_id("q131:1_sub2_answer").clear()
        driver.find_element_by_id("q131:1_sub2_answer").send_keys("abc")
        driver.find_element_by_id("mod_quiz-next-nav").click()
        driver.find_element_by_xpath("//div[@id='region-main']/div[2]/div[2]/table/tbody/tr[2]/td[2]").click()
        try: self.assertEqual("Incomplete answer", driver.find_element_by_id("yui_3_18_1_1_1776763606693_50").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("single_button69e742d985bac9").click()
        driver.find_element_by_xpath("//body[@id='page-mod-quiz-summary']/div[6]/div[2]/div/div/div[3]/button[2]").click()
        driver.find_element_by_xpath("//div[@id='region-main']/div[2]/div/table/tbody/tr[6]/td").click()
        try: self.assertEqual("0.00", driver.find_element_by_xpath("//td[@id='yui_3_18_1_1_1776763619406_217']/b").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='yui_3_18_1_1_1776763619406_222']/div[2]/a").click()
        driver.find_element_by_id("user-menu-toggle").click()
        driver.find_element_by_link_text("Log out").click()
    
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
