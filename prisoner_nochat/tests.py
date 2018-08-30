from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    #cases = ['humanBot', 'AIBot']
    def play_round(self):
        #
        #if self.player.id_in_group == 1:
        #    yield (pages.Introduction)
        
        if self.player.id_in_group == 2:
            yield (pages.Decision, {"decision": 'Cooperate'})
            #assert 'Both of you chose to Cooperate' in self.html
            #assert self.player.payoff == Constants.both_cooperate_payoff
            #yield (pages.Results)


        #if self.case == 'AIBot':
            #yield (pages.Decision, {"decision": 'Defect'})
            #assert 'Both of you chose to Cooperate' in self.html
            #assert self.player.payoff == Constants.both_cooperate_payoff
            #yield (pages.Results)

