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
    instructions_template = 'informed_consent/Instructions.html'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass
#
#def counterbalance_rps (self):
#    # a list 1-6 of orders to play the adversaries
#    #1 - H,HAI,AI (123)
#    #2 - H, AI, HAI (132)
#    #3 - HAI, AI, H (231)
#    #4 - HAI, H, AU (213)
#    #5 - AI, H, HAI (312)
#    #6 - AI, HAI, H (321)
#    try: #if there's a participant label, use it for counterbalancing
#        
#        rps_counterbalance_digit = int(self.participant.label[-1])
#        
#        if rps_counterbalance_digit == 1: #redundant with else
#            self.participant.vars['rps_order'] = 123 
#        elif rps_counterbalance_digit == 2:
#            self.participant.vars['rps_order'] = 132
#        elif rps_counterbalance_digit == 3:
#            self.participant.vars['rps_order'] = 231
#        elif rps_counterbalance_digit == 4:
#            self.participant.vars['rps_order'] = 213
#        elif rps_counterbalance_digit == 5:
#            self.participant.vars['rps_order'] = 312
#        elif rps_counterbalance_digit == 6:
#            self.participant.vars['rps_order'] = 321
#        #else:
#            #self.participant.vars['rps_order'] = 123
#    except: #if nthere's no partcipant label, use session.config
#        #maybe move this to rps models.py
#
#        if self.session.config['rps_counterbalance'] == 1:#redundant with else
#            self.participant.vars['rps_order'] = 123
#        elif self.session.config['rps_counterbalance'] ==2:
#            self.participant.vars['rps_order'] = 132
#        elif self.session.config['rps_counterbalance'] ==3:
#            self.participant.vars['rps_order'] = 231
#        elif self.session.config['rps_counterbalance'] ==4:
#            self.participant.vars['rps_order'] = 213
#        elif self.session.config['rps_counterbalance'] ==5:
#            self.participant.vars['rps_order'] = 312
#        elif self.session.config['rps_counterbalance'] ==6:
#            self.participant.vars['rps_order'] = 321
#        #else:
#           # self.participant.vars['rps_order'] = 123
#    print("1self.participant.vars['rps_order']= ")
#    print(self.participant.vars['rps_order'])
    
class Player(BasePlayer):
    agree_to_participate = models.StringField()
    

                
    def set_counterbalance_on_participant_vars (self):
        try: #check if participant.label exists and has a counterbalance assigned to it
            if ((int(self.participant.label[-2])%2)==0): #if the second to last digit of the participant.label is even
                self.participant.vars['pw_order'] = 2
#                counterbalance_rps(self)#sets. self.participant.vars['rps_order']
            else:
                self.participant.vars['pw_order'] = 1
#                counterbalance_rps(self)#sets. self.participant.vars['rps_order']
#            
#            play_first = any([self.participant.label.endswith("4"),self.participant.label.endswith("1")],)
#            
#            play_second = any([self.participant.label.endswith("2"), self.participant.label.endswith("3")])
#
#            if (play_second): #if playing PW after RPS
#                self.participant.vars['pw_order'] = 2
#                print("self.participant.vars['pw_order']: " + str(self.participant.vars['pw_order']))
#                
#            else: #otherwise, play first
#                self.participant.vars['pw_order'] = 1
#                print("self.participant.vars['pw_order']: " + str(self.participant.vars['pw_order']))
        except: #if the participant label doesn't exist, then continue on to the next section to check session.config and participant.vars
            if ((int(self.session.config['pw_counterbalance'])%2)==0): #if the second to last digit of the participant.label is even
                self.participant.vars['pw_order'] = 2
#                counterbalance_rps(self) #sets. self.participant.vars['rps_order']
                # fix this.  Make an 
            else:
                self.participant.vars['pw_order'] = 1
#                counterbalance_rps(self)#sets. self.participant.vars['rps_order']
        
    def consent_check (self):
        self.participant.vars['consent'] = True
        
 
    experiment_contamination = models.StringField(
        label='What have you heard about this experiment from other participants, if anything? If nothing, write "nothing" or leave this field blank.',
        blank=True)
    
    attention_check = models.StringField(
        choices=['Texas', 'Austria', 'Tennessee', 'Georgia', 'Other'],
        label='What state is Atlanta in?',
        widget=widgets.RadioSelect)
    

