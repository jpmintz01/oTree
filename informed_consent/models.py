from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Spear'

doc = """
Informed consent document
"""

#version 0.3

class Constants(BaseConstants):
    name_in_url = 'informed_consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    agree_to_participate = models.StringField()
    
    def set_counterbalance_on_participant_vars (self):
        try: #check if participant.label exists and has a counterbalance assigned to it
            play_first = any([self.participant.label.endswith("4"),self.participant.label.endswith("1")],)
            
            play_second = any([self.participant.label.endswith("2"), self.participant.label.endswith("3")])

            if (play_second): #if playing PW after RPS
                self.participant.vars['pw_order'] = 2
                print("self.participant.vars['pw_order']: " + str(self.participant.vars['pw_order']))
                
            else: #otherwise, play first
                self.participant.vars['pw_order'] = 1
                print("self.participant.vars['pw_order']: " + str(self.participant.vars['pw_order']))
        except: #if the participant label doesn't exist, then continue on to the next section to check session.config and participant.vars
            pass
        
    def consent_check (self):
        self.participant.vars['consent'] = True
