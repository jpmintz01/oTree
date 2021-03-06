from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

#version 0.2.9

def adversary_choice(self): # function for the adversary (and advisor) choices.  called by instances of the page class - see below
    me = self.player
    last_round = max(1, self.round_number-1)
    choice_list = ['Peace','War']
    me.decision_of_adv_1 = Constants.human_choices[self.round_number-1] #minus 1 since dictionary starts with zero
    me.decision_of_adv_2 = Constants.human_ai_choices[self.round_number-1]
    me.decision_of_adv_3 = Constants.ai_choices[self.round_number-1] 
#    if ((me.adv_1_type == 'human') or (me.adv_1_type == 'human+AI')): #if adv = human
#        me.decision_of_adv_1 = random.choice(choice_list)#define human strategy (random choice)
#    else: # this is the AI 'TFT
#        if me.round_number == 1: # Peace in round one (can change)
#            me.decision_of_adv_1 = 'Peace'
#        else:
#            if me.in_round(last_round).decision_vs_adv_1 == 'War': #no max arg needed because it's nested if that isn't round 1
#                me.decision_of_adv_1 = 'War' #if player Wars, adv Wars
#            else:
#                me.decision_of_adv_1 = 'Peace'
#
#
#    if ((me.adv_2_type == 'human') or (me.adv_2_type == 'human+AI')): #if adv = human
#        me.decision_of_adv_2 = random.choice(choice_list)#define human strategy (random choice)
#    else: # this is the AI 'TFT
#        if me.round_number == 1: # Peace in round one (can change)
#            me.decision_of_adv_2 = 'Peace'
#        else:
#            if me.in_round(last_round).decision_vs_adv_2 == 'War': #no max arg needed because it's nested if that isn't round 1
#                me.decision_of_adv_2 = 'War' #if player Wars, adv Wars
#            else:
#                me.decision_of_adv_2 = 'Peace'
#
#    if ((me.adv_3_type == 'human') or (me.adv_3_type == 'human+AI')): #if adv = human
#        me.decision_of_adv_3 = random.choice(choice_list)#define human strategy (random choice)
#    else: # this is the AI 'TFT
#        if me.round_number == 1: # Peace in round one (can change)
#            me.decision_of_adv_3 = 'Peace'
#        else:
#            if me.in_round(last_round).decision_vs_adv_3 == 'War': #no max arg needed because it's nested if that isn't round 1
#                me.decision_of_adv_3 = 'War' #if player Wars, adv Wars
#            else:
#                me.decision_of_adv_3 = 'Peace'

    
    
class Introduction(Page):
    
    def is_displayed(self): #determines whether this is shown or not - only shows in round 1 AND if player has consented (session variable is set in informed consent). overrides Subsession.creating_session when applicable (demo vs production)
        
        return ((self.round_number <= 1) and (self.participant.vars['consent']) and self.player.play_now())#returns True if I want to show the page


class Practice(Page):
    def is_displayed(self):
        return ((self.round_number <= 1) and (self.participant.vars['consent']) and self.player.play_now() and self.participant.vars['show_PW_practice'])
    def vars_for_template(self):
        me = self.player
        history_adv_1 = {}
        history_adv_2 = {}
        history_adv_3 = {}
        last_round = max(0,self.round_number-1)
        return {
            'adv_1_DelayTime': str(random.randint(1,10)) + 's',
            'adv_2_DelayTime': str(random.randint(1,10)) + 's',
            'adv_3_DelayTime': str(random.randint(1,3)) + 's',
#            'my_decision_adv_1': me.decision_vs_adv_1,
#            'my_decision_adv_2': me.decision_vs_adv_2,
#            'my_decision_adv_3': me.decision_vs_adv_3,
            'adv_1_decision': me.decision_of_adv_1,
            'adv_2_decision': me.decision_of_adv_2,
            'adv_3_decision': me.decision_of_adv_3,
            'total_payoff_v_adv_1': sum([p.payoff_vs_adv_1 for p in me.in_all_rounds()]),
            'total_payoff_v_adv_2': sum([p.payoff_vs_adv_2 for p in me.in_all_rounds()]),
            'total_payoff_v_adv_3': sum([p.payoff_vs_adv_3 for p in me.in_all_rounds()]),
            'history_w_adv_1': history_adv_1,
            'history_w_adv_2': history_adv_2,
            'history_w_adv_3': history_adv_3,
            'payoff_of_adv_1': sum([p.payoff_of_adv_1 for p in me.in_all_rounds()]),
            'payoff_of_adv_2': sum([p.payoff_of_adv_2 for p in me.in_all_rounds()]),
            'payoff_of_adv_3': sum([p.payoff_of_adv_3 for p in me.in_all_rounds()]),
#            'total_payoff_of_adv_1': 
            
#            'list_of_round_nums': [p.round_number for p in me.in_all_rounds()[:-1]],
#            'my_decision_adv_1_total': [p.decision_vs_adv_1 for p in me.in_all_rounds()[:-1]],
#            'adv_1_decision_total': [p.decision_of_adv_1 for p in me.in_all_rounds()[:-1]],
#            'my_payoff_adv_1': me.payoff_vs_adv_1,
#            'adv_1_decision': me.decision_of_adv_1,
#            'adv_1_payoff': me.payoff_of_adv_1,
#
#            'my_decision_adv_2_total': [p.decision_vs_adv_2 for p in me.in_all_rounds()[:-1]],
#            'adv_2_decision_total': [p.decision_of_adv_2 for p in me.in_all_rounds()[:-1]],
#            'my_payoff_adv_2': me.payoff_vs_adv_2,
#            'adv_2_payoff': me.payoff_of_adv_2,
            'my_total_payoff': sum([p.round_payoff for p in me.in_all_rounds()]),
        }
    
