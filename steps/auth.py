from steps.default import Page
from components.auth_from import AuthForm


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    def auth(self, USEREMAIL, PASSWORD):
        auth_form = self.form
        auth_form.set_login(USEREMAIL)
        auth_form.set_password(PASSWORD)
        auth_form.submit()
