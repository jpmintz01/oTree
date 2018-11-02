from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Spear'

doc = """
This is a 'strategic' one-shot "Prisoner's Dilemma". There are 3 human players (including you) and 2 artificial players. Players are asked separately
whether they want to Peace or War. Their choices directly determine the
payoffs.

At each "turn", the player must make a play (Peace or War) with all other players.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner_multiplayer'
    players_per_group = None
    num_adversaries = 3 #human, human+AI, AI-only
    num_rounds = 50 #this is set high just to be higher than self.session.config['num_rounds']
    # the below two must add up to the num_adversaries
    #num_rounds = self.session.config['num_rounds']
    #num_AI_adv = 2
    #num_human_adv = 2
    # 
    instructions_template = 'prisoner_multiplayer/Instructions.html'
    # payoff if 1 player Wars and the other Peaces""",
    betray_payoff = c(3)
    betrayed_payoff = c(0)
    
    # payoff if both players Peace or both War
    both_Peace_payoff = c(2)
    both_War_payoff = c(1)
    human_choices = {0: 'Peace', 1: 'Peace', 2: 'War', 3: 'Peace', 4: 'War', 5: 'War', 6: 'War', 7: 'Peace', 8: 'Peace', 9: 'War', 10: 'Peace', 11: 'Peace', 12: 'War', 13: 'Peace', 14: 'Peace', 15: 'Peace', 16: 'Peace', 17: 'Peace', 18: 'War', 19: 'War', 20: 'War', 21: 'War', 22: 'War', 23: 'Peace', 24: 'Peace', 25: 'Peace', 26: 'War', 27: 'Peace', 28: 'War', 29: 'Peace', 30: 'Peace', 31: 'War', 32: 'Peace', 33: 'Peace', 34: 'War', 35: 'Peace', 36: 'Peace', 37: 'War', 38: 'Peace', 39: 'Peace', 40: 'War', 41: 'War', 42: 'War', 43: 'Peace', 44: 'War', 45: 'War', 46: 'War', 47: 'Peace', 48: 'Peace', 49: 'War'}
    human_ai_choices = {0: 'Peace', 1: 'War', 2: 'Peace', 3: 'Peace', 4: 'War', 5: 'Peace', 6: 'Peace', 7: 'Peace', 8: 'Peace', 9: 'War', 10: 'Peace', 11: 'Peace', 12: 'War', 13: 'Peace', 14: 'Peace', 15: 'War', 16: 'War', 17: 'War', 18: 'War', 19: 'Peace', 20: 'War', 21: 'War', 22: 'Peace', 23: 'Peace', 24: 'Peace', 25: 'Peace', 26: 'Peace', 27: 'War', 28: 'Peace', 29: 'War', 30: 'Peace', 31: 'Peace', 32: 'War', 33: 'Peace', 34: 'War', 35: 'Peace', 36: 'Peace', 37: 'War', 38: 'Peace', 39: 'Peace', 40: 'Peace', 41: 'War', 42: 'Peace', 43: 'Peace', 44: 'Peace', 45: 'War', 46: 'Peace', 47: 'Peace', 48: 'Peace', 49: 'Peace'}
    ai_choices = {0: 'War', 1: 'War', 2: 'War', 3: 'Peace', 4: 'Peace', 5: 'War', 6: 'War', 7: 'War', 8: 'Peace', 9: 'War', 10: 'Peace', 11: 'Peace', 12: 'Peace', 13: 'War', 14: 'Peace', 15: 'War', 16: 'War', 17: 'Peace', 18: 'War', 19: 'Peace', 20: 'Peace', 21: 'War', 22: 'Peace', 23: 'Peace', 24: 'Peace', 25: 'War', 26: 'War', 27: 'Peace', 28: 'War', 29: 'War', 30: 'War', 31: 'War', 32: 'War', 33: 'War', 34: 'Peace', 35: 'Peace', 36: 'Peace', 37: 'Peace', 38: 'War', 39: 'War', 40: 'War', 41: 'Peace', 42: 'Peace', 43: 'Peace', 44: 'War', 45: 'Peace', 46: 'Peace', 47: 'Peace', 48: 'Peace', 49: 'War'}
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Adversary:  ## not used in this version - didn't work with oTree
    adv_decision = models.StringField(
        choices=['Peace', 'War'],
        doc="""Adversary decision""",
        widget=widgets.RadioSelect
    )
    player_decision = models.StringField(
        choices=['Peace', 'War'],
        doc="""Adversary decision""",
        widget=widgets.RadioSelect
    )
    adv_payoff = models.CurrencyField(
        choices=currency_range(c(0), c(3), c(1)),
        initial=c(0)
    )
    player_payoff = models.CurrencyField(
        choices=currency_range(c(0), c(3), c(1)),
        initial=c(0)
    )
    adv_type = models.StringField(
        choices=['human','AI'],
        doc="""Adversary type""",
        widget=widgets.RadioSelect
    )
    round_number = models.IntegerField(initial=1)

    def adv_choice_function(adversary, self, player_choice_last_round):
        choice_list = ['Peace','War']
        if adversary.adv_type == 'human': #if adv = human
            adversary.adv_decision = random.choice(choice_list)#define human strategy (random choice)
        else: # this is the AI 'TFT
            if adversary.round_number == 1: # Peace in round one (can change)
                adversary.adv_decision = 'Peace'
            else:
                if player_choice_last_round == 'War': #no max arg needed because it's nested if that isn't round 1
                   adversary.adv_decision = 'War' #if player Wars, adv Wars
                else:
                    adversary.adv_decision = 'Peace'

