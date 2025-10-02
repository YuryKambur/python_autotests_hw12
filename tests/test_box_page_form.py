from demoqa_tests.application import app
from demoqa_tests.users import users


def test_box_page_form(open_registration_page):

    app.panel.open_form()
    app.register.fill_box_page_form(users.admin)
    app.profile.should_have_data(users.admin)

