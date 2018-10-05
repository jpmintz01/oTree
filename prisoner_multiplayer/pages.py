from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Introduction(Page):
    def is_displayed(self):
        return self.round_number <= 1

        
class Decision(Page):
    def is_displayed(self):
        return self.round_number <= self.session.config['num_rounds']
    form_model = 'player'
    def get_form_fields(self):
        fields = []
        for i in (1, Constants.num_adversaries):
            fields.append('decision_vs_adv_{}'.format(i))
        return fields
            #form_fields = ['decision_vs_adv_1', 'decision_vs_adv_2']
        
        #form_fields = ['decision_vs_adv_{}'.format(i) for i in range(1, Constants.num_adversaries)]
    
    def vars_for_template(self):
        me = self.player
        
        last_round = max(0,self.round_number-1)
        return {
            'adv_1_DelayTime': str(random.randint(1,10)) + 's',
            'my_decision_adv_1': me.decision_vs_adv_1,
            'list_of_round_nums': [p.round_number for p in me.in_all_rounds()[:-1]],
            'my_decision_adv_1_total': [p.decision_vs_adv_1 for p in me.in_all_rounds()[:-1]],
            'adv_1_decision_total': [p.decision_of_adv_1 for p in me.in_all_rounds()[:-1]],
            'my_payoff_adv_1': me.payoff_vs_adv_1,
            'adv_1_decision': me.decision_of_adv_1,
            'adv_1_payoff': me.payoff_of_adv_1,
            
            'adv_2_DelayTime': str(random.randint(1,3)) + 's',
            'my_decision_adv_2': me.decision_vs_adv_2,
            'my_decision_adv_2_total': [p.decision_vs_adv_2 for p in me.in_all_rounds()[:-1]],
            'adv_2_decision_total': [p.decision_of_adv_2 for p in me.in_all_rounds()[:-1]],
            'my_payoff_adv_2': me.payoff_vs_adv_2,
            'adv_2_decision': me.decision_of_adv_2,
            'adv_2_payoff': me.payoff_of_adv_2,
            
            'my_total_payoff': me.round_payoff,
           
        }
   
    #timeout_seconds = 100
                        
    def before_next_page(self):
        last_round = max(1, self.round_number-1)
        me = self.player
        choice_list = ['Cooperate','Defect']
        if me.adv_1_type == 'human': #if adv = human
            me.decision_of_adv_1 = random.choice(choice_list)#define human strategy (random choice)
        else: # this is the AI 'TFT
            if me.round_number == 1: # cooperate in round one (can change)
                me.decision_of_adv_1 = 'Cooperate'
            else:
                if me.in_round(last_round).decision_vs_adv_1 == 'Defect': #no max arg needed because it's nested if that isn't round 1
                    me.decision_of_adv_1 = 'Defect' #if player defects, adv defects
                else:
                    me.decision_of_adv_1 = 'Cooperate'
                   
        if me.adv_2_type == 'human': #if adv = human
            me.decision_of_adv_1 = random.choice(choice_list)#define human strategy (random choice)
        else: # this is the AI 'TFT
            if me.round_number == 1: # cooperate in round one (can change)
                me.decision_of_adv_2 = 'Cooperate'
            else:
                if me.in_round(last_round).decision_vs_adv_2 == 'Defect': #no max arg needed because it's nested if that isn't round 1
                    me.decision_of_adv_2 = 'Defect' #if player defects, adv defects
                else:
                    me.decision_of_adv_2 = 'Cooperate'
                   

        me.set_payoff()
        
#class ResultsWaitPage(WaitPage):
    
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
            
            'my_decision_adv_2': me.decision_vs_adv_2,
            'my_decision_adv_2_total': [p.decision_vs_adv_2 for p in me.in_all_rounds()],
            'adv_2_decision_total': [p.decision_of_adv_2 for p in me.in_all_rounds()],
            'my_payoff_adv_2': me.payoff_vs_adv_2,
            'adv_2_decision': me.decision_of_adv_2,
            'adv_2_payoff': me.payoff_of_adv_2,
            
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
    Decision,
    #ResultsWaitPage,
    Results,
    EndGame
]
