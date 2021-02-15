from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import csv
import json

# from otree.models_concrete import ParticipantToPlayerLookup, RoomToSession

# from otree.models.session import Session as BaseSession
author = 'Philipp Chapkovski, University of Zurich'

doc = """
Randomizing app sequence
"""


def seq_to_dict(s):
    r = {}
    l = len(s) - 1
    for i, j in enumerate(s):
        if i < l:
            r[j] = s[i + 1]
        else:
            r[j] = None
    return r


class Constants(BaseConstants):
    name_in_url = 'intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        app_seq = self.session.config.get('app_sequence')
        first_app, *tail = app_seq
        random.shuffle(tail)
        for p in self.get_players():
            new_app_seq = [first_app] + tail
            p.sequence_of_apps = json.dumps(new_app_seq)
            p.participant.vars['_updated_seq_apps'] = seq_to_dict(new_app_seq)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sequence_of_apps = models.LongStringField()
