from components.default import Component
from selenium.webdriver.support.ui import WebDriverWait


class SignupForm(Component):
    SUBMIT = '//*[@id="signup__form-submit"]'
    SIGNUP_BLOCK = '//*[@class="signup-block"]'
    SIGNUP_BLOCK_CLASS_NAME = "signup-block"
    PRE_SETTINGS_BLOCK = '//*[@class="pre-settings"]'
    PRE_SETTINGS_BLOCK_CLASS_NAME = "pre-settings"

    def check_signup_block(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_class_name(self.SIGNUP_BLOCK_CLASS_NAME)
        )

    def check_pre_settings_block(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_class_name(self.PRE_SETTINGS_BLOCK_CLASS_NAME)
        )
