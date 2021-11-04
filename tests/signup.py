# -*- coding: utf-8 -*-

import os
from components.home import HomeForm
from components.settings import PreSettingsForm

from steps.signup import PresettingsPage, SignupPage

from tests.default import DefaultTest
import mimesis
import time


class Signup(DefaultTest):
    USEREMAIL = mimesis.Person().email()
    PASSWORD = os.environ['PASSWORD']
    USERENAME = 'Тестовое'

    def check_email(self, useremail, is_valid):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.set_text(useremail, pre_settings_form.MAIL)
        pre_settings_form.enter_by_id(pre_settings_form.MAIL)

        self.assertNotEqual(pre_settings_form.check_non_valid(
            pre_settings_form.MAIL), is_valid)

    def check_password(self, password, is_valid):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.set_text(password, pre_settings_form.PASSWORD)
        pre_settings_form.enter_by_id(pre_settings_form.MAIL)

        self.assertNotEqual(pre_settings_form.check_non_valid(
            pre_settings_form.PASSWORD), is_valid)

    # def test_signup(self):
    #     useremail = mimesis.Person().email()
    #     signup_page = SignupPage(self.driver)
    #     signup_page.open()

    #     signup_page.signup(useremail, self.PASSWORD)
    #     PreSettingsForm(self.driver).check_page()

    # def test_signup_full(self):
    #     self.test_signup()

    #     PreSettingsForm(self.driver).check_page()

    #     presettings_page = PresettingsPage(self.driver)
    #     presettings_page.presettings(self.USERENAME)

    #     HomeForm(self.driver).check_page()

    # Страница регистрации(https://lepick.ru/signup).
    # Поле почты. Ошибка при вводе пустой строки, должна появляться подсказка, сообщающая о том, что необходимо заполнить поле.
    def test_empty_email(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.set_login("non_empty_email@mail.ru")
        pre_settings_form.clear_by_id(pre_settings_form.MAIL)
        pre_settings_form.enter_by_id(pre_settings_form.MAIL)

        self.assertTrue(pre_settings_form.check_non_valid(
            pre_settings_form.MAIL))

    # Поле почты. Ошибка при вводе текста, который не похож на почту(не проходит регулярное выражение для проверки почты), должна появляться подсказка, сообщающая о том, что почта введена некорректно.
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

    # Поле пароля. Ошибка при вводе пустой строки должна, появляться подсказка, сообщающая о том, что поле не заполнено.
    def test_empty_password(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.set_password("not_empty_password")
        pre_settings_form.clear_by_id(pre_settings_form.PASSWORD)
        pre_settings_form.enter_by_id(pre_settings_form.PASSWORD)

        self.assertTrue(pre_settings_form.check_non_valid(
            pre_settings_form.PASSWORD))

    # Поле пароля. Ошибка при вводе пароля меньше 8 символов(не подходит под наше ограничение, должна появляться подсказка, сообщающая о том, что пароль должен быть больше 8 символов.
    def test_non_valid_password(self):
        password = "1234567"
        self.check_password(password, False)

    # Поле пароля. При вводе пароля больше 8 символов не должно появляться сообщений об ошибке.
    def test_valid_password(self):
        password = "12345678"
        self.check_password(password, True)

    # Поле повторного пароля. Ошибка. При вводе повторного пароля, не совпадающего с первым, должна появляться подсказка, сообщающая о том, что пароли не совпадают.
    def test_non_valid_second_password(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.set_password("12345678")
        pre_settings_form.set_password_repeat("123456789")
        pre_settings_form.enter_by_id(pre_settings_form.PASSWORD_REPEAT)

        self.assertTrue(pre_settings_form.check_non_valid(
            pre_settings_form.PASSWORD_REPEAT))

    # Поле повторного пароля. При вводе повторного пароля, совпадающего с первым, не должна появляться подсказка, сообщающая о том, что пароли не совпадают.
    def test_valid_second_password(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.set_password("12345678")
        pre_settings_form.set_password_repeat("12345678")
        pre_settings_form.enter_by_id(pre_settings_form.PASSWORD_REPEAT)

        self.assertFalse(pre_settings_form.check_non_valid(
            pre_settings_form.PASSWORD_REPEAT))
