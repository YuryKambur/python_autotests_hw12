from typing import Literal

from selene import browser, have, command

from demoqa_tests import resource


class RegistrationPage:

    def __init__(self):
        pass


    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

        return self

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def fill_phone(self, value):
        browser.element("#userNumber").type(value)
        return self

    def fill_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def select_gender(self, gender: Literal['Male', 'Female', 'Other']):
        browser.element(
            {'Male': 'label[for="gender-radio-1"]',
             'Female': 'label[for="gender-radio-2"]',
             'Other': 'label[for="gender-radio-3"]'}[gender]
        ).click()
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__year-select").click()
        browser.element(f'option[value="{year}"]').click()
        browser.element(".react-datepicker__month-select").click()
        browser.element(f'option[value="{int(month)-1}"]').click()
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, value):
        browser.element("#subjectsContainer").click()
        browser.element("#subjectsInput").type(value).press_enter()
        return self

    def fill_hobbies(self, value: Literal['Sports', 'Reading', 'Music']):
        browser.element(
            {'Sports': 'label[for="hobbies-checkbox-1"]',
            'Reading': 'label[for="hobbies-checkbox-2"]',
            'Music': 'label[for="hobbies-checkbox-3"]'}[value]
        ).click()
        return self

    def upload_file(self, value):
        browser.element('#uploadPicture').set_value(resource.path(value))
        return self

    def fill_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self
        return self
    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def click_submit(self):
        browser.element("#submit").click()
        return self

    def should_registered_user_with(self, full_name, email, gender, number, date_of_birth,
                                    subject, hobbies, upload_file, address, state_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                date_of_birth,
                subject,
                hobbies,
                upload_file,
                address,
                state_city
            )
        )
        return self
