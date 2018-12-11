from otree.api import Currency as c, currency_range
from otree.api import Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


def introduction_check(self):
        if (self.participant.vars['consent']): #if you have consent
            if (self.round_number == 1): #if the first treatment section
                return True
            elif (self.round_number == (self.session.config['num_RPS_rounds']+1)): #if second treatment section

                return True
            elif (self.round_number == ((self.session.config['num_RPS_rounds']*2)+1)): #if third treatment section
                return True
            else:
                return False
        else: #if you don't have consent, skip this page
            return False

class PlayerBot(Bot):

    def play_round(self):
        if introduction_check(self):
            yield (pages.Introduction)
        if (((self.round_number <= 1)  or (self.round_number == (self.session.config['num_RPS_rounds']+1)) or (self.round_number == ((self.session.config['num_RPS_rounds']*2)+1))) and (self.participant.vars['consent'])):
            yield Submission (pages.WaitForPlayers, check_html=False)
        if ((self.round_number <= (self.session.config['num_RPS_rounds']*3)) and (self.participant.vars['consent'])):
            yield Submission (pages.Decision, {'decision_vs_adv_1':"Rock", 'decision_of_adv_1':"Paper",'advisor_choice':"human"}, check_html=False)
        if ((self.round_number == ((self.session.config['num_RPS_rounds']*3)+1)) and (self.participant.vars['consent'])):
            yield (pages.Results)
