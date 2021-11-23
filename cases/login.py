import random
import string
from cases.base import Test
from pageObjs.login import LoginPage
from pageObjs.navbar import NavbarPage

from selenium.webdriver.support.ui import WebDriverWait

# from pageObjs.registration import RegistrationPage


letters = string.ascii_lowercase

short_login = 's'
short_password = '123'

empty_string = ''

comma_login = 'case,'
comma_password = ',case'
zero_digits_password = 'qwertyuiop'

long_string = 'q' * 257

INCORRECT_LOGIN_OR_PASSWORD = "This user doesn't exist or password is incorrect"
LOGIN_ERROR_TEXT = 'Username must be 2-42 letters. a-Z, 0-9'
LOGIN_EXISTING_ERROR_TEXT = 'й логин уже существует'
PASSWORD_ERROR_TEXT = 'Password must be 8 to 30 letters long and contains numbers'

PROFILE_URL = 'https://pinterbest.ru/profile'
REGISTRATION_URL = 'https://pinterbest.ru/signup'
BASE_URL = 'https://pinterbest.ru/'

LOGIN_AVAILABLE = 'Log in'


class LoginTest(Test):
    def setUp(self):
        super().setUp()
        self.page = LoginPage(self.driver)

    def test_login_ok(self):
        self.page.open()
        self.page.fill_form(self.LOGIN, self.PASSWORD)
        self.page.click_login_button()

        navbar = NavbarPage(self.driver)
        login_text = navbar.get_login()
        self.assertEqual(self.LOGIN, login_text)
        # Проверка что редиректит на страницу профиля
        self.assertEqual(PROFILE_URL, self.driver.current_url)

        navbar.click_logout()
        can_login = navbar.get_login_text()
        # Проверяем на возможно снова авторизоваться
        self.assertEqual(LOGIN_AVAILABLE, can_login)

    def test_login_wrong_login(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(rand_string, self.PASSWORD)
        self.page.click_login_button()

        login_page = LoginPage(self.driver)
        alert_message = login_page.get_toast_message()

        self.assertEqual(INCORRECT_LOGIN_OR_PASSWORD, alert_message)

    def test_login_short_login(self):
        self.page.open()
        self.page.fill_form(short_login, self.PASSWORD)
        self.page.click_login_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_login_login_with_punctuation_marks(self):
        good_password = ''.join(random.choice(letters) for i in range(10))
        self.page.open()
        self.page.fill_form(comma_login, good_password)
        self.page.click_login_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_login_empty_login(self):
        good_password = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(empty_string, good_password)
        self.page.click_login_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_login_empty_login_and_password(self):
        self.page.open()
        self.page.fill_form(empty_string, empty_string)
        self.page.click_login_button()

        login_err = self.page.get_login_error()
        password_err = self.page.get_password_error()

        self.assertEqual(LOGIN_ERROR_TEXT, login_err)
        self.assertEqual(PASSWORD_ERROR_TEXT, password_err)

    def test_login_wrong_password(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(self.LOGIN, rand_string)
        self.page.click_login_button()

        login_page = LoginPage(self.driver)
        alert_message = login_page.get_toast_message()

        self.assertEqual(INCORRECT_LOGIN_OR_PASSWORD, alert_message)

    def test_login_empty_password(self):
        good_login = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(good_login, empty_string)
        self.page.click_login_button()

        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_login_short_password(self):
        good_login = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(good_login, short_password)
        self.page.click_login_button()

        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_login_redirect_to_registration(self):
        self.page.open()
        self.page.click_redirect()

        self.assertEqual(REGISTRATION_URL, self.driver.current_url)
