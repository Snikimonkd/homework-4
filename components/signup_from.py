from components.default import Component
from selenium.webdriver.support.ui import WebDriverWait


class SignupForm(Component):
    SUBMIT = '//*[@id="signup__form-submit"]'
    SIGNUP_BLOCK = '//*[@class="signup-block"]'
    PRE_SETTINGS_BLOCK = '//*[@class="pre-settings"]'

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def check_signup_block(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE).text
        )

    def check_pre_settings_block(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE).text
        )