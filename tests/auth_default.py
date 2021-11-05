import os

import mimesis
from components.home import HomeForm
from steps.auth import AuthPage
from steps.signup import SignupPage

from tests.default import DefaultTest


class AuthDefaultTest(DefaultTest):
    USEREMAIL = 'wd055@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        super().setUp()

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)

        HomeForm(self.driver).check_page()


class SignupDefaultTest(DefaultTest):
    PASSWORD = os.environ['PASSWORD']
    USERENAME = 'Тестовое'

    def setUp(self):
        super().setUp()
        signup_page = SignupPage(self.driver)
        signup_page.open()
        signup_page.full(
            self.USERENAME, mimesis.Person().email(), self.PASSWORD)

        HomeForm(self.driver).check_page()
