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
class App1Page1(Page):
    form_model = models.Player
    form_fields = ['decision']

page_sequence = [
    App1Page1
]
