from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender',
                   'service',
                   'rank',
                   'major',
                   'minor',
                   'post_grad',
                  ]
    
class Experience(Page):
    form_model = 'player'
    form_fields = ['years_military_experience',
                   'game_theory_experience',
                   'machine_learning_experience',
                   'attention_check'
                  ]

class Expectations(Page): 
    form_model = 'player'
    form_fields = ['strategy_already',
                   'self_cooperativeness',
                   'other_humans_cooperativeness',
                   'computer_cooperativeness',
                   'AI_cooperativeness',
                  ]


page_sequence = [
    Demographics,
    Experience,
    Expectations
]
