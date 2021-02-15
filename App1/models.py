from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import csv
import json

author = 'Philipp Chapkovski, HSE-Moscow'

doc = """
    app1
"""


class Constants(BaseConstants):
    name_in_url = 'app1'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.IntegerField()
