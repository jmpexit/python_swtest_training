from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, passwd):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, 'user').click()
        wd.find_element(By.NAME, 'user').clear()
        wd.find_element(By.NAME, 'user').send_keys(username)
        wd.find_element(By.NAME, 'pass').click()
        wd.find_element(By.NAME, 'pass').clear()
        wd.find_element(By.NAME, 'pass').send_keys(passwd)
        wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, 'Logout').click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, 'Logout')) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div/div[1]/form/b").text == "("+username+")"

    def ensure_login(self, username, passwd):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, passwd)

