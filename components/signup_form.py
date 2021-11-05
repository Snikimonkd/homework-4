from components.default import Component
from components.settings import PreSettingsForm


class SignupForm(PreSettingsForm):
    PAGE_CLASS = 'signup-block'
    
    SUBMIT = 'signup__form-submit'
    SIGNUP_BLOCK = '//*[@class="signup-block"]'
    SIGNUP_BLOCK_CLASS_NAME = "signup-block"
    PRE_SETTINGS_BLOCK = '//*[@class="pre-settings"]'
    PRE_SETTINGS_BLOCK_CLASS_NAME = "pre-settings"

    def check_non_valid(self, id):
        return self.check_non_valid_by_id('signup_'+id+'_form-item')
