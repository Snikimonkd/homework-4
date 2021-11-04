from components.card import CardForm

from tests.auth_default import SignupDefaultTest


class Header(SignupDefaultTest):

    #  2.1. При нажатии на кнопку лайк при доступном лимите происходит свайп карточку
    def test_like(self):
        card_form = CardForm(self.driver)
        card_form.click_by_id(card_form.LIKE_ID)
        card_form.check_block_by_class(card_form.CARD_SWIPE_RIGHT_CLASS)

    #  2.3. При нажатии на кнопку дизлайк происходит свайп карточку
    def test_dislike(self):
        card_form = CardForm(self.driver)
        card_form.click_by_id(card_form.DISLIKE_ID)
        card_form.check_block_by_class(card_form.CARD_SWIPE_LEFT_CLASS)

    #  2.2. При нажатии на кнопку лайк при превышении лимита отображается сообщение об ошибке
    def test_limit(self):
        card_form = CardForm(self.driver)
        for i in range(21):
            card_form.check_block_by_id(card_form.DISLIKE_ID)
            card_form.click_by_id(card_form.DISLIKE_ID)
        card_form.check_block_by_class('snackbar')
