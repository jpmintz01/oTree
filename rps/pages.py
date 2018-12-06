from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

def counterbalance_adversary (self):
    self.player.counterbalance_rps()

    
def human_advisor_id (self):
    if self.round_number <= self.session.config['num_RPS_rounds']: #if during the first treatment section
        return Constants.human_advisor_1_id
    elif self.round_number <= (self.session.config['num_RPS_rounds']*2):#if during the second treatment section
        return Constants.human_advisor_2_id
    else: #if during the third treatment section
        return Constants.human_advisor_3_id


def adversary_id (self): #only need to call this once
    print("a11")
    counterbalance_adversary(self)
    if self.round_number <= self.session.config['num_RPS_rounds']:
        self.player.adversary_id = self.player.first_adversary_id
        print("self.player.first_adversary_id "+str(self.player.first_adversary_id))
        return self.player.first_adversary_id
    elif self.round_number <= (self.session.config['num_RPS_rounds']*2):
        self.player.adversary_id = self.player.second_adversary_id
        return self.player.second_adversary_id
        print("self.player.second_adversary_id "+str(self.player.second_adversary_id))
    else:
        self.player.adversary_id = self.player.third_adversary_id
        return self.player.third_adversary_id
        print("self.player.third_adversary_id   "+str(self.player.third_adversary_id))
    
    
    
def adversary_choice(self): #provides adversary's choice to the page BEFORE player's choice
    me = self.player
    choice_list = ['Rock','Paper','Scissors']
    me.decision_of_adv_1 = Constants.adversary_choices[self.round_number-1] #set the choice to the control
    
    
#    else: # this is the AI 'TFT
#        if me.round_number == 1: #
#            me.decision_of_adv_1 = random.choice(choice_list)
#        else:
#            if me.in_round(last_round).decision_vs_adv_1 == 'Rock':
#                me.decision_of_adv_1 = 'Paper' #beat his last move
#            elif me.in_round(last_round).decision_vs_adv_1 == 'Paper':
#                me.decision_of_adv_1 = 'Scissors'
#            else:
#                me.decision_of_adv_1 = 'Rock'


def ai_advice_adv_1(self): #actually used for both AI and human advice.
    me = self.player
    last_round = max(0, self.round_number-1)
#    if me.round_number == 1: #
#        return random.choice(['Rock','Paper','Scissors'])
#    else: 
#        if me.in_round(last_round).decision_vs_adv_1 == 'Rock':
#            return 'Paper' #beat his last move
#        elif me.in_round(last_round).decision_vs_adv_1 == 'Paper':
#            return 'Scissors'
#        else:
#            return 'Rock'
    return Constants.advice_choices[self.round_number-1]
    
    
class Introduction(Page):

    def is_displayed(self):
        self.participant.vars['RPS_played'] = True
        counterbalance_adversary (self)
        if (self.participant.vars['consent']): #if you have consent
            if (self.round_number == 1): #if the first treatment section
#                
                
                return True
            elif (self.round_number == (self.session.config['num_RPS_rounds']+1)): #if second treatment section
                
                return True
            elif (self.round_number == ((self.session.config['num_RPS_rounds']*2)+1)): #if third treatment section
                return True
            else:
                return False
        else: #if you don't have consent, skip this page
            return False
#                return (((self.round_number == 1) or (self.round_number == (self.session.config['num_RPS_rounds']+1)) or (self.round_number == ((self.session.config['num_RPS_rounds']*2)+1))) and (self.participant.vars['consent'])) #show the intro if it's round 1 or the first round of treatment 2 (the second half)
    
    def vars_for_template (self):

        return {
            'human_advisor_id': human_advisor_id(self),
            'adversary_id': adversary_id(self),
            'number_of_rounds': self.session.config['num_RPS_rounds']
        }
    
class WaitForPlayers(Page):
    def is_displayed(self):
        return (((self.round_number <= 1)  or (self.round_number == (self.session.config['num_RPS_rounds']+1)) or (self.round_number == ((self.session.config['num_RPS_rounds']*2)+1))) and (self.participant.vars['consent'])) #show the player match page if it's round 1 or the first round of treatment 2 (the second half)
        #need to change number of players based on whether two humans or one
    def vars_for_template (self):
        return {'adversary_id': adversary_id(self)}
   
        
