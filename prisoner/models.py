from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner'
    players_per_group = 2
    num_rounds = 100 #needs to be set higher than self.session.config['num_rounds']

    instructions_template = 'prisoner/Instructions.html'

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = c(300)
    betrayed_payoff = c(-100)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(200)
    both_defect_payoff = c(-50)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

        
    player_guess_adv_1_type = models.StringField(
        choices=['Simple Algorithm', 'Artificial Intelligence'],
        label='What type of machine were you just playing with?',
        widget=widgets.RadioSelect
    )

    decision = models.StringField(
        choices=['Cooperate', 'Defect'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):

        payoff_matrix = {
            'Cooperate':
                {
                    'Cooperate': Constants.both_cooperate_payoff,
                    'Defect': Constants.betrayed_payoff
                },
            'Defect':
                {
                    'Cooperate': Constants.betray_payoff,
                    'Defect': Constants.both_defect_payoff
                }
        }

        self.payoff = payoff_matrix[self.decision][self.other_player().decision]