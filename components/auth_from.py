from time import sleep
from components.default import Component
from selenium.webdriver.common.keys import Keys


class AuthForm(Component):
    LOGIN = '//*[@id="mail"]'
    PASSWORD = '//*[@id="password"]'
    SUBMIT = '//*[@id="login__form-submit"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(Keys.ENTER)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(Keys.ENTER)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
