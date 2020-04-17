from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
        self.vars = {}

    def open_home_page(self):
        self.driver.get("http://addressbook/")
        self.driver.set_window_size(820, 647)

    def login(self, username, password):
        self.open_home_page()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_group_page(self):
        self.driver.find_element(By.LINK_TEXT, "Группы").click()

    def init_group_form(self):
        self.open_group_page()
        self.driver.find_element(By.NAME, "new").click()

    def fill_group_form(self, group):
        self.init_group_form()
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        self.submit_group_creation()

    def submit_group_creation(self):
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Выйти").click()

    def destroy(self):
        self.driver.quit()