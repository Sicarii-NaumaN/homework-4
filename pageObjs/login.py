from pageObjs.base import Page


class LoginPage(Page):
    BASE_URL = 'https://pinterbest.ru/login'
    PATH = ''

    FORM_TITLE = '.auth-page__title'
    TOAST_MESSAGE = '.toast__message'

    PASSWORD_INPUT = 'input[name="password"]'
    PASSWORD_ERROR = '.errors.password-errors.input-error-text'

    LOGIN_INPUT = 'input[name="username"]'
    LOGIN_BUTTON = '.auth-form__submit.auth-view__button'
    LOGIN_ERROR = '.errors.name-errors.input-error-text'

    REDIRECT = ''

    def fill_form(self, login, password):
        login_input = self.wait_until_and_get_elem_by_css(self.LOGIN_INPUT)
        password_input = self.wait_until_and_get_elem_by_css(self.PASSWORD_INPUT)

        login_input.send_keys(login)
        password_input.send_keys(password)

    def get_toast_message(self):
        incorrect_username_or_pwd = self.wait_until_and_get_elem_by_css(self.TOAST_MESSAGE)
        return incorrect_username_or_pwd.text

    def click_login_button(self):
        button = self.wait_until_and_get_elem_by_css(self.LOGIN_BUTTON)
        button.click()

    def get_form_title(self):
        title = self.wait_until_and_get_elem_by_css(self.FORM_TITLE)
        return title.text

    def get_login_error(self):
        error = self.wait_until_and_get_elem_by_css(self.LOGIN_ERROR)
        return error.text

    def get_password_error(self):
        error = self.wait_until_and_get_elem_by_css(self.PASSWORD_ERROR)
        return error.text

    # def click_redirect(self):
    #     button = self.wait_until_and_get_elem_by_css(self.REDIRECT)
    #     button.click()
