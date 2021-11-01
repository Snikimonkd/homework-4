from components.default import Component


class AuthForm(Component):
    LOGIN = '//*[@id="mail"]'
    PASSWORD = '//*[@id="password"]'
    SUBMIT = '//*[@id="login__form-submit"]'

    def set_login(self, login):
        self.set_by_xpath(login, self.LOGIN)

    def set_password(self, pwd):
        self.set_by_xpath(pwd, self.PASSWORD)
