# -*- coding: utf-8 -*-

import os

from steps.auth import AuthPage
from steps.signup import PresettingsPage, SignupPage

from tests.default import DefaultTest


class Signup(DefaultTest):
    USEREMAIL = 'wd055@mail.ru'
    PASSWORD = os.environ['PASSWORD']
    signup_page = None

    def test(self):
        self.signup_page = SignupPage(self.driver)
        self.signup_page.open()

        self.signup_page.signup(self.USEREMAIL, self.PASSWORD)


class Presettings(Signup):
    USERENAME = 'Тестовое'

    def test(self):
        presettings_page = PresettingsPage(self.driver)
        presettings_page.open()

        presettings_page.presettings(self.USERENAME)
