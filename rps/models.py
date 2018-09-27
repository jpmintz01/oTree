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
    ######### end adversary #1

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
        print(self.decision_vs_adv_1)
        print(self.decision_of_adv_1)
#        print(self.decision_vs_adv_2)
#        print(self.decision_of_adv_2)
        self.payoff_vs_adv_1 = payoff_matrix[self.decision_vs_adv_1][self.decision_of_adv_1]
        self.payoff_of_adv_1 = payoff_matrix[self.decision_of_adv_1][self.decision_vs_adv_1]
        
#        self.payoff_vs_adv_2 = payoff_matrix[self.decision_vs_adv_2][self.decision_of_adv_2]
#        self.payoff_of_adv_2 = payoff_matrix[self.decision_of_adv_2][self.decision_vs_adv_2]
        
        self.round_payoff = self.payoff_vs_adv_1 #+ self.payoff_vs_adv_2

 
