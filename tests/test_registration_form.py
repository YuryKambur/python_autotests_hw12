import os

import pytest
from selene import browser, have, by, be, command


def test_registration_form_inputs(open_registration_form):
    browser.element("#firstName").type("Yury")
    browser.element("#lastName").type("K")
    browser.element("#userEmail").type("kk@ya.ru")
    browser.element("#userNumber").type("7985258684")
    browser.element("#currentAddress").type("Finland, Central Street, 25, 13")

    browser.element("#firstName").should(have.value("Yury"))
    browser.element("#lastName").should(have.value("K"))
    browser.element("#userEmail").should(have.value("kk@ya.ru"))
    browser.element("#userNumber").should(have.value("7985258684"))
    browser.element(
        "#currentAddress").should(have.value("Finland, Central Street, 25, 13"))

def test_registration_form_radiobutton():
    browser.element('label[for="gender-radio-1"]').click()

def test_registration_form_checkbox():
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()

def test_registration_form_dropdowns_subjects():
    browser.element("#subjectsContainer").click()
    browser.element("#subjectsInput").type("Maths").press_enter()
    browser.element("#subjectsInput").type("Computer")
    browser.element(by.text("Computer Science")).click()

def test_registration_form_dropdowns_dateOfBirth():
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__year-select").click()
    browser.element("option[value='1994']").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element("option[value='11']").click()
    browser.element(
        "//div[contains(@class, 'react-datepicker__day') and text()='10' and not(contains(@class, 'outside-month'))]").click()


def test_registration_form_uploadPicture():
    browser.element("#uploadPicture").send_keys(os.path.abspath("../python_autotests_hw4/tests/kapi.jpg"))


def test_registration_form_dropdowns_stateCity():
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()

def test_registration_form_submit():
    browser.element("#submit").click()

def test_modal_thanks_for_submitting_form():

    browser.element('//td[text()="Student Name"]/following-sibling::td').should(have.text('Yury K'))
    browser.element('//td[text()="Student Email"]/following-sibling::td').should(have.text('kk@ya.ru'))
    browser.element('//td[text()="Gender"]/following-sibling::td').should(have.text('Male'))
    browser.element('//td[text()="Mobile"]/following-sibling::td').should(have.text('7985258684'))
    browser.element('//td[text()="Date of Birth"]/following-sibling::td').should(have.text('10 December,1994'))
    browser.element('//td[text()="Subjects"]/following-sibling::td').should(have.text('Maths, Computer Science'))
    browser.element('//td[text()="Hobbies"]/following-sibling::td').should(have.text('Sports, Reading, Music'))
    browser.element('//td[text()="Picture"]/following-sibling::td').should(have.text('kapi.jpg'))
    browser.element('//td[text()="Address"]/following-sibling::td').should(
        have.text('Finland, Central Street, 25, 13'))
    browser.element('//td[text()="State and City"]/following-sibling::td').should(have.text('Haryana Karnal'))
    browser.driver.refresh()
