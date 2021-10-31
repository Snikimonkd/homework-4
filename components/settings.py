from components.default import Component
from selenium.webdriver.common.keys import Keys


class SettingsForm(Component):
    MAIL = '//*[@id="mail"]'
    PASSWORD = '//*[@id="password"]'
    PASSWORD_REPEAT = '//*[@id="password_repeat"]'
    SELECT_MONTH = '//*[@class="js__date-input__month"]'
    SELECT_DAY = '//*[@class="js__date-input__day"]'
    SELECT_YEAR = '//*[@class="js__date-input__year"]'

    def set_text(self, text, field):
        self.driver.find_element_by_xpath(field).send_keys(text)

