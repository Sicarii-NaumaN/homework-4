from pageObjs.base import Page


class RegistrationPage(Page):
    BASE_URL = 'https://pinterbest.ru/signup'

    FORM_TITLE = '.form__title'

    LOGIN_INPUT = 'input[name="username"]'
    PASSWORD_INPUT = 'input[name="password"]'
    EMAIL_INPUT = 'input[name="email"]'

    REGISTRATION_BUTTON = '.auth-form__submit.auth-view__button'
    REDIRECT = '.auth-button.auth-view__button'

    PASSWORD_ERROR = '.errors.password-errors.input-error-text'
    LOGIN_ERROR = '.errors.name-errors.input-error-text'
    EMAIL_ERROR = '.errors.email-errors.input-error-text'

    TOAST_MESSAGE = '.toast__message'

    def fill_form(self, login, password, email):
        login_input = self.wait_until_and_get_elem_by_css(self.LOGIN_INPUT)
        password_input = self.wait_until_and_get_elem_by_css(self.PASSWORD_INPUT)
        email_input = self.wait_until_and_get_elem_by_css(self.EMAIL_INPUT)

        login_input.send_keys(login)
        password_input.send_keys(password)
        email_input.send_keys(email)

    def click_registration_button(self):
        button = self.wait_until_and_get_elem_by_css(self.REGISTRATION_BUTTON)
        button.click()

    def click_redirect(self):
        button = self.wait_until_and_get_elem_by_css(self.REDIRECT)
        button.click()

    def get_form_title(self):
        title = self.wait_until_and_get_elem_by_css(self.FORM_TITLE)
        return title.text

    def get_login_error(self):
        error = self.wait_until_and_get_elem_by_css(self.LOGIN_ERROR)
        return error.text

    def get_existing_login_error(self):
        error = self.wait_until_and_get_elem_by_css(self.EMAIL_ERROR)
        return error.text

    def get_toast_message(self):
        taken_login_or_email = self.wait_until_and_get_elem_by_css(self.TOAST_MESSAGE)
        return taken_login_or_email.text

    def get_password_error(self):
        error = self.wait_until_and_get_elem_by_css(self.PASSWORD_ERROR)
        return error.text

    def get_email_error(self):
        error = self.wait_until_and_get_elem_by_css(self.EMAIL_ERROR)
        return error.text
