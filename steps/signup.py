from components.settings import SettingsForm
from components.signup_from import SignupForm
from steps.default import Page


class SignupPage(Page):
    PATH = '/signup'

    def signup(self, USEREMAIL, PASSWORD):
        signup_form = SignupForm(self.driver)
        settings_form = SettingsForm(self.driver)
        settings_form.set_text(USEREMAIL, settings_form.MAIL)
        settings_form.set_text(PASSWORD, settings_form.PASSWORD)
        settings_form.set_text(PASSWORD, settings_form.PASSWORD_REPEAT)
        signup_form.submit()