class Player(BasePlayer):
    ###### adversary #1 (ensure Constants.num_adversaries is correct until incorporating {}.format(i) into the PLayer class
    decision_vs_adv_1 = models.StringField( #my decision
        choices=['Peace', 'War'],
        doc="""This player's decision vs human""",
        widget=widgets.RadioSelect
    )
    decision_of_adv_1 = models.StringField( #adv decision
        choices=['Peace', 'War'],
        doc="""Human adversary's decision""",
        widget=widgets.RadioSelect
    )
    payoff_vs_adv_1 = models.CurrencyField(#my payoff
        choices=currency_range(c(0), Constants.betray_payoff, c(1)),
        initial=c(0)
    )
    payoff_of_adv_1 = models.CurrencyField(#adv's payoff
        choices=currency_range(c(0), Constants.betray_payoff, c(1)),
        initial=c(0)
    )
    adv_1_type = models.StringField(
        choices=['human','human+AI','AI'],
        doc="""Adversary type""",
        widget=widgets.RadioSelect,
        initial='human'
    )
    ######### end adversary #1

  ###### adversary #2 (ensure Constants.num_adversaries is correct until incorporating {}.format(i) into the PLayer class
    decision_vs_adv_2 = models.StringField( #my decision
        choices=['Peace', 'War'],
        doc="""This player's decision vs human+AI""",
        widget=widgets.RadioSelect
    )
    decision_of_adv_2 = models.StringField( #adv decision
        choices=['Peace', 'War'],
        doc="""Human+AI adversary's decision""",
        widget=widgets.RadioSelect
    )
    payoff_vs_adv_2 = models.CurrencyField(#my payoff
        choices=currency_range(c(0), Constants.betray_payoff, c(1)),
        initial=c(0)
    )
    payoff_of_adv_2 = models.CurrencyField(#adv's payoff
        choices=currency_range(c(0), Constants.betray_payoff, c(1)),
        initial=c(0)
    )
    adv_2_type = models.StringField(
        choices=['human','human+AI','AI'],
        doc="""Adversary type""",
        widget=widgets.RadioSelect,
        initial='human+AI'
    )
    ######### end adversary #1
      ###### adversary #1 (ensure Constants.num_adversaries is correct until incorporating {}.format(i) into the PLayer class
    decision_vs_adv_3 = models.StringField( #my decision
        choices=['Peace', 'War'],
        doc="""This player's decision vs AI""",
        widget=widgets.RadioSelect
    )
    decision_of_adv_3 = models.StringField( #adv decision
        choices=['Peace', 'War'],
        doc="""AI adversary's decision""",
        widget=widgets.RadioSelect
    )
    payoff_vs_adv_3 = models.CurrencyField(#my payoff
        choices=currency_range(c(0), Constants.betray_payoff, c(1)),
        initial=c(0)
    )
    payoff_of_adv_3 = models.CurrencyField(#adv's payoff
        choices=currency_range(c(0), Constants.betray_payoff, c(1)),
        initial=c(0)
    )
    adv_3_type = models.StringField(
        choices=['human','human+AI','AI'],
        doc="""Adversary type""",
        widget=widgets.RadioSelect,
        initial='AI'
    )
    ######### end adversary #3
    player_guess_adv_1_type = models.StringField(
        choices=['Simple Algorithm', 'Artificial Intelligence'],
        label='What type of machine were you just playing with?',
        widget=widgets.RadioSelect
    )
    
    round_payoff = models.CurrencyField(
        choices=currency_range(c(0), c(1000), c(1)),
        initial=c(0)
        #c(1000) is just an arbitrary allowed max amount
    )

    
    def set_payoff(self):
        payoff_matrix = {
            'Peace':
                {
                    'Peace': Constants.both_Peace_payoff,
                    'War': Constants.betrayed_payoff
                },
            'War':
                {
                    'Peace': Constants.betray_payoff,
                    'War': Constants.both_War_payoff
                }
        }
        self.payoff_vs_adv_1 = payoff_matrix[self.decision_vs_adv_1][self.decision_of_adv_1]
        self.payoff_of_adv_1 = payoff_matrix[self.decision_of_adv_1][self.decision_vs_adv_1]
        
        self.payoff_vs_adv_2 = payoff_matrix[self.decision_vs_adv_2][self.decision_of_adv_2]
        self.payoff_of_adv_2 = payoff_matrix[self.decision_of_adv_2][self.decision_vs_adv_2]
        
        self.payoff_vs_adv_3 = payoff_matrix[self.decision_vs_adv_3][self.decision_of_adv_3]
        self.payoff_of_adv_3 = payoff_matrix[self.decision_of_adv_3][self.decision_vs_adv_3]
        
        self.round_payoff = self.payoff_vs_adv_1 + self.payoff_vs_adv_2 + self.payoff_vs_adv_3

 
