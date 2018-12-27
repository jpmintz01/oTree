from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import string

author = 'Spear'

doc = """
This is a repeated Rock-Paper-Scissors game. 
"""
#version 0.3.1

class Constants(BaseConstants):
    name_in_url = 'rps'
    players_per_group = None
    num_adversaries = 1
    num_rounds = 60 #this is set high just to be higher than 3x self.session.config['num_RPS_rounds']
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
    num_chars_player_id = 5  #ideally should pull this from the participant label file, but can't do that in models.py (I think...)
    human_advisor_1_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    human_advisor_2_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    human_advisor_3_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    
    human_adversary_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    human_ai_adversary_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    ai_adversary_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    
    #these choices may be artifacts if I'm controlling score and not inputs...
    adversary_choices = {0: 'Peace', 1: 'Peace', 2: 'Peace', 3: 'War', 4: 'War', 5: 'Peace', 6: 'Peace', 7: 'Peace', 8: 'War', 9: 'War', 10: 'War', 11: 'War', 12: 'War', 13: 'Peace', 14: 'Peace', 15: 'Peace', 16: 'War', 17: 'Peace', 18: 'War', 19: 'War', 20: 'War', 21: 'War', 22: 'War', 23: 'War', 24: 'Peace', 25: 'War', 26: 'Peace', 27: 'Peace', 28: 'Peace', 29: 'War', 30: 'Peace', 31: 'Peace', 32: 'War', 33: 'War', 34: 'Peace', 35: 'Peace', 36: 'War', 37: 'War', 38: 'War', 39: 'War', 40: 'War', 41: 'War', 42: 'War', 43: 'War', 44: 'Peace', 45: 'War', 46: 'Peace', 47: 'Peace', 48: 'Peace', 49: 'War', 50: 'Peace', 51: 'Peace', 52: 'Peace', 53: 'War', 54: 'Peace', 55: 'War', 56: 'Peace', 57: 'War', 58: 'Peace', 59: 'War', 60: 'Peace', 61: 'War', 62: 'War', 63: 'Peace', 64: 'Peace', 65: 'Peace', 66: 'War', 67: 'War', 68: 'War', 69: 'War', 70: 'War', 71: 'War', 72: 'Peace', 73: 'War', 74: 'War', 75: 'Peace', 76: 'War', 77: 'War', 78: 'Peace', 79: 'War', 80: 'War', 81: 'War', 82: 'Peace', 83: 'War', 84: 'Peace', 85: 'War', 86: 'War', 87: 'War', 88: 'Peace', 89: 'War', 90: 'War', 91: 'War', 92: 'Peace', 93: 'Peace', 94: 'War', 95: 'Peace', 96: 'War', 97: 'War', 98: 'War', 99: 'Peace'} #adversary choices are the same, regardless of "adversary type" so first adversary's first choice is always scissors.
    advice_choices = {0: 'Peace', 1: 'Peace', 2: 'Peace', 3: 'War', 4: 'War', 5: 'Peace', 6: 'Peace', 7: 'Peace', 8: 'War', 9: 'War', 10: 'War', 11: 'War', 12: 'War', 13: 'Peace', 14: 'Peace', 15: 'Peace', 16: 'War', 17: 'Peace', 18: 'War', 19: 'War', 20: 'War', 21: 'War', 22: 'War', 23: 'War', 24: 'Peace', 25: 'War', 26: 'Peace', 27: 'Peace', 28: 'Peace', 29: 'War', 30: 'Peace', 31: 'Peace', 32: 'War', 33: 'War', 34: 'Peace', 35: 'Peace', 36: 'War', 37: 'War', 38: 'War', 39: 'War', 40: 'War', 41: 'War', 42: 'War', 43: 'War', 44: 'Peace', 45: 'War', 46: 'Peace', 47: 'Peace', 48: 'Peace', 49: 'War', 50: 'Peace', 51: 'Peace', 52: 'Peace', 53: 'War', 54: 'Peace', 55: 'War', 56: 'Peace', 57: 'War', 58: 'Peace', 59: 'War', 60: 'Peace', 61: 'War', 62: 'War', 63: 'Peace', 64: 'Peace', 65: 'Peace', 66: 'War', 67: 'War', 68: 'War', 69: 'War', 70: 'War', 71: 'War', 72: 'Peace', 73: 'War', 74: 'War', 75: 'Peace', 76: 'War', 77: 'War', 78: 'Peace', 79: 'War', 80: 'War', 81: 'War', 82: 'Peace', 83: 'War', 84: 'Peace', 85: 'War', 86: 'War', 87: 'War', 88: 'Peace', 89: 'War', 90: 'War', 91: 'War', 92: 'Peace', 93: 'Peace', 94: 'War', 95: 'Peace', 96: 'War', 97: 'War', 98: 'War', 99: 'Peace'} #ai and human advice is the same, so clicking either advice button produces the same choice.  Will need to change this if advice button changes to "show" the advice instead of making the choice for the user
    
    

