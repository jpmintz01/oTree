from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

def adversary_choice(self):
    me = self.player
    choice_list = ['Rock','Paper','Scissors']
    #if me.adv_1_type == 'human': #if adv = human
        
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

def ai_advice_adv_1(self): #actually AI and human advice.
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
        return self.round_number == 1
    
class WaitForPlayers(Page):
    def is_displayed(self):
        return self.round_number <= 1
    pass
        
class Decision(Page):
    def is_displayed(self):
        return self.round_number <= self.session.config['num_rounds']
    
    form_model = 'player'
    def get_form_fields(self):
        fields = []
        for i in (1,Constants.num_adversaries):
            fields.append('decision_vs_adv_{}'.format(i))
        fields.append('advisor_choice')
        return fields
            #form_fields = ['decision_vs_adv_1', 'decision_vs_adv_2']
        
        #form_fields = ['decision_vs_adv_{}'.format(i) for i in range(1, Constants.num_adversaries)]
    def vars_for_template(self):
        me = self.player
        last_round = max(0, self.round_number-1)
 
    
                
        
        adversary_choice(self);
        history = {}
        for p in me.in_all_rounds():
            history[p.round_number]=[p.decision_vs_adv_1, p.decision_of_adv_1, p.advisor_choice, p.winner]
        return {
            'human_advice_v_adv_1': ai_advice_adv_1(self),
            'AI_advice_v_adv_1': ai_advice_adv_1(self),
            'my_decision_adv_1': me.decision_vs_adv_1,
            'list_of_round_nums': [p.round_number for p in me.in_all_rounds()[:-1]],
            'my_decision_adv_1_total': [p.decision_vs_adv_1 for p in me.in_all_rounds()[:-1]],
            'adv_1_decision_total': [p.decision_of_adv_1 for p in me.in_all_rounds()[:-1]],
            'my_payoff_adv_1': me.payoff_vs_adv_1,
            'adv_1_decision': me.decision_of_adv_1,
            'adv_1_payoff': me.payoff_of_adv_1,
            'my_total_payoff': me.round_payoff,
            'history_list': history,
            
           
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
        return self.round_number == self.session.config['num_rounds']
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
            
#            'my_decision_adv_2': me.decision_vs_adv_2,
#            'my_decision_adv_2_total': [p.decision_vs_adv_2 for p in me.in_all_rounds()],
#            'adv_2_decision_total': [p.decision_of_adv_2 for p in me.in_all_rounds()],
#            'my_payoff_adv_2': me.payoff_vs_adv_2,
#            'adv_2_decision': me.decision_of_adv_2,
#            'adv_2_payoff': me.payoff_of_adv_2,
            
            'my_total_payoff': sum([p.round_payoff for p in me.in_all_rounds()]),

        }
        self.player.participant_vars_dump = str(self.participant.vars)

        
class EndGame(Page):
    form_model = 'player'
    form_fields = ['player_guess_adv_1_type']    
    def is_displayed(self):
        return self.round_number == self.session.config['num_rounds']
    
page_sequence = [
    Introduction,
    WaitForPlayers,
    Decision,
    #ResultsWaitPage,
    Results,
    EndGame
]
