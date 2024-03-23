# -*- coding: utf-8 -*-
import unittest
from time import sleep
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from group import Group
from application import Application


def is_alert_present(wd):
    try:
        wd.switch_to.alert().text
        return True
    except:
        return False


class TestAddGroup(unittest.TestCase):
    def setUp(self): # self представляет экземпляр классса
        self.app = Application() # метод setUp инициализирует фикстуру

    def test_add_group(self):
        self.app.login(username="admin", passwd="secret")
        self.app.create_new_group(Group(name="group1", header="group header 1", footer="group footer 1"))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
