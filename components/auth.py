from components.default import Component


class AuthForm(Component):
    PAGE_CLASS = 'wrapper-login'
    
    EMAIL_ID = 'mail'
    EMAIL_FORM_ID = 'login_mail_form-item'
    PASSWORD_ID = 'password'
    SUBMIT_ID = 'login__form-submit'

    def set_login(self, login):
        self.set_by_id(login, self.EMAIL_ID)

    def set_password(self, pwd):
        self.set_by_id(pwd, self.PASSWORD_ID)
