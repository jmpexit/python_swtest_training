from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_list(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, 'groups').click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_list()
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
        self.return_to_groups()

    def return_to_groups(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, 'group page').click()
