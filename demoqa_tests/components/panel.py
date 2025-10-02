from selene import browser


class Panel:
    def __init__(self):
        self.elements_panel = browser.element("//h5[normalize-space()='Elements']/ancestor::div[contains(@class,'top-card')]")
        self.text_box = browser.element('#item-0')

    def open_form(self):
        browser.open('/')
        self.elements_panel.click()
        self.text_box.click()

        return self