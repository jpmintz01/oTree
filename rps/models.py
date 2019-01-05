from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import string

author = 'Spear'

doc = """
This is a repeated advised Rock-Paper-Scissors game. 
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
    human_advisor_1_id = 'xpr1t'#''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    human_advisor_2_id = 'xpr1t'#''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    human_advisor_3_id = 'xpr1t'#''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    
    human_adversary_id = 'zcc75'#''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    human_ai_adversary_id = '8xe21'#''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    ai_adversary_id = 'tkf72'#''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars_player_id))
    
    #these choices may be artifacts if I'm controlling score and not inputs...
    adversary_choices = {0: 'Paper', 1: 'Scissors', 2: 'Paper', 3: 'Rock', 4: 'Scissors', 5: 'Scissors', 6: 'Rock', 7: 'Paper', 8: 'Paper', 9: 'Scissors', 10: 'Scissors', 11: 'Rock', 12: 'Scissors', 13: 'Paper', 14: 'Rock', 15: 'Scissors', 16: 'Rock', 17: 'Rock', 18: 'Rock', 19: 'Rock', 20: 'Scissors', 21: 'Paper', 22: 'Paper', 23: 'Rock', 24: 'Paper', 25: 'Scissors', 26: 'Scissors', 27: 'Paper', 28: 'Scissors', 29: 'Rock', 30: 'Rock', 31: 'Paper', 32: 'Rock', 33: 'Scissors', 34: 'Paper', 35: 'Paper', 36: 'Paper', 37: 'Paper', 38: 'Scissors', 39: 'Paper', 40: 'Rock', 41: 'Rock', 42: 'Paper', 43: 'Rock', 44: 'Paper', 45: 'Scissors', 46: 'Scissors', 47: 'Rock', 48: 'Paper', 49: 'Rock', 50: 'Scissors', 51: 'Rock', 52: 'Paper', 53: 'Paper', 54: 'Rock', 55: 'Rock', 56: 'Rock', 57: 'Rock', 58: 'Rock', 59: 'Scissors', 60: 'Paper', 61: 'Rock', 62: 'Paper', 63: 'Paper', 64: 'Rock', 65: 'Paper', 66: 'Rock', 67: 'Scissors', 68: 'Rock', 69: 'Paper', 70: 'Scissors', 71: 'Paper', 72: 'Paper', 73: 'Scissors', 74: 'Rock', 75: 'Paper', 76: 'Rock', 77: 'Scissors', 78: 'Paper', 79: 'Rock', 80: 'Scissors', 81: 'Scissors', 82: 'Paper', 83: 'Paper', 84: 'Scissors', 85: 'Paper', 86: 'Rock', 87: 'Scissors', 88: 'Scissors', 89: 'Scissors', 90: 'Rock', 91: 'Rock', 92: 'Scissors', 93: 'Scissors', 94: 'Rock', 95: 'Paper', 96: 'Paper', 97: 'Rock', 98: 'Rock', 99: 'Rock'} #adversary choices are the same, regardless of "adversary type" so first adversary's first choice is always scissors.
    advice_choices = {0: 'Paper', 1: 'Scissors', 2: 'Paper', 3: 'Rock', 4: 'Scissors', 5: 'Scissors', 6: 'Rock', 7: 'Paper', 8: 'Paper', 9: 'Scissors', 10: 'Scissors', 11: 'Rock', 12: 'Scissors', 13: 'Paper', 14: 'Rock', 15: 'Scissors', 16: 'Rock', 17: 'Rock', 18: 'Rock', 19: 'Rock', 20: 'Scissors', 21: 'Paper', 22: 'Paper', 23: 'Rock', 24: 'Paper', 25: 'Scissors', 26: 'Scissors', 27: 'Paper', 28: 'Scissors', 29: 'Rock', 30: 'Rock', 31: 'Paper', 32: 'Rock', 33: 'Scissors', 34: 'Paper', 35: 'Paper', 36: 'Paper', 37: 'Paper', 38: 'Scissors', 39: 'Paper', 40: 'Rock', 41: 'Rock', 42: 'Paper', 43: 'Rock', 44: 'Paper', 45: 'Scissors', 46: 'Scissors', 47: 'Rock', 48: 'Paper', 49: 'Rock', 50: 'Scissors', 51: 'Rock', 52: 'Paper', 53: 'Paper', 54: 'Rock', 55: 'Rock', 56: 'Rock', 57: 'Rock', 58: 'Rock', 59: 'Scissors', 60: 'Paper', 61: 'Rock', 62: 'Paper', 63: 'Paper', 64: 'Rock', 65: 'Paper', 66: 'Rock', 67: 'Scissors', 68: 'Rock', 69: 'Paper', 70: 'Scissors', 71: 'Paper', 72: 'Paper', 73: 'Scissors', 74: 'Rock', 75: 'Paper', 76: 'Rock', 77: 'Scissors', 78: 'Paper', 79: 'Rock', 80: 'Scissors', 81: 'Scissors', 82: 'Paper', 83: 'Paper', 84: 'Scissors', 85: 'Paper', 86: 'Rock', 87: 'Scissors', 88: 'Scissors', 89: 'Scissors', 90: 'Rock', 91: 'Rock', 92: 'Scissors', 93: 'Scissors', 94: 'Rock', 95: 'Paper', 96: 'Paper', 97: 'Rock', 98: 'Rock', 99: 'Rock'} #ai and human advice is the same, so clicking either advice button produces the same choice.  Will need to change this if advice button changes to "show" the advice instead of making the choice for the user
    
    

class Subsession(BaseSubsession):

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
            print("Counterbalance_rps didn't raise an exception.  self.participant.label:")
            print(self.participant.label)
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
            print("Counterbalance_rps raised an exception.  self.participant.label:")
        print("rps_counterbalance_digit: ")
        print(rps_counterbalance_digit)
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
#    player_guess_adv_1_type = models.StringField(
#        choices=['Simple Algorithm', 'Artificial Intelligence'],
#        label='What type of machine were you just playing with?',
#        widget=widgets.RadioSelect
#    )
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
    order_cb = models.IntegerField() #counterbalance order within rps (integer 1, 2, or 3 will indicate what "third" of the game the participant is in)
    
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
                

 
