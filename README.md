# The Strategic Decision-making Experiment (Spear's Dissertation)

## quick start

Go to https://still-falls-66166.herokuapp.com/

To see the experiment start to finish, select "Experiment Start to Finish." then follow select the bottom link to open the experiment.  

To work with individual apps, click the app, then the bottom link.

Notes:
- <b> DON'T BE FOOLED!  The game called prisoner_multiplayer is actually the Peace-War game.</b>  Original naming convention stuck so as not to blow up to code.  Will fix when I go to "code cleanup" phase...
- Apps Versions:<br>
-- PW 0.3.2<br>
-- RPS 0.3.3<br>
-- settings.py 0.2.9<br>
-- Pre-Game questionnaires 0.2.5<br>
-- Post-Game questionnaires 0.2.5<br>
-- informed consent 0.3
- Readme Version 0.3.2
- The experiment apps are set to dev version - participant will see something different.

To do before experiment:
- (DONE but need feedback) control participant win/lose ratio or score by "faking it" vs controlling adversary's choices?
- Make results pages better
- add who participant is playing AGAINST to the wait page in RPS
- fix participant player number in RPS
- fix advisor player number in RPS
- Fix counterbalancing in demo version (if required)
- update Peace-War 2 templates to same version as P-W 1 (player nums are messed up)
- add "learning epochs" to AIs?
- Add third game where participant IS the advisor but has to pass-on AI or human advice? Maybe a percentage of probability of war or something?

- fix post-game questionnaire, page 2: add bold to make questions more clear
- do I need to have the same adversaries for both RPS and P-W?  i.e. human & AI or human & human+AI, or human & human+AI & AI
- Should I add a game that's the actual prisoner's dilemma with: a) the same payoffs, b) an ethical dilemma, or c) add another Peace-War with an explicit "reminder: you're making decisions on people's lives, are you considering your options carefully?" - seems like priming...
- explain AI better?

- if time, add P-W animation (handshake or jet-explosion)
- <b>check fixed advice and adversary choices to see win/lose percentage -> should be near 50%?</b>
- fix post-game questions<br>
-- remove chicken <br>
-- change questions to "Why did you choose the strategy you did?"
- test server
- test data collection
- switch to postgresql?
- runserver prodserver vs devserver
- check peace-war payoffs (war-war should be negative...)
- add adversary type and icon to RPS:<br>
-- instructions<br>
-- decision & win page<br>
-- results page
- create room & list of participant id's<br>
-- Do I need to split them up by AU College?
- Change/update/add immediate visual feedback on decisions
- change/update/add post-game feedback
- block browser commands (back/reload/keyboard/etc)


To do later:
- Clean up code (low priority as long as it works)<br>
-- so clunky, but it works<br>
- Comment code (before publishing)


Fixed in this version:
- Fix post-game questionnaire, page 1: remove chicken
- added who participant is playing AGAINST to the wait page in P-W 1


Fixed in recent versions: 
- Moved styles and such to global page (mostly)
- inserted "now you're playing [human or AI]" in RPS
- automated counterbalancing by participant id's
- created random participant id generator (with last character 1-4 indicating counterbalancing treatment)
________________
<pre>
import random
import string

print('Enter number of participants:')
num_rounds = input()

print('Enter number of characters per participant ID:')
num_chars = input()

print('Enter filename')
filename = input()
f=open(filename, "w+")

participants = []
for i in range(int(num_rounds)):
    participants.append('')
    
    for j in range (int(num_chars)-1):
        choice = random.choice(string.ascii_lowercase + string.digits)
        participants[i] += choice
        
    participants[i] += str(random.choice([1,2,3,4])) #adds random character 1-4
    f.write(participants[i]+"\n")
    
f.close()
</pre>
________________
- separated number of rounds for P-W and RPS (adjustable in settings.py CONFIGS)
- informed consent now a) lets you play if yes or b) sends you to end if no
- updatd demo readme on demo page
- created RPS-(A or H) from RPS so RPS can play vs human and AI (or AI then human)<br>
-- randomized adversary & advisor player id in RPS
- fix CSS for animated progress bar
- Added counterbalancing (will do this by repeating apps then hiding unused ones.  Probably a better way to do this, but will only explore if I have time.  Either way, results will be the same).<br>
-- 1. PW,RPS-(H/A) (using treatment within RPS to randomize A/H)<br>
-- 2. RPS-(H/A),PW2<br>
-- 3. RPS-(A/H),PW2<br>
-- 4. PW,RPS-(A/H) <br>
-- Means (PW, RPS, PW2) <br>
-- create RPS-(A or H) from RPS and PW2 from PW<br>
--- randomize adversary player id (not required)
- Removed flying F-16 (or fix animation)
- removed "what type of algorithm were you playing against?"
- Added other participant IDs & wait pages.
- fixed html formatting errors
- started version tracking
- added possibility of fixed decisions for various players in P-W (same technique as RPS - see below)
- added possibility of fixed decisions for various players in RPS<br>
-- added lists in rps models.py under Constants<br>
-- does python's random function provide enough true randomness?<br><br>
-- list of adversary choices and advisors came from the following code which I ran for 50 rounds:<br>
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
