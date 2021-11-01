from components.default import Component


class HeaderForm(Component):
    SWITCH_BTN_CLASS = 'switch-btn'
    SETTINGS_XPATH = '//*[@href="/settings"]'
    SETTINGS_HREF_ID = 'home-icon__Settings__href'
    SETTINGS_ID = 'home-icon__Settings'
    MESSAGES_XPATH = '//*[@href="/settings"]'
    MESSAGES_HREF_ID = 'home-icon__Messages__href'
    MESSAGES_ID = 'home-icon__Messages'
    # HOME_XPATH = '//*[@href="/"]'
    HOME_HREF_ID = 'home-icon__Home__href'
    HOME_ID = 'home-icon__Home'
    MAIN_LOGO_CLASS = 'label-href'
    BURGER_ID = 'burger-button'

    HEADER_TABBAR = 'header__tabbar'

    _ACTIVE_ICON = 'active-icon'
    _DISABLE_ICON = 'disable-icon'

    def check_header_close(self):
        return self.check_class_in_element(self.driver.find_element_by_class_name(self.HEADER_TABBAR), 'header_close')

    def check_icon_active(self, id):
        return self.check_class_in_element(self.driver.find_element_by_id(id), self._ACTIVE_ICON)

    def theme_is_dark(self):
        return self.driver.find_elements_by_css_selector('body').get_attribute('scheme') == 'space_gray'