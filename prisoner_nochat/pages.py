from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1
    form_model = 'player'
    #form_fields = ['adv_type']
    def vars_for_template(self):
        return {
            'my_adv_type': self.participant.vars['adv_type'],
        }
    timeout_seconds = 100



class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
    def vars_for_template(self):
        me = self.player
        #opponent = me.other_player()
        last_round = max(0,self.round_number-1)
        return {
            'my_decision': me.decision,
            #'opponent_decision': opponent.decision,
            #'same_choice': me.decision == opponent.decision,
            'my_cumulative_payoff': sum([p.payoff for p in me.in_all_rounds()]),
            'my_scores':[p.payoff for p in me.in_all_rounds()],
            'adv_score': [q.adv_payoff for q in me.in_all_rounds()],
            'adv_cumulative_payoff': sum([q.adv_payoff for q in me.in_all_rounds()]),
            'my_list_of_decisions': [p.decision for p in me.in_all_rounds()],
            'my_adversary': self.participant.vars['adv_type'],
            'last_round': last_round,
            'adv_decisions': [r.adv_choice for r in me.in_all_rounds()],
            'adv_choice': me.adv_choice,
            #'my_id_hash': (hash(self.participant.code) % 2),
        }
   
    #timeout_seconds = 100
    
    def before_next_page(self): 
        choice_list = ['Cooperate','Defect']
        if self.participant.vars['adv_type'] == 'human': #human adv picks a random choice
            self.player.adv_choice = random.choice(choice_list)
        else: # this is the AI 'TFT
            if self.player.round_number == 1:
                self.player.adv_choice = 'Cooperate'
            else:
                if self.player.in_round(self.round_number - 1).decision == 'Defect': 
                    self.player.adv_choice = 'Defect' #if player defects, adv defects
                else:
                    self.player.adv_choice = 'Cooperate'
            

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self): 
        for p in self.group.get_players():
          p.set_payoff()
    #timeout_seconds = random.randint(0,10) #not sure if this'll work


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def vars_for_template(self):
        me = self.player
        #opponent = me.other_player()
        last_round = max(0,self.round_number-1)
        return {
            'my_decision': me.decision,
            #'opponent_decision': opponent.decision,
            #'same_choice': me.decision == opponent.decision,
            'my_cumulative_payoff': sum([p.payoff for p in me.in_all_rounds()]),
            'my_scores':[p.payoff for p in me.in_all_rounds()],
            'adv_score': [q.adv_payoff for q in me.in_all_rounds()],
            'adv_cumulative_payoff': sum([q.adv_payoff for q in me.in_all_rounds()]),
            'my_list_of_decisions': [p.decision for p in me.in_all_rounds()],
            'my_adversary': self.participant.vars['adv_type'],
            'last_round': last_round,
            'adv_decisions': [r.adv_choice for r in me.in_all_rounds()],
            'adv_choice': me.adv_choice,
            #'my_id_hash': (hash(self.participant.code) % 2),
        }



page_sequence = [
    Introduction,
    Decision,
    ResultsWaitPage,
    Results
]
