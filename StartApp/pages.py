from ._builtin import Page as oTreePage
import json
import random
from otree.lookup import url_i_should_be_on, get_page_lookup, get_min_idx_for_app


class Page(oTreePage):
    def post(self):
        r = super().post()
        current_app = self._lookup.app_name
        try:
            next_app = get_page_lookup(self.session.code, self.participant._index_in_pages).app_name
        except KeyError:
            # in this case it's apparently the last app in the original app_sequence
            next_app = None
        if current_app == next_app:
            return r
        seq_dict = self.participant.vars.get('_updated_seq_apps')
        if seq_dict:
            app_to_skip_to = seq_dict.get(current_app)
            if app_to_skip_to:
                where_to = get_min_idx_for_app(self.participant._session_code, app_to_skip_to)
            else:
                where_to = self.participant._max_page_index + 1
            self.participant._index_in_pages = where_to
            self._is_frozen = False
            self._index_in_pages = where_to
            return self._redirect_to_page_the_user_should_be_on()
        else:
            return r


class Letsgetstarted(Page):
    def is_displayed(self):
        return True


page_sequence = [
    Letsgetstarted,
]
