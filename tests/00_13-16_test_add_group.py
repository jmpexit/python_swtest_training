# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from time import sleep
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
       #self.binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
       #path = ("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        #self.profile = webdriver.FirefoxProfile()
        #self.wd = webdriver.Firefox(capabilities={"marionette": False})
        #self.wd = webdriver.Firefox(firefox_binary=binary, firefox_profile=profile)
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.implicitly_wait(20)

    def login(self, wd, username, passwd):
        wd.find_element(By.NAME, 'user').click()
        wd.find_element(By.NAME, 'user').clear()
        wd.find_element(By.NAME, 'user').send_keys(username)
        wd.find_element(By.NAME, 'pass').click()
        wd.find_element(By.NAME, 'pass').clear()
        wd.find_element(By.NAME, 'pass').send_keys(passwd)
        wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()

    def open_group_list(self, wd):
        wd.find_element(By.LINK_TEXT, 'groups').click()

    def create_new_group(self, wd, group):
        wd.find_element(By.NAME, 'new').click()
        wd.find_element(By.NAME, 'group_name').click()
        wd.find_element(By.NAME, 'group_name').clear()
        wd.find_element(By.NAME, 'group_name').send_keys(group.gp_name)
        wd.find_element(By.NAME, 'group_header').click()
        wd.find_element(By.NAME, 'group_footer').click()
        wd.find_element(By.NAME, 'group_header').clear()
        wd.find_element(By.NAME, 'group_header').send_keys(group.gp_header)
        wd.find_element(By.NAME, 'group_footer').clear()
        wd.find_element(By.NAME, 'group_footer').send_keys(group.gp_footer)
        wd.find_element(By.NAME, 'submit').click()

    def return_to_groups(self, wd):
        wd.find_element(By.LINK_TEXT, 'group page').click()

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, 'Logout').click()

    def test_add_group(self):
        success = True
        wd = self.wd
        self.open_home_page()
        sleep(5)
        self.login(wd, username="admin", passwd="secret")
      #  wd.find_element_by_xpath("//input[@value='Login']").click()
        self.open_group_list(wd)
        self.create_new_group(wd, Group(name="group1", header="group header 1", footer="group footer 1"))
        self.return_to_groups(wd)
        self.logout(wd)
        self.assertTrue(success)


    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    @property
    def is_alert_present(self):
        try:
            self.wd.switch_to.alert()
        except NoAlertPresentException:
            return False
        return True


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
