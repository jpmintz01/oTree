from otree.api import Currency as c, currency_range
from otree.api import Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random



class PlayerBot(Bot):
    def play_now (self): #this function determines whether to play P-W this round, or after the participant plays RPS.  It returns True to pages.py (where it's called) if pages.py should display the pages for P-W and False if it shoudl skip them.
        
        try: #find out if they've already played RPS by checking participant.vars
            if self.participant.vars['RPS_played']: #why is this showing true?
                print("pw2 bot play_now part.vars: "+ str(self.participant.vars['RPS_played']))
                rps_played = True
            elif not self.participant.vars['RPS_played']:
                print('pw2 models play_now part.vars[RPS_played]')
                print(self.participant.vars['RPS_played'])
                rps_played = False
        except: #If no participant.vars, then set rps_played = false.
            rps_played = False
        print("rps_played: "+str(rps_played))
                    
        try: #find out the pw_order (first or second)
            if self.participant.vars['pw_order'] == 2:
                pw_first = False
            else: #if it's "1" then pw_first 
                pw_first = True
            print("pw_2first try: "+str(pw_first))
        except: #if there's no participant.vars, then check the session.config it to True
            try:
                if (self.session.config['pw_counterbalance'] == 2):
                    pw_first = False
                else:
                    pw_first = True
                print("pw_2first 2 try: "+str(pw_first))
            except:
                pw_first = True
                print("pw_2first except: "+str(pw_first))

        
        print("2not rps_played and pw_first: "+str(not (rps_played == pw_first)))
        print("2self.session.config['num_PW_Rounds']"+str(self.session.config['num_PW_rounds']))
        return not (rps_played == pw_first) # not(==) is XOR
    
    def play_round(self):
        choice_list = ["Peace","War"]
        print('pw2 bot self.player.play_now: ')
        print(self.play_now())
        if ((self.round_number <= 1) and (self.participant.vars['consent']) and self.play_now()):
            yield (pages.Introduction)
            yield Submission(pages.WaitForPlayers,{}, check_html=False)
        if ((self.round_number <= self.session.config['num_PW_rounds'])and (self.participant.vars['consent']) and self.play_now()): 
            
            yield Submission(pages.Decision, {'decision_vs_adv_1': random.choice(choice_list), 'decision_vs_adv_2': random.choice(choice_list), 'decision_vs_adv_3': random.choice(choice_list)}, check_html=False)
        if ((self.round_number == self.session.config['num_PW_rounds'])and (self.participant.vars['consent']) and self.play_now()):
            yield Submission(pages.Results, check_html=False)

