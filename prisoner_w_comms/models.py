from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


doc = """
This is a one-shot "Prisoner's Dilemma with comminications allowed. Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner_w_comms'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'prisoner_w_comms/Instructions.html'

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = c(300)
    betrayed_payoff = c(0)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(200)
    both_defect_payoff = c(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(
        choices=['Cooperate', 'Defect'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )

    player_chat_choice = models.StringField(
        choices=['Do as I say, or I’ll punish you.','I accept your last proposal.','I don’t accept your proposal.','That’s not fair.','I don’t trust you.','Excellent!','Sweet. We are geTng rich.','Give me another chance.','Okay. I forgive you.','I’m changing my strategy.','We can both do better than this.','Curse you.','You betrayed me.','You will pay for this!','In your face!','Let’s always play <action pair>.','This round, let’s play <action pair>.','Don’t play <action>.','Let’s alterna=ve between <action pair> and <action pair>.'])
    

    
    def other_player(self):
        return self.get_others_in_group()[0]

    adv_chat_choice = models.StringField(
        choices=['Do as I say, or I’ll punish you.','I accept your last proposal.','I don’t accept your proposal.','That’s not fair.','I don’t trust you.','Excellent!','Sweet. We are geTng rich.','Give me another chance.','Okay. I forgive you.','I’m changing my strategy.','We can both do better than this.','Curse you.','You betrayed me.','You will pay for this!','In your face!','Let’s always play <action pair>.','This round, let’s play <action pair>.','Don’t play <action>.','Let’s alterna=ve between <action pair> and <action pair>.'])
    
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