class Subsession(BaseSubsession):
#    def creating_session(self):
#        adv_choices = ['Human','AI']
#        for p in self.get_players():
#            p.participant.vars['RPS_played'] = "True"
#            if self.session.config['counterbalancing'] in (1,2):
#                # demo mode
#                p.first_adv = 'Human'
#            elif self.session.config['counterbalancing'] in (3,4):
#                p.first_adv = 'AI'
#            else:
#                # (randomizes)
#                p.first_adv = random.choice(adv_choices)
#                # need to find out if it creates unbalanced treatment groups
    pass

class Group(BaseGroup):
    pass


    
class Player(BasePlayer):
    first_adv = models.StringField( #order in which participant plays the adversaries
        choices=['Human','Human+AI','AI'],
        doc="""Participant's first adversary"""
    )

    second_adv = models.StringField( #order in which participant plays the adversaries
        choices=['Human','Human+AI','AI'],
        doc="""Participant's second adversary"""
    )
    third_adv = models.StringField( #order in which participant plays the adversaries
        choices=['Human','Human+AI','AI'],
        doc="""Participant's third adversary"""
    )
    first_adversary_id = models.StringField()
    second_adversary_id = models.StringField()
    third_adversary_id = models.StringField()
    adversary_id = models.StringField()
    def counterbalance_rps (self): #called only by the Inroduction page on round 1

        try: #if there's a participant label, use it for counterbalancing

            rps_counterbalance_digit = int(self.participant.label[-1]) #last digit of participant label is rps counterbalance digit.
        # a list 1-6 of orders to play the adversaries
        #1 - H,HAI,AI (123)
        #2 - H, AI, HAI (132)
        #3 - HAI, AI, H (231)
        #4 - HAI, H, AU (213)
        #5 - AI, H, HAI (312)
        #6 - AI, HAI, H (321)
        except: 
            # if thres no participant.label, use the default session.config variable
            rps_counterbalance_digit = int(self.session.config['rps_counterbalance'])
        
        if rps_counterbalance_digit == 1: #redundant with else
            self.participant.vars['rps_order'] = 123
            
        elif rps_counterbalance_digit == 2:
            self.participant.vars['rps_order'] = 132
    
        elif rps_counterbalance_digit == 3:
            self.participant.vars['rps_order'] = 231

  
        elif rps_counterbalance_digit == 4:
            self.participant.vars['rps_order'] = 213


        elif rps_counterbalance_digit == 5:
            self.participant.vars['rps_order'] = 312


        elif rps_counterbalance_digit == 6:
            self.participant.vars['rps_order'] = 321

        else:
            self.participant.vars['rps_order'] = 123
        
        rps_order_dict = {
            1: "Human",
            2: "Human+AI",
            3: "AI"
        }

        adv_dict = {
            1: "first_rps_adv",
            2: "second_rps_adv",
            3: "third_rps_adv"
        }
        
        for key, value in adv_dict.items():
            n = int(str(self.participant.vars['rps_order'])[key-1])
            self.participant.vars[value] = rps_order_dict[n]
            
        self.first_adv = self.participant.vars['first_rps_adv']
        self.second_adv = self.participant.vars['second_rps_adv']
        self.third_adv = self.participant.vars['third_rps_adv']
                
        id_dict = {
            "Human": "Player "+ Constants.human_adversary_id,
            "Human+AI": "Player "+ Constants.human_ai_adversary_id + " w/AI",
            "AI": "AI"
        }
        
        self.first_adversary_id = id_dict[str(self.first_adv)]
        self.second_adversary_id = id_dict[str(self.second_adv)]
        self.third_adversary_id = id_dict[str(self.third_adv)]


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
        choices=['Human','Human+AI','AI'],
        doc="""Adversary type""",
        widget=widgets.RadioSelect,
        #initial='human'
    )
    advisor_choice = models.StringField(
        choices=['human','AI','none'],

    )
    ######### end adversary #1
    
    ## remove this.
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
                

 
