from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Experience(Page):
    form_model = 'player'
    form_fields = [
        'prisoner_strategy',
        'play_different_prisoner',
        'chicken_strategy',
        'play_different_chicken',
        'various_comments'
    ]

class Debrief(Page):
    form_model = 'player'
    form_fields = ['agree']

    


page_sequence = [Experience, Debrief]
