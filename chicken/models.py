from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Spear'

doc = """
This is a game of "Stochastic Chicken". There are human players (including you) and artificial players. Players are asked separately
whether they want to stay straight ahead or swerve. Their choices directly determine the payoffs, with the caveat that there's a chance of dying in a crash (getting a big negative payoff).

At each "turn", the player must make a play (straight or swerve) with all other players.
"""


class Constants(BaseConstants):
    name_in_url = 'chicken'
    players_per_group = None
    num_adversaries = 2
    num_rounds = 50 #this is set high just to be higher than self.session.config['num_rounds']
    # the below two must add up to the num_adversaries
    #num_rounds = self.session.config['num_rounds']
    #num_AI_adv = 2
    #num_human_adv = 2
    # 
    instructions_template = 'chicken/Instructions.html'
    # payoff if 1 player defects and the other cooperates""",
    crash_payoff = c(-100)
    winner_payoff = c(1)
    
    # payoff if both players cooperate or both defect
    both_swerve_payoff = c(0)
    loser_payoff = c(-1)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Adversary:  ## not used in this version - didn't work with oTree
    adv_decision = models.StringField(
        choices=['Cooperate', 'Defect'],
        doc="""Adversary decision""",
        widget=widgets.RadioSelect
    )
    player_decision = models.StringField(
        choices=['Cooperate', 'Defect'],
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
        choice_list = ['Cooperate','Defect']
        if adversary.adv_type == 'human': #if adv = human
            adversary.adv_decision = random.choice(choice_list)#define human strategy (random choice)
        else: # this is the AI 'TFT
            if adversary.round_number == 1: # cooperate in round one (can change)
                adversary.adv_decision = 'Cooperate'
            else:
                if player_choice_last_round == 'Defect': #no max arg needed because it's nested if that isn't round 1
                   adversary.adv_decision = 'Defect' #if player defects, adv defects
                else:
                    adversary.adv_decision = 'Cooperate'

class Player(BasePlayer):
    ###### adversary #1 (ensure Constants.num_adversaries is correct until incorporating {}.format(i) into the PLayer class
    decision_vs_adv_1 = models.StringField( #my decision
        choices=['Straight', 'Swerve'],
        doc="""This player's decision vs human 1""",
        widget=widgets.RadioSelect
    )
    decision_of_adv_1 = models.StringField( #adv decision
        choices=['Straight', 'Swerve'],
        doc="""This player's decision vs human 1""",
        widget=widgets.RadioSelect
    )
    payoff_vs_adv_1 = models.CurrencyField(#my payoff
        choices=currency_range(Constants.crash_payoff, Constants.winner_payoff, c(1)),
        initial=c(0)
    )
    payoff_of_adv_1 = models.CurrencyField(#adv's payoff
        choices=currency_range(Constants.crash_payoff, Constants.winner_payoff, c(1)),
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
    decision_vs_adv_2 = models.StringField( #my decision
        choices=['Straight', 'Swerve'],
        doc="""This player's decision vs adv 2""",
        widget=widgets.RadioSelect
    )
    decision_of_adv_2 = models.StringField( #adv decision
        choices=['Straight', 'Swerve'],
        doc="""This player's decision vs adv 2""",
        widget=widgets.RadioSelect
    )
    payoff_vs_adv_2 = models.CurrencyField(#my payoff
        choices=currency_range(Constants.crash_payoff, Constants.winner_payoff, c(1)),
        initial=c(0)
    )
    payoff_of_adv_2 = models.CurrencyField(#adv's payoff
        choices=currency_range(Constants.crash_payoff, Constants.winner_payoff, c(1)),
        initial=c(0)
    )
    adv_2_type = models.StringField(
        choices=['human','AI'],
        doc="""Adversary type""",
        widget=widgets.RadioSelect,
        initial='AI'
    )
    ########## end adversary #2
    player_guess_adv_1_type = models.StringField(
        choices=['Simple Algorithm', 'Artificial Intelligence'],
        label='What type of machine were you just playing with?',
        widget=widgets.RadioSelect
    )

    round_payoff = models.CurrencyField(
        choices=currency_range(c(-10000), c(100), c(1)),
        initial=c(0)
        #c(1000) and c(100) are just an arbitrary allowed max amount but are related to Constants.crash_payoff
    )
    
    

        
    def set_payoff(self):
        
        def generate_payoffs(my_decision, adv_decision, random_num):
            payoff_matrix = {
                'Straight':
                    {
                        'Straight': Constants.crash_payoff, 
                        'Swerve': Constants.winner_payoff
                    },
                'Swerve':
                    {
                        'Straight': Constants.loser_payoff,
                        'Swerve': Constants.both_swerve_payoff
                    }
            }

            if my_decision == 'Swerve' and 1/random_num >= self.session.config['swerve_death_chance']:
                return Constants.crash_payoff
            elif my_decision == 'Straight' and adv_decision == 'Straight' and 1/random_num <= self.session.config['crash_death_chance']:
                return Constants.winner_payoff
            else:
                return payoff_matrix[my_decision][adv_decision]
                




            
        self.payoff_vs_adv_1 = generate_payoffs(self.decision_vs_adv_1, self.decision_of_adv_1, random.random())
        self.payoff_of_adv_1 = generate_payoffs(self.decision_of_adv_1, self.decision_vs_adv_1, random.random())
        
        self.payoff_vs_adv_2 = generate_payoffs(self.decision_vs_adv_2, self.decision_of_adv_2, random.random())
        self.payoff_of_adv_2 = generate_payoffs(self.decision_of_adv_2, self.decision_vs_adv_2, random.random())
        
#        if (self.decision_vs_adv_1 == 'Straight') and (self.decision_of_adv_1 == 'Straight') and (random.randint(1,self.session.config['crash_death_chance']) <=1):
#            self.payoff_vs_adv_1 = Constants
#        if random.random() <= self.session.config['swerve_death_chance']:
#            swerve_payoff = Constants.crash_Payoff
            
        self.round_payoff = self.payoff_vs_adv_1 + self.payoff_vs_adv_2

 
