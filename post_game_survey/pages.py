from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class PlayExperience(Page):
    form_model = 'player'
    form_fields = [
        'prisoner_strategy',
        'play_different_prisoner',
        'chicken_strategy',
        'play_different_chicken',
        'rps_strategy',
        'play_different_rps'
    ]
    def vars_for_template(self):
        return {
            'page_num': 1,
        }

class Comments(Page):
    form_model = 'player'
    form_fields = [
        'comments_human_players',
        'comments_human_advisors',
        'comments_human_AI_players',
        'comments_AI_players',
        'comments_AI_advisors',
        'various_comments'
    ]    
    def vars_for_template(self):
        return {
            'page_num': 2,
        }

class Debrief(Page):
    form_model = 'player'
    form_fields = ['agree']

    


page_sequence = [
    PlayExperience, 
    Comments,
    Debrief
]
