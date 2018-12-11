from os import environ
#import random

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

#Version 0.3

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
#    'doc': "",
#    'counterbalancing': 1,  #enter None or 1, 2, 3, or 4
#        #defines the counterbalance order
##        -- 1. PW,RPS-(H/A) (using treatment within RPS to randomize A/H)<br>
##        -- 2. RPS-(H/A),PW2<br>
##        -- 3. RPS-(A/H),PW2<br>
##        -- 4. PW,RPS-(A/H) <br>
    'pw_counterbalance': '1', #if this number is odd, play PW first. If even, play it after RPS
        #### NOTE: Don't set this to anything other than 1 if you want to play the individual app
    'rps_counterbalance': '2' # a list 1-6 of orders to play the adversaries
    #1 - H,HAI,AI (123)
    #2 - H, AI, HAI (132)
    #3 - HAI, AI, H (231)
    #4 - HAI, H, AU (213)
    #5 - AI, H, HAI (312)
    #6 - AI, HAI, H (321)
}

BROWSER_COMMAND = 'Safari'

SESSION_CONFIGS = [

    {
        'name': 'informed_consent',
        'display_name': "1. Informed Consent (ver 0.3.1)",
        'num_demo_participants': 1,
        'app_sequence': ['informed_consent'],
    },
#    {
#        'name': 'survey',
#        'display_name': "2. Pre-Game Questionnaire",
#        'num_demo_participants': 1,
#        'app_sequence': ['informed_consent','survey'],
#    },

    {
        'name': 'prisoner_multiplayer',
        'display_name': "2. Peace-War (ver 0.3.6) (multiplayer strategic no chat)",
        'num_demo_participants': 1,
#        'counterbalancing': 1,#needs to be 1 or 4 or else it won't play
        'app_sequence': ['informed_consent','prisoner_multiplayer'],
        'use_browser_bots': False,
        'num_PW_rounds': 20,
    },

    {
        'name': 'rps',
        'display_name': "2/3/4. Advised Rock Paper Scissors  (ver 0.4)",
        'num_demo_participants': 1,
#        'dev_game': True,
        'num_RPS_rounds': 2,
        'target_RPS_score': 1, #this puts the player's target score at slightly better than average - could add a 'target_human_score and a target_vs_AI_adversary_score or a target_AI_advisor_score if needed/desired'
        'control_RPS_score': True, #this tells the app, 'yes, I'd lke to control the participant's score instead of using pre-set values and/or an actual algorithm
        'app_sequence': ['informed_consent','rps']
    },
    {
        'name': 'prisoner_multiplayer_2',
        'display_name': "5. Peace-War (ver 0.3.6) (2nd instance for counterbalancing) (multiplayer strategic no chat)",
        'num_demo_participants': 1,
#        'counterbalancing': 2,#needs to be 2 or 3 or else it won't play
        'app_sequence': ['informed_consent','prisoner_multiplayer'],
        'use_browser_bots': False,
        'num_PW_rounds': 20,
    },
    {
        'name': 'post_game_survey',
        'display_name': "6. Post-Game Questionnaire (0.3.7)",
        'num_demo_participants': 1,
        'app_sequence': ['informed_consent','post_game_survey'],
    },
    {
        'name': 'multi_game_test',
        'display_name': "---> Experiment Start to Finish",
        'num_demo_participants': 1,
        'num_RPS_rounds': 20,
        'num_PW_rounds': 20,
        'target_RPS_score': 1, #this puts the player's target score at slightly better than average - could add a 'target_human_score and a target_vs_AI_adversary_score or a target_AI_advisor_score if needed/desired'
        'control_RPS_score': True, #this tells the app, 'yes, I'd lke to control the participant's score instead of using pre-set values and/or an actual algorithm
#        'counterbalancing': 1, #enter None or 1, 2, 3, or 4
        #defines the counterbalance order
#        -- 1. PW,RPS-(H/A) (using treatment within RPS to randomize A/H)<br>
#        -- 2. RPS-(H/A),PW2<br>
#        -- 3. RPS-(A/H),PW2<br>
#        -- 4. PW,RPS-(A/H) <br>
        'app_sequence': ['informed_consent', 'prisoner_multiplayer', 'rps','prisoner_multiplayer_2','post_game_survey'],
        'doc': """if 'pw_counterbalance' is 1, play PW first. If 2, play it after RPS. #### NOTE: Don't set this to anything other than 1 if you want to play the individual app. <br>'rps_counterbalance': # a list 1-6 of orders to play the adversaries #1 - H,HAI,AI (123)<br>#2 - H, AI, HAI (132)<br>#3 - HAI, AI, H (231)<br>#4 - HAI, H, AI (213)<br>#5 - AI, H, HAI (312)<br>#6 - AI, HAI, H (321)""",
    },

]
# see the end of this file for the inactive session configs

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    #    {
    #        'name': 'econ101',
    #        'display_name': 'Econ 101 class',
    #        'participant_label_file': '_rooms/econ101.txt',
    #    },
    {
        'name': 'AU',
        'display_name': 'Air University',
        'participant_label_file': '_rooms/AU_test.txt',
    },
    #    {
    #        'name': 'USAFA',
    #        'display_name': 'USAFA',
    #        'participant_label_file': '_rooms/USAFA.txt',
    #    },
    #    {
    #        'name': 'live_demo',
    #        'display_name': 'Room for live demo (no participant labels)',
    #    },
]


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

