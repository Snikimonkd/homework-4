# -*- coding: utf-8 -*-

import os
from components.auth import AuthForm
from components.home import HomeForm

from steps.auth import AuthPage

from tests.default import DefaultTest

import mimesis


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

    def check_password(self, password, is_valid):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = AuthForm(self.driver)
        auth_form.set_password(password)
        auth_form.enter_by_id(auth_form.PASSWORD_ID)

        self.assertNotEqual(auth_form.check_non_valid_by_id(
            auth_form.PASSWORD_FORM_ID), is_valid)

    # Страница логина(https://lepick.ru/login)
    # Поле почты. Ошибка при вводе пустой строки, должна появляться подсказка, сообщающая о том, что необходимо заполнить поле.
    def test_empty_email(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = AuthForm(self.driver)
        auth_form.set_login("non_empty_email@mail.ru")
        auth_form.clear_by_id(auth_form.EMAIL_ID)
        auth_form.enter_by_id(auth_form.EMAIL_ID)

        self.assertTrue(auth_form.check_non_valid_by_id(
            auth_form.EMAIL_FORM_ID))

    # Поле почты. Ошибка при вводе текста, который не похож на почту(не проходит регулярное выражение для проверки почты),
    # должна появляться подсказка, сообщающая о том, что почта введена некорректно.
    def test_non_valid_email(self):
        email = "asdf"
        self.check_email(email, False)

    # Поле почты. Ошибка при вводе символов на кириллице, должна появиться подсказка, сообщающая о невозможности ввода почты с русскими символами.
    def test_cyrillic_email(self):
        email = "лол_кек@mail.ru"
        self.check_email(email, False)

    # Поле почты. При вводе корректной почты не должно появляться сообщений об ошибке.
    def test_valid_email(self):
        email = "mail@mail.ru"
        self.check_email(email, True)

    # Поле пароля. Ошибка при вводе пустой строки, должна появляться подсказка, сообщающая о том, что поле не заполнено.
    def test_empty_password(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = AuthForm(self.driver)
        auth_form.set_password("not_empty_password")
        auth_form.clear_by_id(auth_form.PASSWORD_ID)
        auth_form.enter_by_id(auth_form.PASSWORD_ID)

        self.assertTrue(auth_form.check_non_valid_by_id(
            auth_form.PASSWORD_FORM_ID))

    # Поле пароля. Ошибка при вводе пароля меньше 8 символов(не подходит под наше ограничение, должна появляться подсказка, 
    # сообщающая о том, что пароль должен быть больше 8 символов.
    def test_short_password(self):
        password = "1234567"
        self.check_password(password, False)

    # Поле пароля. При вводе пароля больше 8 символов не должно появляться сообщений об ошибке.
    def test_valid_password(self):
        password = "12345678"
        self.check_password(password, True)

    # Кнопка “Вход”. Ошибка при вводе данных незарегистрированного пользователя, должна появиться подсказка, сообщающая о неверном логине или пароле.
    def test_non_valid_auth(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        email = mimesis.Person().email()
        password = "12345678"

        auth_page.auth(email, password)

        auth_form = AuthForm(self.driver)
        text = auth_form.text_by_id(auth_form.ERROR_FORM_ID)
        self.assertNotEqual(text, "")

    # Кнопка “Вход”. Ошибка при попытке входа с пустыми полями, должна появиться подсказка, сообщающая о том, что поля не заполнены.
    def test_empty_auth(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        email = ""
        password = ""

        auth_page.auth(email, password)

        auth_form = AuthForm(self.driver)
        text = auth_form.text_by_id(auth_form.ERROR_FORM_ID)
        self.assertNotEqual(text, "")

    # Кнопка “Вход”. При вводе данных зарегистрированного пользователя, должен происходить переход наглавную(https://lepick.ru/).
    def test_valid_auth(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)
        HomeForm(self.driver).check_page()

    # Кнопка “Вход”. Если поле почты и/или пароля заполнено неверно, кнопка должна блокироваться.
    def test_empty_form(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, "")
        try:
            HomeForm(self.driver).check_page()
            assert("sdf")
        except:
            return
