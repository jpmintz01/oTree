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
    number_of_pages = 2


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
        label='What was your strategy(ies) in the Peace-War game(i.e. "I always played Peace with the humans and War against the AI","I defected whenever the player defected in the last round," "I played essentially randomly because I did not really understand the game")'
    )
    play_different_prisoner = models.StringField(
        label='In the Peace-War game, why did your choose differently between players (if at all)?'
    )
    chicken_strategy = models.StringField(
        label='What was your betting strategy(ies) in the Chicken game?(i.e. "I bet on the human because he/she had something to lose.  The AI didn’t", "I bet on the AI because I thought it would know best.", "I bet essentially randomly because I did not really understand the game")'
    )
    play_different_chicken = models.StringField(
        label='In the Chicken game, why did your strategy differ between players (if at all)?'
    )
    rps_strategy = models.StringField(
        label='What was your strategy in the Rock-Paper-Scissors game? (i.e. "I always relied on the AI because it was best", "I chose myself because I did not trust either advisor", "I played essentially randomly because I did not really understand the game")'
    )
    play_different_rps = models.StringField(
        label='In the Rock-Paper-Scissors game, why did you choose the strategy you did?'
    )
    comments_human_players = models.StringField(
        label='What comments do you have about the other human players who did not have AI to help them in the games?'
    )
    comments_human_advisors = models.StringField(
        label='What comments do you have about the other human advisors who did not have AI to help them in the games?'
    )
    comments_human_AI_players = models.StringField(
        label='What comments do you have about the other human players who had AI to help them in the games?'
    )
#    comments_human_AI_advisors = models.StringField(
#        label='What comments do you have about the other human advisors who had AI to help them in the games?'
#    )
    comments_AI_players = models.StringField(
        label='What comments do you have about the AI players in the games?'
    )
    comments_AI_advisors = models.StringField(
        label='What comments do you have about the AI advisors in the games?'
    )
    various_comments = models.StringField(
        label='Do you have any additional comments on what it was like to compete against both humans and artificial intelligence?'
    )
    agree = models.BooleanField(
        label='Please select "Yes" to acknowledge you will not share information about or discuss this game with anyone until notified that it is ok to do so by the researcher.'
    )
