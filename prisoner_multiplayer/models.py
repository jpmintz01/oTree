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

 