#environ['DATABASE_URL'] = 'postgres://postgres@localhost/django_db'

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """
Click an app, then the bottom link on the next page.
<br><br>
The 'Experiment Start to Finish' is what a participant will see.
"""

# don't share this with anybody.
SECRET_KEY = '(92a15wamnlz#lnupw5agxu)s*cu^uh&ro27o9+onw)8kl@ub9'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# inactive session configs
#    {
#        'name': 'multi_game_test',
#        'display_name': "Experiment Start to Finish",
#        'num_demo_participants': 1,
#        'num_rounds': 10,
#        'app_sequence': ['informed_consent','survey','prisoner_multiplayer', 'rps','post_game_survey'],
#        #'app_sequence':random.shuffle(['prisoner_multiplayer', 'chicken']),
#        #['survey','prisoner_multiplayer',],#'closing_comments'],
#        'use_browser_bots': False,
#        'use_strategy_method': True,
#        'crash_death_chance': 3, #1 in 3 chance of death in head-on crash
#        'doc': """ Edit the 'crash_death_chance' to a 1 in X number. If you want the chances of a crash death to be 1 in 1 (100%), enter 1.  If you want it to be 1 in 10, enter 10. to change the factor to that of the death payoff (usually negative).  Edit the 'swerve_death_chance' to a 1 in X number. If you want the chances of a swerve death to be 1 in 1000, enter 1000. It will randomly change the factor by which crash payoff (usually negative) is multiplied to that of the death_payoff.""",
#        'swerve_death_chance': 50, #1 in 50 chance of death
#    },
#    {
#        'name': 'prisoner',
#        'display_name': "Prisoner's Dilemma (one-shot w/chat)",
#        'num_demo_participants': 2,
#        'app_sequence': ['prisoner', 'payment_info'],
#    },
#    {
#        'name': 'prisoner_w_comms',
#        'display_name': "Prisoner's Dilemma (one-shot with Discrete Comms) (not working)",
#        'num_demo_participants': 2,
#        'app_sequence': ['prisoner_w_comms'],
#    },

#    {
#        'name': 'prisoner',
#        'display_name': "Prisoner's Dilemma (with chat)",
#        'num_demo_participants': 2,
#        'num_rounds': 10,
#        'app_sequence': ['prisoner'],#, 'payment_info'],
#    },

#    {
#        'name': 'chicken',
#        'display_name': "Chicken",
#        'num_demo_participants': 1,
#        'num_rounds': 2,
#        'crash_death_chance': 3, #1 in 3 chance of death in head-on crash
#        'doc': """ Edit the 'crash_death_chance' to a 1 in X number. If you want the chances of a crash death to be 1 in 1 (100%), enter 1.  If you want it to be 1 in 10, enter 10. to change the factor to that of the death payoff (usually negative).  Edit the 'swerve_death_chance' to a 1 in X number. If you want the chances of a swerve death to be 1 in 1000, enter 1000. It will randomly change the factor by which crash payoff (usually negative) is multiplied to that of the death_payoff.""",
#        'swerve_death_chance': 50, #1 in 50 chance of death in crash into ditch
#        'app_sequence': [
#            'chicken'
#
#        ],
#    },
#    {
#        'name': 'trust',
#        'display_name': "Trust Game",
#        'num_demo_participants': 2,
#        'num_rounds': 10,
#        'app_sequence': ['trust'],# 'payment_info'],
#    },
#    {
#        'name': 'ultimatum_non_strategy',
#        'display_name': "Ultimatum (direct response treatment)",
#        'num_demo_participants': 2,
#        'app_sequence': ['ultimatum',],# 'payment_info'],
#        'use_strategy_method': False,
#    },
#    {
#        'name': 'ultimatum_strategy',
#        'display_name': "Ultimatum (strategy method treatment)",
#        'num_demo_participants': 2,
#        'app_sequence': ['ultimatum',],#, 'payment_info'],
#        'use_strategy_method': True,
#    },

