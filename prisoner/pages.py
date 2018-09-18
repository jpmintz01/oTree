from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
#from otree.chat import chat_template_tag



class Introduction(Page):
    timeout_seconds = 100


class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

#    def vars_for_template(self):
#        me = self.player
#        opponent = me.other_player()
#        context = template(self)
#        return {
#            'vars_from_django': template(context),
#            'socket_path': template().socket_path,
#            'channel': template.channel,
#            'participant_id': template.partcipant_id,
#            'nickname_signed': template.nickname_signed,
#            'nickname_i_see_for_myself': template.nickname_i_see_for_myself,
#        }

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
        }


page_sequence = [
    Introduction,
    Decision,
    ResultsWaitPage,
    Results
]
