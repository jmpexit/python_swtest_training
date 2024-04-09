# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
from time import sleep
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from model.contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
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


    def create_new_contact(self, wd, contact):
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.con_name)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.con_midname)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.con_surname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.con_nick)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.con_title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.con_co)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.con_addr)
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.con_hometel)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.con_mobtel)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.con_worktel)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(contact.con_fax)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.con_email)
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.con_bday)
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.con_bmonth)
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.con_byear)
        wd.find_element(By.NAME, "new_group").click()
        Select(wd.find_element(By.NAME, "new_group")).select_by_visible_text(contact.con_group)
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def return_to_home(self, wd):
        wd.find_element(By.LINK_TEXT, "home").click()

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()


    def test_add_contact(self):
        success = True
        wd = self.wd
        self.open_home_page()
        sleep(5)
        self.login(wd, username="admin", passwd="secret")
        self.create_new_contact(wd, Contact(name="Ju", midname="Pr", surname="Mi", nick="lucky",\
                                            title="ti1", co="very big co", addr="usa, CA, sm.st smth", hometel="111-11-11",\
                                            mobtel="1-111-111-1111", worktel="222-22-22", fax="222-22-22", email="em@ex.ca",\
                                            bday="2", bmonth="January", byear="1985", group="group1"))
        self.return_to_home(wd)
        self.logout(wd)
        self.assertTrue(success)


    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()