from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


class Application:

    def __init__(self): #конструктор класса
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.implicitly_wait(20)

    def login(self, username, passwd):
        wd = self.wd
        self.open_home_page()
        wd.find_element(By.NAME, 'user').click()
        wd.find_element(By.NAME, 'user').clear()
        wd.find_element(By.NAME, 'user').send_keys(username)
        wd.find_element(By.NAME, 'pass').click()
        wd.find_element(By.NAME, 'pass').clear()
        wd.find_element(By.NAME, 'pass').send_keys(passwd)
        wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()

    def open_group_list(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, 'groups').click()

    def create_new_group(self, group):
        wd = self.wd
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
        wd = self.wd
        wd.find_element(By.LINK_TEXT, 'group page').click()

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, 'Logout').click()


    def create_new_contact(self, contact):
        wd = self.wd
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
        self.return_to_home()

    def return_to_home(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def destroy(self):
        self.wd.quit()
