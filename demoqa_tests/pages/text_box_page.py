import allure
from selene import browser, command, have

from demoqa_tests.users.users import User


class TextBoxPage:
    def __init__(self):
        self.userName = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.address = browser.element('#currentAddress')
        self.perm_address = browser.element('#permanentAddress')
        self.submit = browser.element('#submit')

    def fill_box_page_form(self, user: User):
        with allure.step(f"Ввод имени: {user.full_name}"):
            self.userName.type(user.full_name)
        with allure.step(f"Ввод email: {user.email}"):
            self.email.type(user.email)
        with allure.step(f"Ввод текущего адреса: {user.address}"):
            self.address.type(user.address)
        with allure.step(f"Ввод постоянного адреса: {user.permanent_address}"):
            self.perm_address.type(user.permanent_address)
        with allure.step("Скролл до кнопки и отправка формы"):
            self.submit.perform(command.js.scroll_into_view).click()
        return self

    def should_have_data(self, user: User):
        with allure.step(f"Проверка имени: {user.full_name}"):
            browser.element('#name').should(have.text(user.full_name))
        with allure.step(f"Проверка email: {user.email}"):
            browser.element('#email').should(have.text(user.email))
        with allure.step(f"Проверка текущего адреса: {user.address}"):
            browser.element('#output #currentAddress').should(have.text(user.address))
        with allure.step(f"Проверка постоянного адреса: {user.permanent_address}"):
            browser.element('#output #permanentAddress').should(have.text(user.permanent_address))
        return self
