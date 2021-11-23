from pageObjs.base import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class NavbarPage(Page):
    # Selectors
    BASE_URL = 'https://pinterbest.ru/'
    PATH = ''
    USERNAME = ".navbar__username"#".profile-info__username"
    LOGO = '.fab fa-pinterest sidebar__logo-image'

    # Sidebar
    BELL = '.notifications-toggle'
    NIGHT_THEME = '.sidebar__toggle theme-toggle'
    CHAT = '.sidebar__toggle.slider-toggle'

    PROFILE = '.navbar__username'
    LOGOUT = '.navbar__dropdown-action'
    DROP_DOWN_MENU = '.fas.fa-ellipsis-v.navbar__action-icon'
    REGISTRATION = '.navbar__auth-link navbar__auth-link_secondary'
    LOGIN = '.navbar__auth-link.navbar__auth-link_primary'

    LOGIN_TITLE = '.navbar__auth-text'
    NO_NOTIFICATION_TITLE = '.slider__feature-description'

    def get_login(self):
        login_text = self.wait_until_and_get_elem_by_css(self.USERNAME)
        return login_text.text

    # By.CSS_SELECTOR("div[class='{}']".format(self.USERNAME))
    def click_logo(self):
        logo = self.wait_until_and_get_elem_by_css(self.LOGO)
        logo.click()

    def click_bell(self):
        bell = self.wait_until_and_get_elem_by_css(self.BELL)
        bell.click()

    def get_no_notifications_text(self):
        title = self.wait_until_and_get_elem_by_css(self.NO_NOTIFICATION_TITLE)
        return title.text

    def click_profile(self):
        profile = self.wait_until_and_get_elem_by_css(self.PROFILE)
        profile.click()

    def click_chat(self):
        chat = self.wait_until_and_get_elem_by_css(self.CHAT)
        chat.click()

    def click_logout(self):
        menu = self.wait_until_and_get_elem_by_css(self.DROP_DOWN_MENU)
        menu.click()

        logout = self.wait_until_and_get_elem_by_css(self.LOGOUT)
        logout.click()

    def open_menu(self):
        menu = self.wait_until_and_get_elem_by_css(self.DROP_DOWN_MENU)
        menu.click()

    def get_registration_logo(self):
        logo = self.wait_until_and_get_elem_by_css(self.REGISTRATION)
        return logo

    def get_login_text(self):
        title = self.wait_until_and_get_elem_by_css(self.LOGIN_TITLE)
        return title.text
