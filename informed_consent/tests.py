from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.InformedConsent, {'agree_to_participate': "True"})
#        yield (pages.Experience, {'experiment_contamination': 'nothing',
#                   'attention_check': 'Georgia'})
        yield (pages.Introduction)
