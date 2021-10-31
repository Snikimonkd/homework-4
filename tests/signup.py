# -*- coding: utf-8 -*-

import os
from components.signup_from import SignupForm
from steps.auth import AuthPage

from steps.signup import PresettingsPage, SignupPage

from tests.default import DefaultTest
import mimesis

class Signup(DefaultTest):
    USEREMAIL = mimesis.Person().email()
    PASSWORD = os.environ['PASSWORD']
    signup_page = None

    def test(self):
        self.signup_page = SignupPage(self.driver)
        self.signup_page.open()

        self.signup_page.signup(self.USEREMAIL, self.PASSWORD)


class Presettings(Signup):
    USERENAME = 'Тестовое'

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.auth(self.USEREMAIL, self.PASSWORD)

        SignupForm(self.driver).check_pre_settings_block()

        presettings_page = PresettingsPage(self.driver)
        presettings_page.presettings(self.USERENAME)
