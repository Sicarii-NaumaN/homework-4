import random
import string
from cases.base import Test
from pageObjs.registration import RegistrationPage
from pageObjs.navbar import NavbarPage

short_login = 's'
short_password = '123'

bad_email1 = 'bad.ru'
bad_email2 = '@bad.ru'
bad_email3 = 'bad@ru'
bad_email4 = 'bad@bad'

existing_email = 'test@test.ru'

PROFILE_URL = 'https://pinterbest.ru/profile'
LOGIN_URL = 'https://pinterbest.ru/login'

LOGIN_AVAILABLE = 'Log in'

LOGIN_ERROR_TEXT = 'Username must be 2-42 letters. a-Z, 0-9'
PASSWORD_ERROR_TEXT = 'Password must be 8 to 30 letters long and contains numbers'
EMAIL_ERROR_TEXT = 'Invalid email (example user@pinterbest.com)'
LOGIN_OR_EMAIL_EXISTING_ERROR_TEXT = 'This username or email already taken. Please, choose another one'


class RegistrationTest(Test):
    def setUp(self):
        super().setUp()
        self.page = RegistrationPage(self.driver)

    def test_registration_registration_ok(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        login = 'test' + rand_string
        email = rand_string + '@mail.ru'
        self.page.open()
        self.page.fill_form(login, self.PASSWORD, email)
        self.page.click_registration_button()

        navbar = NavbarPage(self.driver)
        login_text = navbar.get_login()
        self.assertEqual(login, login_text)
        # Проверка что редиректит на страницу профиля
        self.assertEqual(PROFILE_URL, self.driver.current_url)

        navbar.click_logout()
        can_login = navbar.get_login_text()
        # Проверяем на возможно снова авторизоваться
        self.assertEqual(LOGIN_AVAILABLE, can_login)

    def test_registration_empty_fields(self):
        self.page.open()
        self.page.fill_form('', '', '')
        self.page.click_registration_button()

        login_err = self.page.get_login_error()
        password_err = self.page.get_password_error()
        email_err = self.page.get_email_error()

        self.assertEqual(LOGIN_ERROR_TEXT, login_err)
        self.assertEqual(PASSWORD_ERROR_TEXT, password_err)
        self.assertEqual(EMAIL_ERROR_TEXT, email_err)

    def test_registration_short_login(self):
        self.page.open()
        self.page.fill_form(short_login, self.PASSWORD, self.EMAIL)
        self.page.click_registration_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_registration_short_password(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(rand_string, short_password, self.EMAIL)
        self.page.click_registration_button()

        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_registration_with_unsupported_marks(self):
        self.page.open()
        self.page.fill_form(',' + self.LOGIN, self.PASSWORD, ',' + self.EMAIL)
        self.page.click_registration_button()

        login_err = self.page.get_login_error()
        email_err = self.page.get_email_error()

        self.assertEqual(LOGIN_ERROR_TEXT, login_err)
        self.assertEqual(EMAIL_ERROR_TEXT, email_err)

    def test_registration_password_less_8_symbols(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(8))

        self.page.open()
        self.page.fill_form(rand_string, rand_string, self.EMAIL)
        self.page.click_registration_button()

        password_err = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, password_err)

    def test_registration_email_without_sign(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(rand_string, self.PASSWORD, bad_email1)
        self.page.click_registration_button()

        email_err = self.page.get_email_error()

        self.assertEqual(EMAIL_ERROR_TEXT, email_err)

    def test_registration_email_without_login(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(rand_string, self.PASSWORD, bad_email2)
        self.page.click_registration_button()

        email_err = self.page.get_email_error()

        self.assertEqual(EMAIL_ERROR_TEXT, email_err)

    def test_registration_email_without_domain(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(rand_string, self.PASSWORD, bad_email3)
        self.page.click_registration_button()

        email_err = self.page.get_email_error()

        self.assertEqual(EMAIL_ERROR_TEXT, email_err)

    def test_registration_email_without_region(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(rand_string, self.PASSWORD, bad_email4)
        self.page.click_registration_button()

        email_err = self.page.get_email_error()

        self.assertEqual(EMAIL_ERROR_TEXT, email_err)

    def test_registration_login_already_taken(self):
        self.page.open()
        self.page.fill_form(self.LOGIN, self.PASSWORD, self.EMAIL)
        self.page.click_registration_button()

        alert_message = self.page.get_toast_message()

        self.assertEqual(LOGIN_OR_EMAIL_EXISTING_ERROR_TEXT, alert_message)

    def test_registration_email_already_taken(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(rand_string, self.PASSWORD, existing_email)
        self.page.click_registration_button()

        alert_message = self.page.get_toast_message()

        self.assertEqual(LOGIN_OR_EMAIL_EXISTING_ERROR_TEXT, alert_message)

    def test_registration_redirect_to_login(self):
        self.page.open()
        self.page.click_redirect()

        self.assertEqual(LOGIN_URL, self.driver.current_url)
