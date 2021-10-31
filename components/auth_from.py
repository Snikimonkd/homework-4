from components.default import Component


class AuthForm(Component):
    LOGIN = '//*[@id="mail"]'
    PASSWORD = '//*[@id="password"]'
    SUBMIT = '//*[@id="login__form-submit"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
