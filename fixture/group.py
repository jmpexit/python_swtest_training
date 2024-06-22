from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_list(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and (len(wd.find_elements(By.NAME, 'new')) > 0)):
            wd.find_element(By.LINK_TEXT, 'groups').click()
        #or if true - return

    def create(self, group):
        wd = self.app.wd
        self.open_group_list()
        wd.find_element(By.NAME, 'new').click()
        self.fill_in_group_form(group)
        #submit creation
        wd.find_element(By.NAME, 'submit').click()
        self.return_to_groups()

    def fill_in_group_form(self, group):
        wd = self.app.wd
        self.enter_field_values('group_name', group.gp_name)
        self.enter_field_values('group_header', group.gp_header)
        self.enter_field_values('group_footer', group.gp_footer)

    def enter_field_values(self, field_name, entry):
        wd = self.app.wd
        if entry is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(entry)

    def return_to_groups(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, 'group page').click()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_list()
        wd.find_element(By.NAME, 'selected[]').click()
        wd.find_element(By.NAME, 'delete').click()
        self.return_to_groups()

    def update_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_list()
        self.select_first_group()
        #open modification form
        wd.find_element(By.NAME, 'edit').click()
        self.fill_in_group_form(new_group_data)
        #submit update
        wd.find_element(By.NAME, 'update').click()
        self.return_to_groups()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, 'selected[]').click()

    def delete(self, group):
        wd = self.app.wd
        self.open_group_list()
        self.select_first_group()
        #wd.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='group1'])[2]/input[1]").click()
        #submit deletion
        wd.find_element(By.NAME, 'delete').click()
        self.return_to_groups()

    def count(self):
        wd = self.app.wd
        self.open_group_list()
        return len(wd.find_elements(By.NAME, 'selected[]'))



