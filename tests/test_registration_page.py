
from demoqa_tests.pages.registration_page import RegistrationPage


def test_registration_page(open_registration_page):

    registration_page = RegistrationPage()
    registration_page.open()

    #registration_form_inputs
    (
    registration_page
    .fill_first_name('John')
    .fill_last_name('Smith')
    .fill_email('qwerty@mail.com')
    .fill_phone("7985258684")
    .fill_address("Finland, Central Street, 25, 13")

    #registration_form_radiobutton
    .select_gender('Male')

    #registration_form_dropdowns_dateOfBirth
    .fill_date_of_birth(1994, 11, 10)

    #registration_form_dropdowns_subjects
    .fill_subjects('Maths')
    .fill_subjects('Computer Science')

    #registration_form_checkbox
    .fill_hobbies('Sports')
    .fill_hobbies('Reading')

    #registration_form_uploadPicture
    .upload_file("kapi.jpg")

    #registration_form_dropdowns_stateCity
    .fill_state("Haryana")
    .fill_city("Karnal")

    .click_submit()

    .should_registered_user_with(
        full_name="John Smith",
        email="qwerty@mail.com",
        gender="Male",
        number="7985258684",
        date_of_birth="10 November,1994",
        subject="Maths, Computer Science",
        hobbies="Sports, Reading",
        upload_file="kapi.jpg",
        address="Finland, Central Street, 25, 13",
        state_city="Haryana Karnal"
        )
    )


