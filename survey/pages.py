from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

    
class Introduction(Page):
    def is_displayed(self):
        return self.participant.vars['consent']
    pass

#class Demographics(Page):
#    def is_displayed(self):
#        return self.participant.vars['consent']
#    form_model = 'player'
#    form_fields = ['age',
#                   'gender',
#                   'school',
#                   'service',
#                   'rank',
#                   'major',
#                   'minor',
#                   'post_grad',
#                  ]
#    def vars_for_template(self):
#        return {
#            'page_num': 1,
#        }

class Experience(Page):
    def is_displayed(self):
        return self.participant.vars['consent']
    form_model = 'player'
    form_fields = [#'years_military_experience',
                   #'game_theory_experience',
                   #'machine_learning_experience',
                   'experiment_contamination',
                   'attention_check'
                  ]
    def vars_for_template(self):
        return {
            'page_num': 1,
        }
#
#class Expectations(Page): 
#    def is_displayed(self):
#        return self.participant.vars['consent']
#    form_model = 'player'
#    form_fields = ['self_cooperativeness',
#                   'other_humans_cooperativeness',
#                   'computer_cooperativeness',
#                   'AI_cooperativeness',
#                  ]
#    def vars_for_template(self):
#        return {
#            'page_num': 3,
#        }
#    
#class GameIntro(Page):
#    pass
    

page_sequence = [
    Introduction,
    #Demographics,
    Experience,
#    Expectations,
#    GameIntro,
]
