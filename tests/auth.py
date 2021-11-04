# -*- coding: utf-8 -*-

import os
from components.auth import AuthForm

from steps.auth import AuthPage

from tests.default import DefaultTest


class Auth(DefaultTest):
    USEREMAIL = 'wd055@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    def check_email(self, useremail, is_valid):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = AuthForm(self.driver)
        auth_form.set_login(useremail)
        auth_form.enter_by_id(auth_form.EMAIL_ID)

        self.assertNotEqual(auth_form.check_non_valid_by_id(
            auth_form.EMAIL_FORM_ID), is_valid)

    # def test(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()

    #     auth_page.auth(self.USEREMAIL, self.PASSWORD)

    # # Страница логина(https://lepick.ru/login)
    # # Поле почты. Ошибка при вводе пустой строки, должна появляться подсказка, сообщающая о том, что необходимо заполнить поле.
    # def test_empty_email(self):
    #     email = ""
    #     self.check_email(email)

    # Поле почты. Ошибка при вводе текста, который не похож на почту(не проходит регулярное выражение для проверки почты),
    # должна появляться подсказка, сообщающая о том, что почта введена некорректно.
    def test_non_valid_email(self):
        email = "asdf"
        self.check_email(email, False)

    # Поле почты. Ошибка при вводе символов на кириллице, должна появиться подсказка, сообщающая о невозможности ввода почты с русскими символами.

    # Поле почты. При вводе корректной почты не должно появляться сообщений об ошибке.
    def test_valid_email(self):
        email = "mail@mail.ru"
        self.check_email(email, True)
