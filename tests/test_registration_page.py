
from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.users import users


def test_registration_page(open_registration_page):

    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_from(users.guest)
    registration_page.panel.should_have_data(users.guest)


