# The Strategic Decision-making Experiment (Spear's Dissertation)

## quick start

Go to https://still-falls-66166.herokuapp.com/

To see the experiment start to finish, select "Experiment Start to Finish." then follow select the bottom link to open the experiment.  

To work with individual apps, click the app, then the bottom link.

Notes:
- Apps Versions:
-- PW 0.2.6
-- RPS 0.2.7
-- settings 0.2.7
- Readme Version 0.2.7
- The experiment apps are set to dev version - participant will see something different.

To do before experiment:
- test server
- test data collection
- switch to postgresql?
- runserver prodserver vs devserver
- check peace-war payoffs (war-war should be negative...)
- add adversary type and icon to RPS:
-- instructions
-- decision & win page
-- results page
- create room & list of participant id's
-- Do I need to split them up by AU College?
- Add counterbalancing (will do this by repeating apps then hiding unused ones.  Probably a better way to do this, but will only explore if I have time.  Either way, results will be the same).<br>
-- 1. PW,RPS-(H/A) (using treatment within RPS to randomize A/H)<br>
-- 2. RPS-(H/A),PW2<br>
-- 3. RPS-(A/H),PW2<br>
-- 4. PW,RPS-(A/H) <br>
-- Means (PW, RPS, PW2) <br>
-- create RPS-(A or H) from RPS and PW2 from PW
--- randomize adversary player id
- Change/update/add immediate visual feedback on decisions
- change/update/add post-game feedback
- block browser commands (back/reload/keyboard/etc)
-

To do later:
- Clean up code (low priority as long as it works)
-- Move styles and such to global page
- Comment code (before publishing)


Fixed in this version:
- separated number of rounds for P-W and RPS
- informed consent now a) lets you play or b) sends you to end
- updatd demo readme on demo page
- created RPS-(A or H) from RPS
-- randomized adversary & advisor player id in RPS
- fix CSS for moving progress bar

Fixed in recent versions: 
- Removed flying F-16 (or fix animation)
- removed "what type of algorithm were you playing against?"
- Added other participant IDs & wait pages.
- fixed html formatting errors
- started version tracking
- added possibility of fixed decisions for various players in P-W (same technique as RPS - see below)
- added possibility of fixed decisions for various players in RPS<br>
-- added lists in rps models.py under Constants<br>
-- does python's random function provide enough true randomness?<br>
-- lists came from the following code which I ran for 50 rounds :<br>
________________
<pre>
import random

print('Enter number of rounds:')
num_rounds = input()
choice_dict = {}
for i in range(int(num_rounds)):
    choice = random.choice(['Rock', 'Paper', 'Scissors'])
    print(str(i+1)+": " +choice)
    choice_dict[i]=choice
    
print(choice_dict)
</pre>
________________


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
