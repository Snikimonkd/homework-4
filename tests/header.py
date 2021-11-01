from components.header import HeaderForm
from components.message import MessageForm
from tests.auth_default import AuthDefaultTest


class Header(AuthDefaultTest):

    # 1.8. При нажатии на кнопку сообщения происходит переход на страницу сообщений
    def test_message_button(self):
        header_form = HeaderForm(self.driver)
        print('!!!!!!!!!!!!!!!!!!!!')
        print('!!!!!!!!!!!!!!!!!!!!')
        print('!!!!!!!!!!!!!!!!!!!!')
        print('!!!!!!!!!!!!!!!!!!!!')
        print(header_form.check_icon_active(header_form.MESSAGES_ID))
        header_form.click_by_id(header_form.MESSAGES_ID)
        MessageForm(self.driver).check_page()
        print(header_form.check_icon_active(header_form.MESSAGES_ID))

