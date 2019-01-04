from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class PlayExperience(Page):
    def is_displayed(self):
        return (self.participant.vars['consent'])
    form_model = 'player'
    form_fields = [
        'prisoner_strategy',
#        'play_different_prisoner',
        'rps_strategy',
#        'play_different_rps'
    ]
    def vars_for_template(self):
        return {
            'page_num': 1,
        }

class Comments(Page):
    def is_displayed(self):
        return (self.participant.vars['consent'])
    form_model = 'player'
    form_fields = [
        'comments_human_advisors',
        'comments_AI_advisors',
        'comments_human_players',
        'comments_human_AI_players',
        'comments_AI_players',
        'various_comments'
    ]    
    def vars_for_template(self):
        return {
            'page_num': 2,
        }

class Demographics(Page):
    def is_displayed(self):
        return self.participant.vars['consent']
    form_model = 'player'
    form_fields = ['age',
                   'gender',
                   'school',
                   'service',
                   'rank',
                   'major',
#                   'minor',
                   'post_grad',
                  ]
    def vars_for_template(self):
        return {
            'page_num': 3,
        }

class Experience(Page):
    def is_displayed(self):
        return self.participant.vars['consent']
    form_model = 'player'
    form_fields = ['years_military_experience',
                   'game_theory_experience',
                   'machine_learning_experience',
                   'attention_check',
                   'experiment_contamination'
                  ]
    def vars_for_template(self):
        return {
            'page_num': 4,
        }
#

class Debrief(Page):
    def is_displayed(self):
        self.player.self_participant_vars_dump = str(self.participant.vars)
#        self_session_dump = self.sesssion.
        return (self.participant.vars['consent'])
    
    form_model = 'player'
    form_fields = ['agree']

page_sequence = [
    PlayExperience, 
    Comments,
    Demographics,
    Experience,
    Debrief
]
