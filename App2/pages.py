from . import models
from ._builtin import Page, WaitPage
from StartApp.pages import Page
from otree.api import Currency as c, currency_range
from .models import Constants
import json
import random
from random import sample, choice


# You can add as many pages as needed in the beginning and in the end
# of shuffled sequence
class App2Page1(Page):
    pass


page_sequence = [
    App2Page1
]
