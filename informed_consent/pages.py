from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import string

def rand_part_label (self):
    num_chars = 5
    participant = ""
    for j in range (int(num_chars)-2):
        choice = random.choice(string.ascii_lowercase + string.digits)
        participant += choice

    participant += str(random.choice([1,2])) #adds random character 1-8 (app will select PW first or second based on whether this character is even or odd)      
    participant += str(random.choice([1,2,3,4,5,6])) #adds random character 1-6 (app will select which counterbalance of the RPS game based on this)
    return participant


class InformedConsent(Page):
    form_model = 'player'
    form_fields = ['agree_to_participate']
    def before_next_page (self):
        try:
            if (self.participant.label == None):
                self.participant.label = rand_part_label(self)
                print("informed_consent, Pages, InformedConsent, before_next_page, try, if" )
                print(self.participant.label)
        except:
            print("informed_consent, Pages, InformedConsent, before_next_page, try, except" )
            print(self.participant.label)
            pass
        self.player.set_counterbalance_on_participant_vars() #check for counterbalancing on participant label and set participant.vars['pw_order'] and participant.vars['rps_order']
        print ("informed_consent, Pages, InformedConsent, before_next_page - self.part.vars.pw_order")
        print(self.participant.vars['pw_order'])
        if (self.player.agree_to_participate == "True"):
            self.participant.vars['consent'] = True
        else:
            self.participant.vars['consent'] = False

class Experience(Page):
    def is_displayed(self):
        print('self.part.vars["consent"] '+ str(self.participant.vars['consent']))
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
        self.participant.vars['RPS_played'] = False
        self.participant.vars['show_PW_practice'] = True
        self.participant.vars['show_RPS_practice'] = True
#        print('inf consent intro set self.part.vars[RPS_played]' +str(self.participant.vars['RPS_played']))
#        print('self.part.vars["consent"] '+str(self.participant.vars['consent']))
        return self.participant.vars['consent']
    pass
#
page_sequence = [
    InformedConsent,
#    Experience,
    Introduction
]
