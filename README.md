# The Strategic Decision-making Experiment (Spear's Dissertation)

## quick start

Go to https://still-falls-66166.herokuapp.com/

To see the experiment in action, select "Experiment Start to Finish." then follow select the bottom link to open the experiment.  

Notes:
- Apps Version: 0.2
- This is still a dev version - participant will see something different.
- This link is a series of apps.

To do:
- create room & list of participant id's
- add possibility of fixed decisions for various players in P-W
- Add counterbalancing (will do this by repeating apps then hiding unused ones.  Probably a better way to do this, but will only explore if I have time.  Either way, results will be the same).<br>
-- (PW,RPS-H,RPS-A), (RPS-H,RPS-A,PW), (RPS-A,RPS-H,PW), (PW,RPS-A,RPS-H)
- Change/update/add immediate visual feedback on decisions
- change/update/add post-game feedback
- block browser commands (back/reload/keyboard/etc)
-

Fixed in this version:
- added possibility of fixed decisions for various players in RPS<br>
-- added lists in rps models.py under Constants<br>
-- lists came from the following code which I ran for 50 rounds 
________________
import random

print('Enter number of rounds:')
num_rounds = input()
choice_dict = {}
for i in range(int(num_rounds)):
    choice = random.choice(['Rock', 'Paper', 'Scissors'])
    print(str(i+1)+": " +choice)
    choice_dict[i]=choice

print(choice_dict)
________________

Fixed in recent versions: 
- Removed flying F-16 (or fix animation)
- removed "what type of algorithm were you playing against?"
- Added other participant IDs & wait pages.
- fixed html formatting errors
- started version tracking


Otherwise, click on any app.
For 1-Participant games, select the bottom link to open the game in a new tab.

For 2-participant games, select the link just below "open in split screen."

##

# oTree

oTree is a Python framework that lets you build:

- Multiplayer strategy games, like the prisoner's dilemma, public goods game, and auctions
- Controlled behavioral experiments in economics, psychology, and related fields
- Surveys and quizzes

## Homepage

http://www.otree.org/

## Docs

http://otree.readthedocs.org

## Related repositories

The oTree core libraries are [here](https://github.com/oTree-org/otree-core).
