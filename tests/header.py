from components.header import HeaderForm
from components.home import HomeForm
from components.message import MessageForm
from components.settings import SettingsForm
from tests.auth_default import AuthDefaultTest


class Header(AuthDefaultTest):

    # 1.8. При нажатии на кнопку сообщения происходит переход на страницу сообщений
    # 1.9. При активной странице сообщения кнопка должна быть серой и не кликабельной, иначе насыщенной и кликабельной
    def test_message_button(self):
        header_form = HeaderForm(self.driver)
        active = header_form.check_icon_active(header_form.MESSAGES_ID)
        header_form.click_by_id(header_form.MESSAGES_HREF_ID)
        MessageForm(self.driver).check_page()
        self.assertNotEqual(
            active, header_form.check_icon_active(header_form.MESSAGES_ID))

    # 1.6. При нажатии на кнопку главного экрана происходит переход на главную страницу
    # 1.7. При активной главное странице кнопка должна быть серой и не кликабельной, иначе насыщенной и кликабельной
    def test_home_button(self):
        header_form = HeaderForm(self.driver)
        header_form.click_by_id(header_form.MESSAGES_HREF_ID)

        active = header_form.check_icon_active(header_form.HOME_ID)
        header_form.click_by_id(header_form.HOME_HREF_ID)
        HomeForm(self.driver).check_page()
        self.assertNotEqual(
            active, header_form.check_icon_active(header_form.HOME_ID))

            
    # 1.10. При нажатии на кнопку настроен происходит переход на страницу настроек
    # 1.11. При активной странице настроек кнопка должна быть серой и не кликабельной, иначе насыщенной и кликабельной
    def test_settings_button(self):
        header_form = HeaderForm(self.driver)
        active = header_form.check_icon_active(header_form.SETTINGS_ID)
        header_form.click_by_id(header_form.SETTINGS_HREF_ID)
        SettingsForm(self.driver).check_page()
        self.assertNotEqual(
            active, header_form.check_icon_active(header_form.SETTINGS_ID))