class WaitForPlayers(Page):
    def is_displayed(self): #only shows in round 1 AND if player has consented (session variable is set in informed consent)
        if ((self.round_number <= 1) and (self.participant.vars['consent']) and self.player.play_now()):
            self.participant.vars['show_PW_practice'] = False
        return ((self.round_number <= 1)and (self.participant.vars['consent']) and self.player.play_now()) #returns True if I want to show the page
    pass
    
    
class Decision(Page):
    def is_displayed(self):
#        print("Dself.round_number "+str(self.round_number))
#        print("Dself.session.config['num_PW_rounds'] "+str(self.session.config['num_PW_rounds']))
#        print("Dself.participant.vars['consent'] "+str(self.participant.vars['consent']))
#        print("Dself.player.play_now()) "+str(self.player.play_now()))
#        print("DConstants.num_rounds "+str(Constants.num_rounds))
        return ((self.round_number <= self.session.config['num_PW_rounds'])and (self.participant.vars['consent']) and self.player.play_now())
    form_model = 'player'
#    def get_form_fields(self):
#        fields = []
#        for i in (1, Constants.num_adversaries):
#            fields.append('decision_vs_adv_{}'.format(i))
#        return fields
    form_fields = ['decision_vs_adv_1', 'decision_vs_adv_2', 'decision_vs_adv_3']
        
        #form_fields = ['decision_vs_adv_{}'.format(i) for i in range(1, Constants.num_adversaries)]
    
    def vars_for_template(self):
        me = self.player
        adversary_choice(self)
        last_round = max(0,self.round_number-1)
        history_adv_1 = {}
        history_adv_2 = {}
        history_adv_3 = {}
            
        for p in me.in_all_rounds():
            history_adv_1[p.round_number]=[p.decision_vs_adv_1, p.payoff_vs_adv_1, p.decision_of_adv_1, p.payoff_of_adv_1]
            history_adv_2[p.round_number]=[p.decision_vs_adv_2, p.payoff_vs_adv_2, p.decision_of_adv_2, p.payoff_of_adv_2]
            history_adv_3[p.round_number]=[p.decision_vs_adv_3, p.payoff_vs_adv_3, p.decision_of_adv_3, p.payoff_of_adv_3]
            
        return {
            'adv_1_DelayTime': str(random.randint(1,10)) + 's',
            'adv_2_DelayTime': str(random.randint(1,10)) + 's',
            'adv_3_DelayTime': str(random.randint(1,3)) + 's',
#            'my_decision_adv_1': me.decision_vs_adv_1,
#            'my_decision_adv_2': me.decision_vs_adv_2,
#            'my_decision_adv_3': me.decision_vs_adv_3,
            'adv_1_decision': me.decision_of_adv_1,
            'adv_2_decision': me.decision_of_adv_2,
            'adv_3_decision': me.decision_of_adv_3,
            'total_payoff_v_adv_1': sum([p.payoff_vs_adv_1 for p in me.in_all_rounds()]),
            'total_payoff_v_adv_2': sum([p.payoff_vs_adv_2 for p in me.in_all_rounds()]),
            'total_payoff_v_adv_3': sum([p.payoff_vs_adv_3 for p in me.in_all_rounds()]),
            'history_w_adv_1': history_adv_1,
            'history_w_adv_2': history_adv_2,
            'history_w_adv_3': history_adv_3,
            'payoff_of_adv_1': sum([p.payoff_of_adv_1 for p in me.in_all_rounds()]),
            'payoff_of_adv_2': sum([p.payoff_of_adv_2 for p in me.in_all_rounds()]),
            'payoff_of_adv_3': sum([p.payoff_of_adv_3 for p in me.in_all_rounds()]),
#            'total_payoff_of_adv_1': 
            
#            'list_of_round_nums': [p.round_number for p in me.in_all_rounds()[:-1]],
#            'my_decision_adv_1_total': [p.decision_vs_adv_1 for p in me.in_all_rounds()[:-1]],
#            'adv_1_decision_total': [p.decision_of_adv_1 for p in me.in_all_rounds()[:-1]],
#            'my_payoff_adv_1': me.payoff_vs_adv_1,
#            'adv_1_decision': me.decision_of_adv_1,
#            'adv_1_payoff': me.payoff_of_adv_1,
#
#            'my_decision_adv_2_total': [p.decision_vs_adv_2 for p in me.in_all_rounds()[:-1]],
#            'adv_2_decision_total': [p.decision_of_adv_2 for p in me.in_all_rounds()[:-1]],
#            'my_payoff_adv_2': me.payoff_vs_adv_2,
#            'adv_2_payoff': me.payoff_of_adv_2,
            'my_total_payoff': sum([p.round_payoff for p in me.in_all_rounds()]),
#            'my_total_payoff': sum([me.round_payoff]),
           
        }
   
    #timeout_seconds = 100
                        
    def before_next_page(self):
        me = self.player