class Decision(Page):
    def is_displayed(self):

        return ((self.round_number <= (self.session.config['num_RPS_rounds']*3)) and (self.participant.vars['consent'])) #show the decision page if still in rounds that are part of treatment 1 or 2 or 3
    
    form_model = 'player'
    def get_form_fields(self):
        fields = ['decision_vs_adv_1', 'decision_of_adv_1','advisor_choice']
        #fields = []
        #for i in (1, Constants.num_adversaries):
        #    fields.append('decision_vs_adv_{}'.format(i))
        #fields.append('advisor_choice')
        return fields
            #form_fields = ['decision_vs_adv_1', 'decision_vs_adv_2']
        
        #form_fields = ['decision_vs_adv_{}'.format(i) for i in range(1, Constants.num_adversaries)]
    def vars_for_template(self):
        me = self.player
        last_round = max(0, self.round_number-1)

        history = {}
        if not (self.session.config['control_RPS_score']): #this should be a boolean variable that is session-configurable to tell the function to return not a choice, but a number.  If this variable is false, then run the adversary_choice function
            adversary_choice(self); #provides the adversary's choice to the template (global function above)
                
        for p in me.in_all_rounds():
            history[p.round_number]=[p.decision_vs_adv_1, p.decision_of_adv_1, p.advisor_choice, p.winner]
        return {
            'control_RPS_score': self.session.config['control_RPS_score'],
            'target_RPS_score': self.session.config['target_RPS_score'],
            'human_advice_v_adv_1': ai_advice_adv_1(self),
            'AI_advice_v_adv_1': ai_advice_adv_1(self),
            'my_decision_adv_1': me.decision_vs_adv_1,
            'list_of_round_nums': [p.round_number for p in me.in_all_rounds()[:-1]],
            'my_decision_adv_1_total': [p.decision_vs_adv_1 for p in me.in_all_rounds()[:-1]],
            'adv_1_decision_total': [p.decision_of_adv_1 for p in me.in_all_rounds()[:-1]],
            'my_payoff_adv_1': me.payoff_vs_adv_1,
            'adv_1_decision': me.decision_of_adv_1,
            'adv_1_payoff': me.payoff_of_adv_1,
            #'my_total_payoff': me.round_payoff,
            'my_total_payoff': sum([p.round_payoff for p in me.in_all_rounds()]),
            'history_list': history,
            'human_advisor_id': human_advisor_id(self),
            'adversary_id': adversary_id(self),
           
        }
   
    #timeout_seconds = 100
                        
    def before_next_page(self):
        me = self.player
#        choice_list = ['Rock','Paper','Scissors']
#        if me.adv_1_type == 'human': #if adv = human
#            me.decision_of_adv_1 = random.choice(choice_list)#define human strategy (random choice)
#        else: # this is the AI 'TFT
#            if me.round_number == 1: #
#                me.decision_of_adv_1 = random.choice(choice_list)
#            else:
#                if me.in_round(last_round).decision_vs_adv_1 == 'Rock':
#                    me.decision_of_adv_1 = 'Paper' #beat his last move
#                elif me.in_round(last_round).decision_vs_adv_1 == 'Paper':
#                    me.decision_of_adv_1 = 'Scissors'
#                else:
#                    me.decision_of_adv_1 = 'Rock'
        me.set_payoff()
        
#class ResultsWaitPage(WaitPage):
#    def is_displayed(self):
#        return random.random() >= 0.9;
#    def sim_wait(self):
#        self.set_payoff()
    
#   def after_all_players_arrive(self):
#        for p in self.group.get_players():
#       self.set_payoff()


class Results(Page):
    def is_displayed(self):
        return ((self.round_number == ((self.session.config['num_RPS_rounds']*3)+1)) and (self.participant.vars['consent'])) #show the results if it's the last round and consent was given
    def vars_for_template(self):
        me = self.player
        #opponent = me.other_player()
        last_round = max(0,self.round_number-1)
        history = {}              
        for p in me.in_all_rounds():
            history[p.round_number]=[p.advisor_choice, p.decision_vs_adv_1, p.decision_of_adv_1, p.adversary_id,  p.winner]
        return {
#            'my_decision_adv_1_total': [p.decision_vs_adv_1 for p in me.in_all_rounds()],
#            'adv_1_decision_total': [p.decision_of_adv_1 for p in me.in_all_rounds()],
            'list_of_round_nums': [p.round_number for p in me.in_all_rounds()],
#            'my_decision_adv_1_total': [p.decision_vs_adv_1 for p in me.in_all_rounds()[:-1]],
#            'adv_1_decision_total': [p.decision_of_adv_1 for p in me.in_all_rounds()[:-1]],
            'my_total_payoff': sum([p.round_payoff for p in me.in_all_rounds()]),
            'history_list': history,

        }
#        self.player.participant_vars_dump = str(self.participant.vars)

        
class EndGame(Page):
    form_model = 'player'
    form_fields = ['player_guess_adv_1_type']    
    def is_displayed(self):
        return ((self.round_number == (self.session.config['num_RPS_rounds']*2)) and (self.participant.vars['consent']))
    
page_sequence = [
    Introduction,
    WaitForPlayers,
    Decision,
    #ResultsWaitPage,
    Results,
#    EndGame
]
