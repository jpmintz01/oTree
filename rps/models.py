from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Spear'

doc = """
This is a repeated Rock-Paper-Scissors game. 
"""


class Constants(BaseConstants):
    name_in_url = 'rps'
    players_per_group = None
    num_adversaries = 1
    num_rounds = 50 #this is set high just to be higher than self.session.config['num_rounds']
    # the below two must add up to the num_adversaries
    #num_rounds = self.session.config['num_rounds']
    #num_AI_adv = 2
    #num_human_adv = 2
    # 
    instructions_template = 'rps/Instructions.html'
    # payoff if 1 player defects and the other cooperates""",
    win_payoff = c(1)
    draw_payoff = c(0)
    lose_payoff = c(-1)
    adversary_choices = {0: 'Scissors', 1: 'Paper', 2: 'Paper', 3: 'Scissors', 4: 'Scissors', 5: 'Paper', 6: 'Paper', 7: 'Paper', 8: 'Scissors', 9: 'Rock', 10: 'Scissors', 11: 'Scissors', 12: 'Paper', 13: 'Rock', 14: 'Scissors', 15: 'Paper', 16: 'Scissors', 17: 'Paper', 18: 'Paper', 19: 'Rock', 20: 'Scissors', 21: 'Scissors', 22: 'Rock', 23: 'Paper', 24: 'Scissors', 25: 'Paper', 26: 'Scissors', 27: 'Paper', 28: 'Rock', 29: 'Scissors', 30: 'Scissors', 31: 'Paper', 32: 'Scissors', 33: 'Paper', 34: 'Rock', 35: 'Scissors', 36: 'Rock', 37: 'Scissors', 38: 'Scissors', 39: 'Rock', 40: 'Scissors', 41: 'Rock', 42: 'Scissors', 43: 'Scissors', 44: 'Scissors', 45: 'Paper', 46: 'Scissors', 47: 'Paper', 48: 'Scissors', 49: 'Paper'}
    advice_choices = {0: 'Rock', 1: 'Paper', 2: 'Scissors', 3: 'Paper', 4: 'Paper', 5: 'Rock', 6: 'Paper', 7: 'Paper', 8: 'Paper', 9: 'Paper', 10: 'Rock', 11: 'Paper', 12: 'Scissors', 13: 'Scissors', 14: 'Rock', 15: 'Rock', 16: 'Paper', 17: 'Rock', 18: 'Paper', 19: 'Scissors', 20: 'Paper', 21: 'Scissors', 22: 'Rock', 23: 'Rock', 24: 'Rock', 25: 'Rock', 26: 'Scissors', 27: 'Paper', 28: 'Rock', 29: 'Scissors', 30: 'Paper', 31: 'Paper', 32: 'Scissors', 33: 'Scissors', 34: 'Paper', 35: 'Paper', 36: 'Rock', 37: 'Rock', 38: 'Scissors', 39: 'Rock', 40: 'Scissors', 41: 'Scissors', 42: 'Scissors', 43: 'Paper', 44: 'Paper', 45: 'Paper', 46: 'Rock', 47: 'Paper', 48: 'Rock', 49: 'Scissors'} #ai and human advice is the same, to control the experiment
    
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    ###### adversary #1 (ensure Constants.num_adversaries is correct until incorporating {}.format(i) into the PLayer class
    decision_vs_adv_1 = models.StringField( #my decision
        choices=['Rock', 'Paper', 'Scissors'],
        doc="""This player's decision vs human 1""",
        widget=widgets.RadioSelect
    )
    decision_of_adv_1 = models.StringField( #adv decision
        choices=['Rock', 'Paper', 'Scissors'],
        doc="""This player's decision vs human 1""",
        widget=widgets.RadioSelect
    )
    payoff_vs_adv_1 = models.CurrencyField(#my payoff
        choices=currency_range(c(0), Constants.win_payoff, c(1)),
        initial=c(0)
    )
    payoff_of_adv_1 = models.CurrencyField(#adv's payoff
        choices=currency_range(c(0), Constants.win_payoff, c(1)),
        initial=c(0)
    )
    adv_1_type = models.StringField(
        choices=['human','AI'],
        doc="""Adversary type""",
        widget=widgets.RadioSelect,
        initial='human'
    )
    advisor_choice = models.StringField(
        choices=['human','AI','none'],

    )
    ######### end adversary #1
    player_guess_adv_1_type = models.StringField(
        choices=['Simple Algorithm', 'Artificial Intelligence'],
        label='What type of machine were you just playing with?',
        widget=widgets.RadioSelect
    )
    ###### adversary #2 (ensure Constants.num_adversaries is correct until incorporating {}.format(i) into the PLayer class
#    decision_vs_adv_2 = models.StringField( #my decision
#        choices=['Rock', 'Paper', 'Scissors'],
#        doc="""This player's decision vs adv 2""",
#        widget=widgets.RadioSelect
#    )
#    decision_of_adv_2 = models.StringField( #adv decision
#        choices=['Rock', 'Paper', 'Scissors'],
#        doc="""This player's decision vs adv 2""",
#        widget=widgets.RadioSelect
#    )
#    payoff_vs_adv_2 = models.CurrencyField(#my payoff
#        choices=currency_range(c(0), Constants.win_payoff, c(1)),
#        initial=c(0)
#    )
#    payoff_of_adv_2 = models.CurrencyField(#adv's payoff
#        choices=currency_range(c(0), Constants.win_payoff, c(1)),
#        initial=c(0)
#    )
#    adv_2_type = models.StringField(
#        choices=['human','AI'],
#        doc="""Adversary type""",
#        widget=widgets.RadioSelect,
#        initial='AI'
#    )
    ########## end adversary #2

    round_payoff = models.CurrencyField(
        choices=currency_range(c(-1000), c(1000), c(1)),
        initial=c(0)
        #c(1000) is just an arbitrary allowed max amount
    )
    winner = models.StringField(
        choices=["player", 'adversary', 'draw']
    )
    
    def set_payoff(self):
        payoff_matrix = {
            'Rock':
                {
                    'Rock': Constants.draw_payoff,
                    'Paper': Constants.lose_payoff,
                    'Scissors': Constants.win_payoff
                },
            'Paper':
                {
                    'Rock': Constants.win_payoff,
                    'Paper': Constants.draw_payoff,
                    'Scissors': Constants.lose_payoff
                },
            'Scissors':
                {
                    'Rock': Constants.lose_payoff,
                    'Paper': Constants.win_payoff,
                    'Scissors': Constants.draw_payoff
                },
        }
        self.payoff_vs_adv_1 = payoff_matrix[self.decision_vs_adv_1][self.decision_of_adv_1]
        self.payoff_of_adv_1 = payoff_matrix[self.decision_of_adv_1][self.decision_vs_adv_1]
        
#        self.payoff_vs_adv_2 = payoff_matrix[self.decision_vs_adv_2][self.decision_of_adv_2]
#        self.payoff_of_adv_2 = payoff_matrix[self.decision_of_adv_2][self.decision_vs_adv_2]
        
        self.round_payoff = self.payoff_vs_adv_1 #+ self.payoff_vs_adv_2
        if (self.round_payoff == Constants.win_payoff):
            self.winner = "player"
        elif (self.round_payoff == Constants.lose_payoff):
            self.winner = "adversary"
        else:
            self.winner = "draw"
                

 
