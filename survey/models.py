from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    instructions_template = 'survey/Instructions.html'
    number_of_pages = 3


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
        label='How many years of military experience do you have? (include time in a military academy)',
        min=0, max=50)

    major = models.StringField(
        label='What was/is your undergraduate major? (list all separated by comma)',
    )

    minor = models.StringField(
        label='What was/is your undergraduate minor? (list all separated by comma, or "none")',
    )

    post_grad = models.StringField(
        label='What post-graduate degrees do you have? (list all separated by comma, or "none". Ex. MS in Computer Engineering, MA in Military and Strategic Studies, PhD in English Literature)',
    )

    game_theory_experience = likert_var('On a scale of 1-5 with 1 being little to none, and 5 being "I understand terms such as Nash equilibria and Pareto Optimal", what level of understanding do you have with Game Theory or Prisoners Dilemma?')

    machine_learning_experience = likert_var('On a scale of 1-5 with 1 being little to none, and 5 being "I can code an AI using tensorflow", what level of understanding do you have with machine learning and/or artificial intelligence?')


    # Should i make these likert variables for each type of player?
    self_cooperativeness = likert_var('On a scale of 1-5 with 1 being not cooperative, and 5 being highly cooperative, how do you expect yourself to behave during this game?'
                                     )

    other_humans_cooperativeness = likert_var('On a scale of 1-5 with 1 being not cooperative, and 5 being highly cooperative, how do you expect "other human players" to behave during this game?'
                                             ) 

    computer_cooperativeness = likert_var('On a scale of 1-5 with 1 being not cooperative, and 5 being highly cooperative, how do you expect "the computer" to behave during this game?'
                                         ) 

    AI_cooperativeness = likert_var('On a scale of 1-5 with 1 being not cooperative, and 5 being highly cooperative, how do you expect "the AI" to behave during this game?'
                                   ) 
    
    attention_check = models.StringField(
        choices=['Texas', 'Austria', 'Tennessee', 'Georgia', 'Other'],
        label='What state is Atlanta in?',
        widget=widgets.RadioSelect)

