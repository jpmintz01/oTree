from otree.api import Currency as c, currency_range
from otree.api import Submission
from . import pages
from ._builtin import Bot
from .models import Constants



class PlayerBot(Bot):

    def play_round(self):
        if ((self.round_number <= 1) and (self.participant.vars['consent']) and self.player.play_now()):
            yield (pages.Introduction)
            yield Submission(pages.WaitForPlayers,{}, check_html=False)
        if ((self.round_number <= self.session.config['num_PW_rounds'])and (self.participant.vars['consent']) and self.player.play_now()): 
            
            yield Submission(pages.Decision, {'decision_vs_adv_1': "Peace", 'decision_vs_adv_2': "Peace", 'decision_vs_adv_3': "Peace"}, check_html=False)
        elif ((self.round_number == self.session.config['num_PW_rounds'])and (self.participant.vars['consent']) and self.player.play_now()):
            yield Submission(pages.Results, check_html=False)

