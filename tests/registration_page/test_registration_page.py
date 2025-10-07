import allure

from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.users import users


def test_registration_page(setup_browser):

    registration_page = RegistrationPage()
    with allure.step('Открыть demoqa.com на странице Practice Form'):
        registration_page.open()
    with allure.step('Заполнить Practice Form валидными данными'):
        registration_page.fill_from(users.guest)
    with allure.step('Проверить результат заполнения на Submitting Form Page'):
        registration_page.panel.should_have_data(users.guest)


