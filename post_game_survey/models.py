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
    number_of_pages = 5


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

#if self.session.configs['dev_game']:
#    self.participant.vars['consent'] = True
    
class Player(BasePlayer):
    
    prisoner_strategy = models.StringField(
        label='What was your strategy(ies) in the <b>Peace-War game</b>(i.e. "I always played Peace with the humans and War against the AI","I defected whenever the player defected in the last round," "I played essentially randomly because I did not really understand the game")',
        blank=True
    )
    play_different_prisoner = models.StringField(
        label='In the Peace-War game, why did you choose differently between players (if at all)?',
        blank=True
    )
#    chicken_strategy = models.StringField(
#        label='What was your betting strategy(ies) in the Chicken game?(i.e. "I bet on the human because he/she had something to lose.  The AI didn’t", "I bet on the AI because I thought it would know best.", "I bet essentially randomly because I did not really understand the game")'
#    )
#    play_different_chicken = models.StringField(
#        label='In the Chicken game, why did your strategy differ between players (if at all)?'
#    )
    rps_strategy = models.StringField(
        label='What was your strategy in the <b>Rock-Paper-Scissors game</b>? (i.e. "I always relied on the AI because it was best", "I chose myself because I did not trust either advisor", "I played essentially randomly because I did not really understand the game")',
        blank=True
    )
    play_different_rps = models.StringField(
        label='In the Rock-Paper-Scissors game, why did you choose the strategy you did?',
        blank=True
    )
    comments_AI_advisors = models.StringField(
        label='What comments do you have about your <b>AI ADVISOR</b>?',
        blank=True
    )
    comments_human_advisors = models.StringField(
        label='What comments do you have about your <b>human ADVISORS</b>?',
        blank=True
    )
    comments_human_players = models.StringField(
        label='What comments do you have about your <b>human competitors who did NOT have AI</b> to help them in the games?',
        blank=True
    )
    comments_human_AI_players = models.StringField(
        label='What comments do you have about your <b>human competitors who DID have AI</b> to help them in the games?',
        blank=True
    )
    comments_AI_players = models.StringField(
        label='What comments do you have about your <b>AI competitors</b> in the games?',
        blank=True
    )

    various_comments = models.StringField(
        label='Do you have any additional comments on what it was like to compete against both humans and artificial intelligence?',
        blank=True
    )
    
    age = models.IntegerField(
        label='In what year were you born?',
        min=1900, max=2015)

    gender = models.StringField(
        choices=['Male', 'Female', 'Other'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    service = models.StringField(
        choices=['Air Force', 'Army', 'Navy', 'Marine', 'Other'],
        label='What service are you a part of?',
        widget=widgets.RadioSelect)
    
    rank = models.StringField(label='What is your rank?')

    school = models.StringField(
        choices=['SOS', 'ACSC', 'SAASS', 'AWC', 'Other'],
        label='Which AU school are you attending?',
        widget=widgets.RadioSelect)
    
    years_military_experience = models.IntegerField(
        label='How many years of military experience do you have? (include time in a military academy or ROTC)',
        min=0, max=50)

    major = models.StringField(
        label='What was/is your undergraduate major? (list all separated by comma)',
        blank=True
    )

    minor = models.StringField(
        label='What was/is your undergraduate minor? (list all separated by comma, or "none")',
        blank=True
    )

    post_grad = models.StringField(
        label='What post-graduate degrees do you have? (list all separated by comma, or "none". Ex. MS in Computer Engineering, MA in Military and Strategic Studies, PhD in English Literature)',
        blank=True
    )

    #Add an "I have heard of the prisoner's dilemma before
    
    #add an "I have studied game theory before
    
    game_theory_experience = likert_var('On a scale of 1-5 with 1 being little to none, and 5 being "I understand terms such as Nash equilibria and Pareto Optimal", what level of understanding do you have with Game Theory or Prisoners Dilemma?' # I should change this to a "Test" like "which definition of pareto-optimal is most true
    )

    # add a few AI-related test questions
    # which computer language is most popular with machine learning developers Linux, C++, Python, HTML
    # which of the following have AI researchers or engineers? (DeepMind, Future of Life Institute, Future of Humanity Institute, )
    machine_learning_experience = likert_var('On a scale of 1-5 with 1 being little to none, and 5 being "I can code an AI using tensorflow", what level of understanding do you have with machine learning and/or artificial intelligence?' #
    )
    
    agree = models.BooleanField(
        label='Please select "Yes" to acknowledge you will not share information about or discuss this game with anyone until notified that it is ok to do so by the researcher.'
    )
    
    