#        print("before_next_page")
#        print("round_number "+str(me.round_number))
        me.set_payoff()
        
class ResultsWaitPage(WaitPage):
    pass
#    def sim_wait(self):
#        self.set_payoff()
    
#   def after_all_players_arrive(self):
#        for p in self.group.get_players():
#       self.set_payoff()


class Results(Page):
    def is_displayed(self):
        return ((self.round_number == self.session.config['num_PW_rounds'])and (self.participant.vars['consent']) and self.player.play_now())
    def vars_for_template(self):
        me = self.player
        #opponent = me.other_player()
        last_round = max(0,self.round_number-1)
        return {
            'my_decision_adv_1': me.decision_vs_adv_1,
            'list_of_round_nums': [p.round_number for p in me.in_all_rounds()],
            'my_decision_adv_1_total': [p.decision_vs_adv_1 for p in me.in_all_rounds()],
            'adv_1_decision_total': [p.decision_of_adv_1 for p in me.in_all_rounds()],
            'my_payoff_adv_1': me.payoff_vs_adv_1,
            'adv_1_decision': me.decision_of_adv_1,
            'adv_1_payoff': me.payoff_of_adv_1,
            
            'my_decision_adv_2': me.decision_vs_adv_2,
            'my_decision_adv_2_total': [p.decision_vs_adv_2 for p in me.in_all_rounds()],
            'adv_2_decision_total': [p.decision_of_adv_2 for p in me.in_all_rounds()],
            'my_payoff_adv_2': me.payoff_vs_adv_2,
            'adv_2_decision': me.decision_of_adv_2,
            'adv_2_payoff': me.payoff_of_adv_2,
            
            'my_decision_adv_3': me.decision_vs_adv_3,
            'my_decision_adv_3_total': [p.decision_vs_adv_3 for p in me.in_all_rounds()],
            'adv_3_decision_total': [p.decision_of_adv_3 for p in me.in_all_rounds()],
            'my_payoff_adv_3': me.payoff_vs_adv_3,
            'adv_3_decision': me.decision_of_adv_3,
            'adv_3_payoff': me.payoff_of_adv_3,
            
            'my_total_payoff': sum([p.round_payoff for p in me.in_all_rounds()]),

        }
        self.player.participant_vars_dump = str(self.participant.vars)
        
class EndGame(Page):
    
    form_model = 'player'
    form_fields = ['player_guess_adv_1_type']
    def is_displayed(self):
        return ((self.round_number == self.session.config['num_PW_rounds'])and (self.participant.vars['consent']) and self.player.play_now())
    
page_sequence = [
    Introduction,
    Practice,
    WaitForPlayers,
    Decision,
#    ResultsWaitPage,
    Results,
#    EndGame
]
