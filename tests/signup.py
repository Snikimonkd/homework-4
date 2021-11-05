# -*- coding: utf-8 -*-

import os
from components.home import HomeForm
from components.settings import PreSettingsForm

from steps.signup import PresettingsPage, SignupPage

from components.signup_form import SignupForm
from steps.auth import AuthPage

from tests.default import DefaultTest
import mimesis
from datetime import datetime
import time


class Signup(DefaultTest):
    USEREMAIL = "siniy_kit@mail.ru"
    PASSWORD = os.environ['PASSWORD']
    USERENAME = 'Тестовое'

    def check_email(self, useremail, is_valid):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = SignupForm(self.driver)
        pre_settings_form.set_text(useremail, pre_settings_form.MAIL)
        pre_settings_form.enter_by_id(pre_settings_form.MAIL)

        self.assertNotEqual(pre_settings_form.check_non_valid(
            pre_settings_form.MAIL), is_valid)

    def check_password(self, password, is_valid):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = SignupForm(self.driver)
        pre_settings_form.set_text(password, pre_settings_form.PASSWORD)
        pre_settings_form.enter_by_id(pre_settings_form.MAIL)

        self.assertNotEqual(pre_settings_form.check_non_valid(
            pre_settings_form.PASSWORD), is_valid)

    # Страница регистрации(https://lepick.ru/signup).
    # Поле почты. Ошибка при вводе пустой строки, должна появляться подсказка, сообщающая о том, что необходимо заполнить поле.
    def test_empty_email(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = SignupForm(self.driver)
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

        pre_settings_form = SignupForm(self.driver)
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

        pre_settings_form = SignupForm(self.driver)
        pre_settings_form.set_password("12345678")
        pre_settings_form.set_password_repeat("123456789")
        pre_settings_form.enter_by_id(pre_settings_form.PASSWORD_REPEAT)

        self.assertTrue(pre_settings_form.check_non_valid(
            pre_settings_form.PASSWORD_REPEAT))

    # Поле повторного пароля. При вводе повторного пароля, совпадающего с первым, не должна появляться подсказка, сообщающая о том, что пароли не совпадают.
    def test_valid_second_password(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = SignupForm(self.driver)
        pre_settings_form.set_password("12345678")
        pre_settings_form.set_password_repeat("12345678")
        pre_settings_form.enter_by_id(pre_settings_form.PASSWORD_REPEAT)

        self.assertFalse(pre_settings_form.check_non_valid(
            pre_settings_form.PASSWORD_REPEAT))

    # Поле возраста. Ошибка при попытке регистрации с возрастом менее 18 лет, должна появиться подсказка, сообщающая о том, что нельзя зарегистрироваться.
    def test_age_less_than_18(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = SignupForm(self.driver)
        d = datetime.now()

        pre_settings_form.set_select_by_class_name(
            str(d.month-1), pre_settings_form.SELECT_MONTH)
        pre_settings_form.set_select_by_class_name(
            str(d.day), pre_settings_form.SELECT_DAY)

        self.assertTrue(pre_settings_form.check_non_valid_by_id(
            pre_settings_form.SELECT_FORM_ID))

    # Поле возраста. Ошибка при попытке поставить несуществующее число(31 февраля), должна появляться ошибка.
    # С этим связан баг, который не пофикшен на фронте

    # Поле возраста. Если ввести возраст больше 18 лет и существующую дату, не должно появляться сообщений об ошибке.
    def test_age_more_than_18(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = SignupForm(self.driver)

        d = datetime.now()
        pre_settings_form.set_select_by_class_name(
            str(d.month-1), pre_settings_form.SELECT_MONTH)
        pre_settings_form.set_select_by_class_name(
            str(d.day-1), pre_settings_form.SELECT_DAY)

        self.assertFalse(pre_settings_form.check_non_valid_by_id(
            pre_settings_form.SELECT_FORM_ID))

    # Кнопка “Зарегистрироваться”. Ошибка при вводе почты уже зарегистрированного пользователя и нажатие на кнопку, должна появляться подсказка, сообщающая о том, что почта уже занята.
    def test_already_signup(self):
        useremail = "mail@mail.ru"
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = SignupForm(self.driver)

        signup_page.signup(useremail, self.PASSWORD)

        text = pre_settings_form.text_by_id(pre_settings_form.ERROR_FORM_ID)
        self.assertNotEqual(text, "")

    # Кнопка “Зарегистрироваться”. Ошибка при вводе пустых строк во все поля и нажатие на кнопку, должна появляться подсказка, сообщающая о том, что необходимо заполнить поля.
    def test_already_signup(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = SignupForm(self.driver)

        signup_page.signup("", "")

        self.assertEqual(
            (pre_settings_form.check_non_valid(pre_settings_form.PASSWORD),
             pre_settings_form.check_non_valid(pre_settings_form.MAIL)),
            (True, True))

    # Кнопка “Зарегистрироваться”. Ошибка при вводе неправильных данных(пароль непроходящий валидацию или возраст меньше 18 лет) кнопка должна блокироваться.
    def test_non_valid_pass_submit(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_page.signup(self.USEREMAIL, "1234567")
        try:
            HomeForm(self.driver).check_page()
            assert("")
        except:
            return

    def test_non_valid_age_submit(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        pre_settings_form = SignupForm(self.driver)
        d = datetime.now()

        pre_settings_form.set_select_by_class_name(
            str(d.month-1), pre_settings_form.SELECT_MONTH)
        pre_settings_form.set_select_by_class_name(
            str(d.day), pre_settings_form.SELECT_DAY)

        signup_page.signup(self.USEREMAIL, "12345678")
        try:
            PreSettingsForm(self.driver).check_page()
            assert("")
        except:
            return

    # Кнопка “Зарегистрироваться”. При вводе всех данных незарегистрированного пользователя и нажатие на кнопку, должен происходить переход на второй этап регистрации(https://lepick.ru/presettings).
    def test_signup(self):
        useremail = mimesis.Person().email()
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_page.signup(useremail, self.PASSWORD)
        SignupForm(self.driver).check_page()

    # Второй этап регистрации (https://lepick.ru/presettings)
    # Поле имени. Ошибка при вводе небуквенных символов, должна появляться подсказка, сообщающая о том, что нельзя вводить имя, содержащее небуквенные символы.
    def test_forbidden_symbols(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)
        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.check_page()

        pre_settings_form.set_text("%", pre_settings_form.NAME)
        pre_settings_form.enter_by_id(pre_settings_form.NAME)

        self.assertTrue(pre_settings_form.check_non_valid(
            pre_settings_form.NAME))

    # Поле имени. Ошибка при вводе имени длиннее 50 символов.
    def test_len_50_name(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)
        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.check_page()

        long_name = "asdfsadlfkjhasdlfkhjasdflkjhasdflkjhasdfasdfasdfasdfasdf"

        pre_settings_form.set_text(
            long_name, pre_settings_form.NAME)
        pre_settings_form.enter_by_id(pre_settings_form.NAME)

        text = pre_settings_form.text_by_id(pre_settings_form.NAME)

        # В поле имени не дает ввести больше 50 символов, никаких сообщений об ошибке не показывается
        self.assertNotEqual(text, long_name)

    # Поле имени. Ошибка при введении пустой строки.
    def test_empty_name(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.check_page()

        pre_settings_form.set_text("Keklol", pre_settings_form.NAME)
        pre_settings_form.clear_by_id(pre_settings_form.NAME)
        pre_settings_form.enter_by_id(pre_settings_form.NAME)

        self.assertTrue(pre_settings_form.check_non_valid(
            pre_settings_form.NAME))

    # Поле имени. Если ввести имя состоящее только из букв и короче 50 символов - не должно появляться сообщений об ошибке.
    def test_valid_name(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)

        PreSettingsForm(self.driver).check_page()

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.set_text("Kek", pre_settings_form.NAME)
        pre_settings_form.enter_by_id(pre_settings_form.NAME)

        self.assertFalse(pre_settings_form.check_non_valid(
            pre_settings_form.NAME))

    # Поле пола партнера. При выборе пола партнера, можно выбрать любой пол, даже тот, что и у самого пользователя.
    def test_preferences(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.check_page()

        res = []
        for i in range(3):
            pre_settings_form.set_select_by_id(
                str(i), pre_settings_form.DATE_PREFERENCE)
            pre_settings_form.enter_by_id(pre_settings_form.DATE_PREFERENCE)
            res.append(pre_settings_form.check_non_valid(
                pre_settings_form.NAME))

        self.assertEqual(res, [False, False, False])

    # Загрузка аватарки. Ошибка при попытке загрузки фотографии неподходящего типа(не png, jpeg или jpg), в проводнике не отображаются неподходящие картинки.
    def test_non_valid_photo_type(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.check_page()

        pre_settings_form.set_text("Kek", pre_settings_form.NAME)
        pre_settings_form.set_file(
            pre_settings_form.FILE_NOT_FORMAT, pre_settings_form.INPUT_AVATAR)
        pre_settings_form.submit()
        try:
            HomeForm(self.driver).check_page()
            assert("")
        except:
            return

    # Загрузка аватарки. Ошибка при попытке загрузки фотографии больше 10 МБ, аватарка не загружается, и появляется подсказка, сообщающая о том что аватарка слишком большая.
    def test_non_valid_photo_type(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.check_page()

        pre_settings_form.set_text("Kek", pre_settings_form.NAME)
        pre_settings_form.set_file(
            pre_settings_form.FILE_LARGE, pre_settings_form.INPUT_AVATAR)
        pre_settings_form.check_block_by_class('snackbar')

    # Загрузка аватарки. При загрузке фотографии подходящего размера и типа, она появляется на экране в отведенном для нее окошке.
    def test_valid_photo_type(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.check_page()

        src_before = pre_settings_form.driver.find_element_by_id(
            pre_settings_form.PHOTO_ID).get_attribute('src')
        pre_settings_form.set_text("Kek", pre_settings_form.NAME)
        pre_settings_form.set_file(
            pre_settings_form.FILE_FACE, pre_settings_form.INPUT_AVATAR)
        # ждем пока фотка загрузится
        time.sleep(1)
        src_after = pre_settings_form.driver.find_element_by_id(
            pre_settings_form.PHOTO_ID).get_attribute('src')
        self.assertNotEqual(src_before, src_after)

    # Кнопка “Сохранить”. Если одно из полей не заполнено и/или заполнено неверно, кнопка блокируется.
    def test_forbidden_symbols_submit(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)
        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.check_page()

        pre_settings_form.set_text("%", pre_settings_form.NAME)
        pre_settings_form.enter_by_id(pre_settings_form.NAME)

        pre_settings_form.submit()
        try:
            HomeForm(self.driver).check_page()
            assert("")
        except:
            return

    # Кнопка “Сохранить”. Если загрузить фотку без лица и нажать на кнопку, должна появиться подсказка, сообщающая о том, что на фотографии нет лица.
    def test_forbidden_symbols_submit(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.auth(self.USEREMAIL, self.PASSWORD)

        pre_settings_form = PreSettingsForm(self.driver)
        pre_settings_form.check_page()

        pre_settings_form.set_text("Kek", pre_settings_form.NAME)
        pre_settings_form.set_file(
            pre_settings_form.FILE_NOT_FACE, pre_settings_form.INPUT_AVATAR)
        pre_settings_form.submit()
        pre_settings_form.check_block_by_class('snackbar')

    # Кнопка “Сохранить”. Если все данные введены верно, то при нажатии на кнопку должен происходить переход в ленту(https://lepick.ru/).
    def test_signup_full(self):
        self.test_signup()

        PreSettingsForm(self.driver).check_page()

        presettings_page = PresettingsPage(self.driver)
        presettings_page.presettings(self.USERENAME)

        HomeForm(self.driver).check_page
