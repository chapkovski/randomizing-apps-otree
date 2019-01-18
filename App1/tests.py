from otree.api import Currency as c, currency_range
from . import pages as p
from ._builtin import Bot
import random
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield p.App1Page1, {'decision': random.randint(0, 100)}
