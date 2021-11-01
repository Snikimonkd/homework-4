import os

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def set_by_xpath(self, text, xpath):
        self.driver.find_element_by_xpath(xpath).send_keys(text)
        self.driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)

    def set_by_id(self, text, id):
        self.driver.find_element_by_id(id).send_keys(text)
        self.driver.find_element_by_id(id).send_keys(Keys.ENTER)

    def set_select_by_id(self, value, id):
        Select(self.driver.find_element_by_id(id)).select_by_value(value)

    def set_file(self, file, id):
        self.driver.find_element_by_id(id).send_keys(os.getcwd()+file)

    def check_valid_by_id(self, id):
        return 'form-item_error' in self.driver.find_element_by_id(id).get_attribute('class').split()
