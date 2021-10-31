from components.settings import SettingsForm
from components.signup_from import SignupForm
from steps.default import Page


class SignupPage(Page):
    PATH = '/signup'

    def signup(self, useremail, password):
        signup_form = SignupForm(self.driver)
        settings_form = SettingsForm(self.driver)
        settings_form.set_text(useremail, settings_form.MAIL)
        settings_form.set_text(password, settings_form.PASSWORD)
        settings_form.set_text(password, settings_form.PASSWORD_REPEAT)
        signup_form.submit()


class PresettingsPage(Page):
    PATH = '/presettings'

    def presettings(self, username):
        settings_form = SettingsForm(self.driver)
        settings_form.set_text(username, settings_form.NAME)
        settings_form.submit()
