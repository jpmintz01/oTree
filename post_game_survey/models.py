from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Spear'

doc = """
An electronic example of the questions in the post-game questionnaire/interview
"""


class Constants(BaseConstants):
    name_in_url = 'post_game_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def likert_var(label):
    return models.IntegerField(
        choices=[1,2,3,4,5],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

class Player(BasePlayer):
    prisoner_strategy = models.StringField(
        label='What was your strategy(ies) in the Prisoners Dilemma game? (i.e. "I defected whenever the player defected in the last round," "I played essentially randomly because I did not really understand the game")'
    )
    play_different_prisoner = models.StringField(
        label='In the Prisoners Dilemma game, how did your strategy differ when competing with the human versus the artificial players (if at all)?'
    )
    chicken_strategy = models.StringField(
        label='What was your strategy(ies) in the Chicken game?(i.e. "I swerved every time because it reduced my risk of dying," "I played essentially randomly because I did not really understand the game")'
    )
    play_different_chicken = models.StringField(
        label='In the Chicken game, how did your strategy differ when competing with the human versus the artificial players (if at all)?'
    )
    various_comments = models.StringField(
        label='Do you have any additional comments on what it was like to compete against both humans and artificial intelligence?'
    )
    agree = models.BooleanField(
        label='Please select "Yes" to acknowledge you will not share information about or discuss this game with anyone until notified that it is ok to do so by the researcher.'
    )
