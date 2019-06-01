from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import csv
import json
from otree.models_concrete import ParticipantToPlayerLookup, RoomToSession

# from otree.models.session import Session as BaseSession
author = 'Philipp Chapkovski, HSE-Moscow'

doc = """
Randomizing app sequence
"""

from otree.models_concrete import ParticipantToPlayerLookup
from otree.common_internal import (
    get_models_module)
from otree import common_internal


def get_new_sequence_of_apps(app_sequence):
    the_rest = app_sequence[1:]
    random.shuffle(the_rest)
    app_sequence = [app_sequence[0]] + the_rest
    return app_sequence


def build_participant_to_player_lookups(participant, subsession_app_names, session):
    participant_to_player_lookups = []
    page_index = 0

    for app_name in subsession_app_names:

        views_module = common_internal.get_pages_module(app_name)
        models_module = get_models_module(app_name)
        Constants = models_module.Constants
        Player = models_module.Player

        players_flat = Player.objects.filter(session=session, participant=participant).values(
            'id', 'participant__code', 'participant__id', 'subsession__id',
            'round_number'
        )

        #
        players_by_round = [[] for _ in range(Constants.num_rounds)]
        for p in players_flat:
            players_by_round[p['round_number'] - 1].append(p)
        for round_number, round_players in enumerate(players_by_round, start=1):
            for View in views_module.page_sequence:
                page_index += 1
                for p in round_players:
                    participant_code = p['participant__code']
                    url = View.get_url(
                        participant_code=participant_code,
                        name_in_url=Constants.name_in_url,
                        page_index=page_index
                    )

                    participant_to_player_lookups.append(
                        ParticipantToPlayerLookup(
                            participant_id=p['participant__id'],
                            participant_code=participant_code,
                            page_index=page_index,
                            app_name=app_name,
                            player_pk=p['id'],
                            subsession_pk=p['subsession__id'],
                            session_pk=session.pk,
                            url=url))

    ParticipantToPlayerLookup.objects.bulk_create(
        participant_to_player_lookups
    )


class Constants(BaseConstants):
    name_in_url = 'intro'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for g in self.get_groups():
            new_app_seq=get_new_sequence_of_apps(self.session.config['app_sequence'])
            for p in g.get_players():
                print('OLD APP SEQ', self.session.config['app_sequence'])
                if not p.sequence_of_apps:
                    ParticipantToPlayerLookup.objects.filter(participant=p.participant).delete()
                    p.sequence_of_apps = json.dumps(new_app_seq)
                    print(f'SETTING A NEW RANDOM SEQUENCE...:::{p.sequence_of_apps}')
                    build_participant_to_player_lookups(p.participant, json.loads(p.sequence_of_apps),
                                                        self.session)


class Group(BaseGroup):
    ...


class Player(BasePlayer):
    sequence_of_apps = models.LongStringField()
