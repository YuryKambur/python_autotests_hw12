from datetime import date

from selene import have, browser

from demoqa_tests.users.users import User, Hobby

MONTHS = [
    "", "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

def format_demoqa_date(d) -> str:
    if isinstance(d, date):
        return f"{d.day:02d} {MONTHS[d.month]},{d.year}"
    return str(d)

def format_hobbies(hobbies) -> str:
    if isinstance(hobbies, list):
        return ', '.join(h.value if isinstance(h, Hobby) else str(h) for h in hobbies)
    if isinstance(hobbies, Hobby):
        return hobbies.value


class SubmittingFormPage:
    def should_have_data(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                user.full_name,
                user.email,
                user.gender,
                user.number,
                format_demoqa_date(user.date_of_birth),
                user.subject,
                format_hobbies(user.hobbies),
                user.upload_file,
                user.address,
                user.state_city,
            )
        )
        return self