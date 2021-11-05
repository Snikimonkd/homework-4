from components.default import Component


class SettingsForm(Component):
    PAGE_CLASS = 'settings'

    PHOTO_ID = 'settings__new-photo'

    MAIL = 'email'
    NAME = 'name'
    PASSWORD = 'password'
    PASSWORD_REPEAT = 'password_repeat'

    SELECT_FORM_ID = 'signup_birthday_from-item'

    SELECT_MONTH = 'js__date-input__month'
    SELECT_DAY = 'js__date-input__day'
    SELECT_YEAR = 'js__date-input__year'

    SUBMIT = 'settings__submit'
    SEX = 'settings_sex'
    DATE_PREFERENCE = 'settings__datePreference'
    SEX_MALE = '0'
    SEX_FEMALE = '1'
    SEX_BOTH = '2'

    INPUT_AVATAR = 'input_avatar'
    FILE_FACE = '/img/face.png'
    FILE_NOT_FACE = '/img/not_face.png'
    FILE_NOT_FORMAT = '/img/not_format.webp'
    FILE_LARGE = '/img/large_image.png'

    def set_text(self, text, field):
        self.set_by_id(text, field)

    def set_select(self, value, field):
        self.set_select_by_id(value, field)

    def check_non_valid(self, id):
        return self.check_non_valid_by_id(id+'_form-item')


class PreSettingsForm(SettingsForm):
    PAGE_CLASS = 'pre-settings'

    MAIL = 'mail'
    ERROR_FORM_ID = "signup-error" 

    def set_login(self, login):
        self.set_by_id(login, self.MAIL)

    def set_password(self, pwd):
        self.set_by_id(pwd, self.PASSWORD)

    def set_password_repeat(self, pwd):
        self.set_by_id(pwd, self.PASSWORD_REPEAT)
