from components.settings import PreSettingsForm, SettingsForm
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
        signup_form.check_pre_settings_block()


class PresettingsPage(Page):
    PATH = '/presettings'

    def presettings(self, username):
        presettings_form = PreSettingsForm(self.driver)
        presettings_form.set_text(username, presettings_form.NAME)
        presettings_form.set_file(presettings_form.FILE_FACE, presettings_form.INPUT_AVATAR)
        presettings_form.set_select(presettings_form.SEX_FEMALE, presettings_form.SEX)
        presettings_form.submit()
