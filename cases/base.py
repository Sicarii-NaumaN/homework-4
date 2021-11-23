import unittest

import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote, ChromeOptions
from selenium.webdriver.chrome.webdriver import Options

from pageObjs.login import LoginPage
from pageObjs.navbar import NavbarPage


class Test(unittest.TestCase):
    page = None
    steps = None

    def setUp(self):
        browser = 'CHROME'
        options = ChromeOptions()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        options.add_experimental_option("prefs", prefs)
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            options=options
        )

        self.LOGIN = os.getenv('LOGIN')
        self.PASSWORD = os.getenv('PASSWORD')
        self.MAIL = os.getenv('MAIL')
        self.LOGIN2 = os.getenv('LOGIN2')
        self.PASSWORD2 = os.getenv('PASSWORD2')
        self.MAIL2 = os.getenv('MAIL2')
        self.ID2 = os.getenv('ID2')
        self.ID = os.getenv('ID')

    def login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.fill_form(self.LOGIN, self.PASSWORD)
        login_page.click_login_button()

    def login2(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.fill_form(self.LOGIN2, self.PASSWORD2)
        login_page.click_login_button()

    def logout(self):
        navbar = NavbarPage(self.driver)
        navbar.open_menu()
        navbar.click_logout()

    def go_to_main(self):
        self.page.open(self.page.BASE_URL)

    def tearDown(self):
        self.driver.quit()
