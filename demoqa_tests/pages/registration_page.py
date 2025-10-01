from typing import Literal
from selene import browser, have, command
from demoqa_tests import resource
from demoqa_tests.pages.submitting_form_page import SubmittingFormPage
from demoqa_tests.users.users import User, Hobby


class RegistrationPage:

    def __init__(self):
        self.panel = SubmittingFormPage()

        self._first_name      = browser.element('#firstName')
        self._last_name       = browser.element('#lastName')
        self._email           = browser.element('#userEmail')
        self._phone           = browser.element('#userNumber')
        self._address         = browser.element('#currentAddress')

        self._gender_male     = browser.element('label[for="gender-radio-1"]')
        self._gender_female   = browser.element('label[for="gender-radio-2"]')
        self._gender_other    = browser.element('label[for="gender-radio-3"]')

        self._dob_input       = browser.element('#dateOfBirthInput')
        self._dob_year_select = browser.element('.react-datepicker__year-select')
        self._dob_month_select= browser.element('.react-datepicker__month-select')

        self._subjects_box    = browser.element('#subjectsContainer')
        self._subjects_input  = browser.element('#subjectsInput')

        self._hobby_sports    = browser.element('label[for="hobbies-checkbox-1"]')
        self._hobby_reading   = browser.element('label[for="hobbies-checkbox-2"]')
        self._hobby_music     = browser.element('label[for="hobbies-checkbox-3"]')

        self._upload          = browser.element('#uploadPicture')

        self._state           = browser.element('#state')
        self._city            = browser.element('#city')
        self._options         = browser.all('[id^=react-select][id*=option]')

        self._submit          = browser.element('#submit')

        self._genders = {
            'Male':   self._gender_male,
            'Female': self._gender_female,
            'Other':  self._gender_other,
        }
        self._hobbies = {
            'Sports':  self._hobby_sports,
            'Reading': self._hobby_reading,
            'Music':   self._hobby_music,
        }

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        self._first_name.type(value)
        return self

    def fill_last_name(self, value):
        self._last_name.type(value)
        return self

    def fill_email(self, value):
        self._email.type(value)
        return self

    def fill_phone(self, value):
        self._phone.type(value)
        return self

    def fill_address(self, value):
        self._address.type(value)
        return self

    def select_gender(self, gender: Literal['Male', 'Female', 'Other']):
        self._genders[gender].click()
        return self

    def fill_date_of_birth(self, year, month, day):
        self._dob_input.click()
        self._dob_year_select.click()
        browser.element(f'option[value="{int(year)}"]').click()
        self._dob_month_select.click()
        browser.element(f'option[value="{int(month)-1}"]').click()
        browser.element(
            f'.react-datepicker__day--0{int(day):02d}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, value):
        self._subjects_box.click()
        self._subjects_input.type(value).press_enter()
        return self

    def fill_hobbies(self, value: Literal['Sports', 'Reading', 'Music']):
        self._hobbies[value].click()
        return self

    def upload_file(self, value):
        self._upload.set_value(resource.path(value))
        return self

    def fill_state(self, value):
        self._state.perform(command.js.scroll_into_view)
        self._state.click()
        self._options.element_by(have.exact_text(value)).click()
        return self

    def fill_city(self, value):
        self._city.click()
        self._options.element_by(have.exact_text(value)).click()
        return self

    def fill_from(self, user: User):

        first, last = user.full_name.split(' ', 1)

        subjects = [s.strip() for s in user.subject.split(',') if s.strip()]
        hobbies = [h.value if isinstance(h, Hobby) else str(h) for h in user.hobbies]

        state_city = user.state_city.split()
        state, city = state_city[0], state_city[-1]

        (self
         .fill_first_name(first)
         .fill_last_name(last)
         .fill_email(user.email)
         .fill_phone(user.number)
         .fill_address(user.address)
         .select_gender(user.gender)
         .fill_date_of_birth(user.date_of_birth.year,
                            user.date_of_birth.month,
                            user.date_of_birth.day)
         )
        for s in subjects:
            self.fill_subjects(s)
        for h in hobbies:
            self.fill_hobbies(h)

        (self
         .upload_file(user.upload_file)
         .fill_state(state)
         .fill_city(city)
         )

        self._submit.click()
        return self
