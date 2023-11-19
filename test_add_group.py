# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
#.Chrome(executable_path=r'')
        self.wd.implicitly_wait(60)

    def test_test_add_group(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("group1")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("group header 1")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("group footer 1")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()
        # wd.get("http://localhost/addressbook/")
        # wd.find_element("user").click()
        # wd.find_element("user").clear()
        # wd.find_element("user").send_keys("admin")
        # wd.find_element("pass").clear()
        # wd.find_element("pass").send_keys("secret")
        # wd.find_element("//input[@value='Login']").click()
        # wd.find_element("groups").click()
        # wd.find_element("new").click()
        # wd.find_element("group_name").click()
        # wd.find_element("group_name").clear()
        # wd.find_element("group_name").send_keys("group1")
        # wd.find_element("group_header").click()
        # wd.find_element("group_footer").click()
        # wd.find_element("group_header").clear()
        # wd.find_element("group_header").send_keys("group header 1")
        # wd.find_element("group_footer").clear()
        # wd.find_element("group_footer").send_keys("group footer 1")
        # wd.find_element("submit").click()
        # wd.find_element("group page").click()
        # wd.find_element("Logout").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
