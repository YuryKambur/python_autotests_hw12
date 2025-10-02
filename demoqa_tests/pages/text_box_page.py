from selene import browser, have, command

from demoqa_tests.users.users import User


class TextBoxPage:
    def __init__(self):
        self.userName = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.address = browser.element('#currentAddress')
        self.perm_address = browser.element('#permanentAddress')
        self.submit = browser.element('#submit')

    def fill_box_page_form(self, user:User):
        self.userName.type(user.full_name)
        self.email.type(user.email)
        self.address.type(user.address)
        self.perm_address.type(user.permanent_address)
        self.submit.perform(command.js.scroll_into_view).click()

        return self

    def should_have_data(self, user:User):
        browser.element('#name').should(have.text(user.full_name))
        browser.element('#email').should(have.text(user.email))
        browser.element('#output #currentAddress').should(have.text(user.address))
        browser.element('#output #permanentAddress').should(have.text(user.permanent_address))
        return self