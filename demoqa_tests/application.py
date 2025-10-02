from demoqa_tests.components.panel import Panel
from demoqa_tests.pages.text_box_page import TextBoxPage



class Application:
    def __init__(self):
        self.panel = Panel()
        self.register = TextBoxPage()
        self.profile = TextBoxPage()


app = Application()