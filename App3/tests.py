from otree.api import Currency as c, currency_range
from . import pages as p
from ._builtin import Bot
import random
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield p.App3Page1
