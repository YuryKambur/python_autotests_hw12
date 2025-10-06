import allure
from allure_commons.types import AttachmentType

from demoqa_tests.application import app
from demoqa_tests.users import users


def test_box_page_form(setup_browser):

    with allure.step('Открыть demoqa.com на странице Text Box'):
        app.panel.open_form()
    with allure.step('Заполнить Text Box валидными данными'):
        app.register.fill_box_page_form(users.admin)
    with allure.step('Проверить результат заполнения'):
        app.profile.should_have_data(users.admin)
