from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InformedConsent(Page):
    form_model = 'player'
    form_fields = ['agree_to_participate']
    def before_next_page (self):
        if (self.player.agree_to_participate == "True"):
            self.participant.vars['consent'] = True
        else:
            self.participant.vars['consent'] = False

page_sequence = [
    InformedConsent
]