#    {
#        'name': 'trust_simple',
#        'display_name': "Trust Game (simple version from tutorial)",
#        'num_demo_participants': 2,
#        'num_rounds': 10,
#        'app_sequence': ['trust_simple'],
#    },
#    {
#        'name': 'dictator',
#        'display_name': "Dictator Game",
#        'num_demo_participants': 2,
#        'app_sequence': ['dictator',],# 'payment_info'],
#    },
#    {
#        'name': 'ultimatum',
#        'display_name': "Ultimatum (randomized: strategy vs. direct response)",
#        'num_demo_participants': 2,
#        'app_sequence': ['ultimatum',],# 'payment_info'],
#    },
##    {
##        'name': 'prisoner_nochat',
##        'display_name': "Prisoner's Dilemma (no Chat allowed)",
##        'num_demo_participants': 1,
##        'app_sequence': ['prisoner_nochat', 'payment_info'],
##        'use_browser_bots': False,
##    },
##

##    {
##        'name': 'quiz',
##        'num_demo_participants': 1,
##        'app_sequence': ['quiz'],
##    },
##    {
##        'name': 'my_public_goods',
##        'display_name': "My Public Goods (Simple Version)",
##        'num_demo_participants': 3,
##        'app_sequence': ['my_public_goods'],
##        'use_browser_bots': False,
##    },
##    {
##        'name': 'public_goods',
##        'display_name': "Public Goods",
##        'num_demo_participants': 3,
##        'app_sequence': ['public_goods', 'payment_info'],
##    },


### {
###     'name': 'prisoner',
###     'display_name': "Prisoner's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['prisoner', 'payment_info'],
### },
### {

##    {
##        'name': 'prisoner',
##        'display_name': "Prisoner's Dilemma",
##        'num_demo_participants': 2,
##        'app_sequence': ['prisoner', 'payment_info'],
##    },

### {
###     'name': 'vickrey_auction',
###     'display_name': "Vickrey Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['vickrey_auction', 'payment_info'],
### },
### {
###     'name': 'volunteer_dilemma',
###     'display_name': "Volunteer's Dilemma",
###     'num_demo_participants': 3,
###     'app_sequence': ['volunteer_dilemma', 'payment_info'],
### },
### {
###     'name': 'cournot',
###     'display_name': "Cournot Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'cournot', 'payment_info'
###     ],
### },
### {
###     'name': 'principal_agent',
###     'display_name': "Principal Agent",
###     'num_demo_participants': 2,
###     'app_sequence': ['principal_agent', 'payment_info'],
### },

### {
###     'name': 'matching_pennies',
###     'display_name': "Matching Pennies",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'matching_pennies',
###     ],
### },
### {
###     'name': 'traveler_dilemma',
###     'display_name': "Traveler's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['traveler_dilemma', 'payment_info'],
### },
### {
###     'name': 'bargaining',
###     'display_name': "Bargaining Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['bargaining', 'payment_info'],
### },
### {
###     'name': 'common_value_auction',
###     'display_name': "Common Value Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['common_value_auction', 'payment_info'],
### },
##    {
##        'name': 'guess_two_thirds',
##        'display_name': "Guess 2/3 of the Average",
##        'num_demo_participants': 3,
##        'app_sequence': ['guess_two_thirds', 'payment_info'],
##    },
### {
###     'name': 'bertrand',
###     'display_name': "Bertrand Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'bertrand', 'payment_info'
###     ],
### },
### {
###     'name': 'real_effort',
###     'display_name': "Real-effort transcription task",
###     'num_demo_participants': 1,
###     'app_sequence': [
###         'real_effort',
###     ],
### },
### {
###     'name': 'lemon_market',
###     'display_name': "Lemon Market Game",
###     'num_demo_participants': 3,
###     'app_sequence': [
###         'lemon_market', 'payment_info'
###     ],
### },
### {
###     'name': 'public_goods_simple',
###     'display_name': "Public Goods (simple version from tutorial)",
###     'num_demo_participants': 3,
###     'app_sequence': ['public_goods_simple', 'payment_info'],
### },

