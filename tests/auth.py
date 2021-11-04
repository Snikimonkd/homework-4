# -*- coding: utf-8 -*-

import os
from components.auth import AuthForm

from steps.auth import AuthPage

from tests.default import DefaultTest


class Auth(DefaultTest):
    USEREMAIL = 'wd055@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)


    # Страница логина(https://lepick.ru/login)
    # Поле почты. Ошибка при вводе пустой строки, должна появляться подсказка, сообщающая о том, что необходимо заполнить поле.
    def test_empte_email(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = AuthForm(self.driver)
        auth_form.set_login("")
        auth_form.enter_by_id(auth_form.EMAIL_ID)
        auth_form.check_valid_by_id(auth_form.EMAIL_FORM_ID)
