# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import unittest
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
       # self.wd = By()
        self.wd.implicitly_wait(60)

    def login(self, wd, username, passwd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(passwd)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def open_group_list(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_new_group(self, wd, group):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.gp_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.gp_header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.gp_footer)
        wd.find_element_by_name("submit").click()

    def return_to_groups(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", passwd="secret")
        #wd.find_element_by_xpath("//input[@value='Login']").click()
        self.open_group_list(wd)
        self.create_new_group(wd, Group(name="group1", header="group header 1", footer="group footer 1"))
        self.return_to_groups(wd)
        self.logout(wd)
        self.assertTrue(success)

    def test_add_empty_named_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", passwd="secret")
        #wd.find_element_by_xpath("//input[@value='Login']").click()
        self.open_group_list(wd)
        self.create_new_group(wd, Group(name="", header="", footer=""))
        self.return_to_groups(wd)
        self.logout(wd)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
