# -*- coding: utf-8 -*-

import os

from steps.auth import AuthPage

from tests.default import DefaultTest


class AuthTest(DefaultTest):
    USEREMAIL = 'wd055@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    def auth(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)
