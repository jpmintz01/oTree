from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return {
            'my_decision': me.decision,
            'opponent_decision': opponent.decision,
            'same_choice': me.decision == opponent.decision,
            'my_cumulative_payoff': sum([p.payoff for p in me.in_all_rounds()]),
            'his_cumulative_payoff': sum([q.payoff for q in opponent.in_all_rounds()]),

        }
    timeout_seconds = 100


class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return {
            'my_decision': me.decision,
            'opponent_decision': opponent.decision,
            'same_choice': me.decision == opponent.decision,
            'my_cumulative_payoff': sum([p.payoff for p in me.in_all_rounds()]),
            'his_cumulative_payoff': sum([q.payoff for q in opponent.in_all_rounds()]),

        }
    timeout_seconds = 100

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return {
            'my_decision': me.decision,
            'opponent_decision': opponent.decision,
            'same_choice': me.decision == opponent.decision,
            'my_cumulative_payoff': sum([p.payoff for p in me.in_all_rounds()]),
            'his_cumulative_payoff': sum([q.payoff for q in opponent.in_all_rounds()]),

        }



page_sequence = [
    Introduction,
    Decision,
    ResultsWaitPage,
    Results
]
