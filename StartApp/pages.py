from ._builtin import Page
import json
import random

class Letsgetstarted(Page):
    def is_displayed(self):

        return True


page_sequence = [
    Letsgetstarted,
]
