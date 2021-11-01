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
    USERENAME = 'Тестовое'

    def test_signup(self):
        useremail = mimesis.Person().email()
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_page.signup(useremail, self.PASSWORD)

    def test_signup_full(self):
        self.test_signup()

        SignupForm(self.driver).check_pre_settings_block()

        presettings_page = PresettingsPage(self.driver)
        presettings_page.presettings(self.USERENAME)

    # def test_presettings(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #     auth_page.auth(self.USEREMAIL, self.PASSWORD)

    #     SignupForm(self.driver).check_pre_settings_block()

    #     presettings_page = PresettingsPage(self.driver)
    #     presettings_page.presettings(self.USERENAME)
