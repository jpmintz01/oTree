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
    name_in_url = 'prisoner_nochat'
    players_per_group = None
    
    num_rounds = 6

    instructions_template = 'prisoner_nochat/Instructions.html'

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = c(3)
    betrayed_payoff = c(0)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(2)
    both_defect_payoff = c(1)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['adv_type'] = models.StringField(
                    choices=['human', 'AI'],
                    doc="""Adversary Type""",
                    widget=widgets.RadioSelect,
                    initial='human',
                )
                p.participant.vars['adv_type'] = 'AI'


class Group(BaseGroup):
    pass
    


class Player(BasePlayer):
    decision = models.StringField(
        choices=['Cooperate', 'Defect'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )

    adv_choice = models.StringField(
        choices=['Cooperate', 'Defect'],
        doc="""Adversary decision""",
        widget=widgets.RadioSelect
    )
    adv_payoff = models.CurrencyField(
        choices=currency_range(c(0), c(3), c(1)),
        initial=c(0)
    )
    #adv_type = models.StringField(
    #    choices=['human', 'AI'],
    #    doc="""Adversary Type""",
    #    widget=widgets.RadioSelect,
    #)
    
    #def other_player(self):
        #return self.get_others_in_group()[0]

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

        self.payoff = payoff_matrix[self.decision][self.adv_choice]#other_player().decision]
        self.adv_payoff = payoff_matrix[self.adv_choice][self.decision]
        #self.adv_payoff = payoff_matrix[self.adv_choice][self.decision] #adversary's scorre
