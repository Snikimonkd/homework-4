from components.default import Component


class SignupForm(Component):
    PAGE_CLASS = 'signup-block'
    
    SUBMIT = 'signup__form-submit'
    SIGNUP_BLOCK = '//*[@class="signup-block"]'
    SIGNUP_BLOCK_CLASS_NAME = "signup-block"
    PRE_SETTINGS_BLOCK = '//*[@class="pre-settings"]'
    PRE_SETTINGS_BLOCK_CLASS_NAME = "pre-settings"
