from os import environ
import random

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']



SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

BROWSER_COMMAND = 'Safari'

SESSION_CONFIGS = [
    #    {
    #        'name': 'survey',
    #        'num_demo_participants': 1,
    #        'app_sequence': ['survey'],
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
        {
        'name': 'prisoner',
        'display_name': "Prisoner's Dilemma",
        'num_demo_participants': 2,
        'num_rounds': 10,
        'app_sequence': ['prisoner'],#, 'payment_info'],
    },
    {
        'name': 'chicken',
        'display_name': "Chicken",
        'num_demo_participants': 2,
        'num_rounds': 2,
        'crash_death_chance': 3, #1 in 3 chance of death in head-on crash
        'doc': """ Edit the 'crash_death_chance' to a 1 in X number. If you want the chances of a crash death to be 1 in 1 (100%), enter 1.  If you want it to be 1 in 10, enter 10. to change the factor to that of the death payoff (usually negative).  Edit the 'swerve_death_chance' to a 1 in X number. If you want the chances of a swerve death to be 1 in 1000, enter 1000. It will randomly change the factor by which crash payoff (usually negative) is multiplied to that of the death_payoff.""",
        'swerve_death_chance': 50, #1 in 50 chance of death in crash into ditch
        'app_sequence': [
            'chicken'

        ],
    },


    {
        'name': 'prisoner_multiplayer',
        'display_name': "Prisoner's Dilemma (multiplayer strategic no chat)",
        'num_demo_participants': 1,
        'app_sequence': ['prisoner_multiplayer'],
        'use_browser_bots': False,
        'num_rounds': 3,
    },
    {
        'name': 'rps',
        'display_name': "Rock Paper Scissors",
        'num_demo_participants': 1,
        'num_rounds': 10,
        'app_sequence': ['rps',],# 'payment_info'],
    },
    {
        'name': 'multi_game_test',
        'display_name': "Game Example",
        'num_demo_participants': 1,
        'num_rounds': 3,
        'app_sequence': ['survey','prisoner_multiplayer', 'chicken', 'rps','post_game_survey'],
        #'app_sequence':random.shuffle(['prisoner_multiplayer', 'chicken']),
        #['survey','prisoner_multiplayer',],#'closing_comments'],
        'use_browser_bots': False,
        'use_strategy_method': True,
        'crash_death_chance': 3, #1 in 3 chance of death in head-on crash
        'doc': """ Edit the 'crash_death_chance' to a 1 in X number. If you want the chances of a crash death to be 1 in 1 (100%), enter 1.  If you want it to be 1 in 10, enter 10. to change the factor to that of the death payoff (usually negative).  Edit the 'swerve_death_chance' to a 1 in X number. If you want the chances of a swerve death to be 1 in 1000, enter 1000. It will randomly change the factor by which crash payoff (usually negative) is multiplied to that of the death_payoff.""",
        'swerve_death_chance': 50, #1 in 50 chance of death
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
        'name': 'USAFA',
        'display_name': 'USAFA',
        'participant_label_file': '_rooms/USAFA.txt',
    },
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


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """
Here are various games implemented with 
oTree. These games are open
source, and you can modify them as you wish.
"""

# don't share this with anybody.
SECRET_KEY = '(92a15wamnlz#lnupw5agxu)s*cu^uh&ro27o9+onw)8kl@ub9'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# inactive session configs
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
###     'name': 'trust',
###     'display_name': "Trust Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust', 'payment_info'],
### },
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
### {
###     'name': 'trust_simple',
###     'display_name': "Trust Game (simple version from tutorial)",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust_simple'],
### },
