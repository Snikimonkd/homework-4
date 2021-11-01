import os

import mimesis
from components.home import HomeForm
from steps.signup import SignupPage

from tests.default import DefaultTest


class AuthDefaultTest(DefaultTest):
    USEREMAIL = mimesis.Person().email()
    PASSWORD = os.environ['PASSWORD']
    USERENAME = 'Тестовое'

    def setUp(self):
        super().setUp()
        signup_page = SignupPage(self.driver)
        signup_page.open()
        signup_page.full(self.USERENAME, self.USEREMAIL, self.PASSWORD)

        HomeForm(self.driver).check_page()
