# -*- coding: utf-8 -*-

import os

from steps.auth import AuthPage
from steps.signup import SignupPage

from tests.default import DefaultTest


class SignupTest(DefaultTest):
    USEREMAIL = 'wd055@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    def signup(self):
        auth_page = SignupPage(self.driver)
        auth_page.open()

        auth_page.signup(self.USEREMAIL, self.PASSWORD)

    def presettings(self):
        auth_page = SignupPage(self.driver)
        auth_page.open()

        auth_page.signup(self.USEREMAIL, self.PASSWORD)
