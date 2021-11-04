from steps.default import Page
from components.auth import AuthForm


class AuthPage(Page):
    PATH = ''

    def auth(self, USEREMAIL, PASSWORD):
        auth_form = AuthForm(self.driver)
        auth_form.set_login(USEREMAIL)
        auth_form.set_password(PASSWORD)
        auth_form.submit()
