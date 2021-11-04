import os

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def click_by_id(self, id):
        self.driver.find_element_by_id(id).click()

    def click_by_class_name(self, class_name):
        self.driver.find_element_by_class_name(class_name).click()

    def click_by_xpath(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def submit(self):
        self.click_by_id(self.SUBMIT)

    def set_by_xpath(self, text, xpath):
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def set_by_id(self, text, id):
        self.driver.find_element_by_id(id).send_keys(text)

    def enter_by_id(self, id):
        self.driver.find_element_by_id(id).send_keys(Keys.ENTER)
        
    def clear_by_id(self, id):
        self.driver.find_element_by_id(id).clear()
        
    def text_by_id(self, id):
        self.driver.find_element_by_id(id).text

    def set_select_by_id(self, value, id):
        Select(self.driver.find_element_by_id(id)).select_by_value(value)

    def set_file(self, file, id):
        self.driver.find_element_by_id(id).send_keys(os.getcwd()+file)

    def check_class_in_element(self, element, class_name):
        return class_name in element.get_attribute('class').split()

    def check_non_valid_by_id(self, id):
        return self.check_class_in_element(self.driver.find_element_by_id(id), 'form-item_error')

    def check_block_by_class(self, class_name):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_class_name(class_name)
        )

    def check_block_by_id(self, id):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(id)
        )

    def check_page(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_class_name(self.PAGE_CLASS)
        )
