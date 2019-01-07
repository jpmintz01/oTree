from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
 
    def play_round(self):
    
        yield (pages.PlayExperience, {'prisoner_strategy': "Peace-War strategy", 'rps_strategy': "RPS Strategy"})
        yield (pages.Comments, {'comments_human_advisors': "Comments on human advisors",'comments_AI_advisors': "Comments on AI advisors",'comments_human_players': "Comments on human players",'comments_human_AI_players': "comments on AI-Assistend Human plauers", 'comments_AI_players': "Comments on AI Players", 'various_comments': "Various Comments"})
        yield (pages.Demographics, {'age': "1901",'gender': "Other", 'school': "SOS", 'service': "Other",'rank': "My Rank", 'major': "Undergrad Major", 'post_grad': "Post-Grad degrees" })
        yield (pages.Experience, {    'years_military_experience': 50,                   'game_theory_experience': "2-Basic understanding", 'machine_learning_experience': "3-Knowledgeable (I can describe the strengths and weaknesses of machine learning)", 'experiment_contamination': 'nothing', 'attention_check':'Georgia'})
        yield (pages.Debrief, {'agree': True})
