from components.header import HeaderForm

from tests.default import DefaultTest


class Header(DefaultTest):

    # 1.3. При нажатии на бургер открывается меню
    def test_burger(self):
        header_form = HeaderForm(self.driver)
        close = header_form.check_header_close()
        header_form.click_by_id(header_form.BURGER_ID)
        self.assertEqual(close, header_form.check_header_close())
        self.assertNotEqual(close, header_form.check_header_close())
