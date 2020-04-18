from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "Группы").click()

    def init_group_form(self):
        self.open_group_page()
        self.app.driver.find_element(By.NAME, "new").click()

    def create(self, group):
        self.init_group_form()
        self.app.driver.find_element(By.NAME, "group_name").click()
        self.app.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.app.driver.find_element(By.NAME, "group_header").click()
        self.app.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.app.driver.find_element(By.NAME, "group_footer").click()
        self.app.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        self.submit_group_creation()

    def submit_group_creation(self):
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "group page").click()