# This was the version deployed in-person on day 1
# The Strategic Decision-making Experiment (Spear's Dissertation)

## quick start

Go to https://still-falls-66166.herokuapp.com/

To see the experiment start to finish, select "Experiment Start to Finish." then follow select the bottom link to open the experiment.  

To work with individual apps, click the app, then the bottom link.

Notes:
- <b> DON'T BE FOOLED!  The game called prisoner_multiplayer is actually the Peace-War game.</b>  Original naming convention stuck so as not to blow up to code.  Will fix when I go to "code cleanup" phase...
- Apps Versions:<br>
-- PW 0.4.1 (includes practice round)<br>
-- PW2 0.4
-- RPS 0.4.1 (includes practice round<br> 
-- settings.py 0.3.1<br>
-- Post-Game questionnaires 0.3.8<br>
-- informed consent 0.4.1 (sets up practice round)<br>
--- Pre-Game questionnaires (now included in Informed Consent<br>
-- bots version 0.4.3b (needs to account for RPS practice round)
- Readme Version 0.4.7
- The experiment apps are set to dev version - participant will see something different.

To do before experiment:
EXPERIMENT CONDUCT
MUST DO:
- set heroku environment variables
- double check heroku and local versions are same and current
- Mon AM: open the room session
- ensure able to use backup on local version
- test final version on heroku server with browser bots (works so far)


SHOULD DO:
- Add an outcome anomation to P-W next to each 
- cut down number of extra rounds or somehow set them to the config vars
- Make P-W results page better 


EXPERIMENT DESIGN
MUST DO:

SHOULD DO:
- change/update/add post-game feedback
- (use participant.vars variable - Make the first choice of each type in RPS a "win" to control out the "algorithm aversion when seeing it err."  If any advisor loses the first time, the participant is likely to avoid that advisor again.  But, I'd also need to make the first "no-choice" a win also.  After that, I'd control score back to target_RPS_score.
- Add "have you ever served on a CCDR, JCS, or OSD staff?"
- Change/update/add immediate visual feedback on decisions



To do later:
- BOTS
-- make bots more robust (random answers)<br>
- cut down extra variables in player class
- add "learning epochs" to AIs?
- explain AI better?
- Clean up code (low priority as long as it works)<br>
-- so clunky, but it works<br>
- Comment code (before publishing)
- if time, add P-W animation (handshake or jet-explosion)
- adjust post-game questions based on Prahl and Swol 2017?
-- how did you feel when the AI advisor failed you? were you ever going to use it again?<br>
-- How did you feel about the other human players?  Did you feel you had more in common with them than the AI?  Was there a kind of kinship? <br>
- split to H vs HAI, then H vs AI instead of all three at once?  That gives twice as many control inputs, and removes the possible confound of three variables?
- control P-W score


Done:
- fix RPS "control" score - it's always win/lose/win/lose... - maybe make it get back to central after max of 3 wins since first of each choice should be a win
- ensure settings.py (all repositories) is correct
- test the room session
- re-test counterbalancing from part.id
- double-check PW = PW2 version
- test server
- test data collection
- test self.participant.vars dump
- check peace-war payoffs (war-war should be negative...)
- give the human advisors a name?  Like "Steven" or something - Prahl and Swol 2017 - accentuates the difference between the human and AI.
- have 2-3 example rounds of each game to show them how to play (use Javascript to hide/prevent "submit" until player selects "I'm ready to start")
- Change P-W to Promote Peace or Wage War (PP or WW) to make it a verb like Cooperate or Defect
- disable buttons on RPS instruction page...(use div instead of button)
- Add "I will not share information about this study with others until told to do so" to informed consent.
- fix text and button size on tablet (P-W) 
- block browser commands (back/reload/keyboard/etc) or tell participants not to use keyboard except to type (and not to click back or reload)
- figure out kiosk mode
- Change "next" button to "Submit Round Choices"
- somehow disable adversary buttons in P-W (clicking them submits the form or causes something to happen) - maybe make it a div with icon like top "you (player dmo11)" instead of icon.  
-- "Icon turns green.."too wide, Player+AI button too wide (bold?), 
- remove "examples" from post-game questions like "i played randomly"
- create room & list of participant id's<br>
-- Do I need to split them up by AU College?
- cut down extra variables in player class
- upgrade heroku redis, dynos, db, etc to paid versions using otree hub or directly on heroku site
- fixed rps advice (got peace-war choices in there accidentally - Rand_Round generator)
- make bots test session and participant ID usage
- fix RPS adversary and expert "player IDs": make them the same for all players (get rid of random variable)
- fix RPS adv_type storage (to make data analysis easier)
- fix post-game questions<br>
-- change questions to "Why did you choose the strategy you did?"
- Move experiment_contamination to post-game questionnaire
- add survey control number (AUFELLOW1201) and IRB (FWr20190020H) to Post-Game Questionnaire
- created basic bots for all but post-game questionnaire
- add survey control number (AUFELLOW1201) and IRB (FWr20190020H) to both Informed Consent
- add number of rounds to RPS instructions
- add css animation to adversary type in RPS instructions
- Remove undergraduate minor
- Make controlled score a session variable in RPS (already done)
- RPS wasn't logging when it played on participant.vars, hence P-W was always played before and after.
- have the same adversaries for both RPS and P-W (i.e. human & AI or human & human+AI, or human & human+AI & AI)
- add adversary type to RPS:<br>
-- results page <br>
-- maybe wait page <br>
- fix participant player number in RPS
- fix advisor player number in RPS
- Fix counterbalancing in demo version (if required)
- removed pre-game questionnaire app (combined two questions and instructions into informed consent app)
- Adjust participant control "win/lose" ratio to something statistically/logically possible (RPS shouldn't be much more than 33% win)
- move most pre-game questions to end
- add adversary type and icon to RPS:<br>
-- decision & win page<br>
- fix post-game questionnaire, page 2: add bold to make questions more clear
-  control participant win/lose ratio or score by "faking it" vs controlling adversary's choices?
- add who participant is playing AGAINST to the wait page in RPS
- Fix post-game questionnaire, page 1: remove chicken
- added who participant is playing AGAINST to the wait page in P-W 1
- update Peace-War 2 templates to same version as P-W 1 (player nums are messed up)

Ideas but not now:
- Add third game? Maybe:
-- where participant IS the advisor but has to pass-on AI or human advice? Maybe a percentage of probability of war or something? <br>
--  the actual prisoner's dilemma with: <br>
--- a) the same payoffs, <br>
--- b) an ethical dilemma (target the terrorists with X chance of blowing up the baby milk factory) or, <br>
--- c) add another Peace-War with an explicit "reminder: you're making decisions on people's lives, are you considering your options carefully?" - seems like priming... <br>
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

## old bugs fixed / changes made

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

