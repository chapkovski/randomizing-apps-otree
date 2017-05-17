from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import csv
import json
from otree.models_concrete import ParticipantToPlayerLookup, RoomToSession
# from otree.models.session import Session as BaseSession
author = 'Philipp Chapkovski, University of Zurich'

doc = """
intro
"""


class Constants(BaseConstants):
    name_in_url = 'intro'
    players_per_group = None
    num_rounds = 1
    # 'apps' are just set of pages.
    # 'fields' is a dictionary that associates each page with a set of fields

class Subsession(BaseSubsession):
    ...


class Group(BaseGroup):
    ...


class Player(BasePlayer):
    sequence_of_apps = models.TextField()
