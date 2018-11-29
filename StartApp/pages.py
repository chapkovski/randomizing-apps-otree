from ._builtin import Page
import json
import random
from otree.models_concrete import ParticipantToPlayerLookup
from otree.common_internal import (
    get_models_module)
from otree import common_internal



def get_new_sequence_of_apps(app_sequence):
    the_rest = app_sequence[1:]
    random.shuffle(the_rest)
    app_sequence = [app_sequence[0]] + the_rest
    return app_sequence



def build_participant_to_player_lookups(participant,  subsession_app_names, session):
        participant_to_player_lookups = []
        page_index = 0

        for app_name in subsession_app_names:

            views_module = common_internal.get_pages_module(app_name)
            models_module = get_models_module(app_name)
            Constants = models_module.Constants
            Player = models_module.Player

            players_flat = Player.objects.filter(session=session).values(
                'id', 'participant__code', 'participant__id', 'subsession__id',
                'round_number'
            )

            #
            players_by_round = [[] for _ in range(Constants.num_rounds)]
            for p in players_flat:
                players_by_round[p['round_number']-1].append(p)
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

class Letsgetstarted(Page):
    def is_displayed(self):
        print('OLD APP SEQ', self.participant.session.config['app_sequence'])
        if not self.player.sequence_of_apps:
            print('SETTING A NEW RANDOM SEQUENCE...')
            ParticipantToPlayerLookup.objects.filter(participant=self.participant).delete()
            self.player.sequence_of_apps = json.dumps(get_new_sequence_of_apps(self.session.config['app_sequence']))
            build_participant_to_player_lookups(self.participant, json.loads(self.player.sequence_of_apps), self.session)
        return True


page_sequence = [
    Letsgetstarted,
]
