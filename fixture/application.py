from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self): #конструктор класса
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self) #помощник получает ссылку на объект класса App.
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
 #       wd.implicitly_wait(20)


    def return_to_home(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def destroy(self):
        self.wd.quit()
