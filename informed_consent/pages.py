from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InformedConsent(Page):
    form_model = 'player'
    form_fields = ['agree_to_participate']
    def before_next_page (self):
        try:
            if (self.participant.label == None):
                self.participant.label = "dmo11"
        except:
            pass
        self.player.set_counterbalance_on_participant_vars() #check for counterbalancing on participant label and set participant.vars['pw_order'] and participant.vars['rps_order']
        if (self.player.agree_to_participate == "True"):
            self.participant.vars['consent'] = True
        else:
            self.participant.vars['consent'] = False

class Experience(Page):
    def is_displayed(self):
        return self.participant.vars['consent']
    form_model = 'player'
    form_fields = ['experiment_contamination',
                   'attention_check'
                  ]
    def vars_for_template(self): #is this needed or artifiact
        return {
            'page_num': 1,
        }

class Introduction(Page):
    def is_displayed(self):
        return self.participant.vars['consent']
    pass
#
page_sequence = [
    InformedConsent,
#    Experience,
    Introduction
]
