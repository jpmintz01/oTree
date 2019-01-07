# generate list of random choices
import random

print('Enter number of players:')
num_players= input()
print('Enter number of rounds:')
num_rounds = input()
print('Enter weighting factor for AI vs others (i.e. AI 2x more likely vs AI than other answers -> 2):')
weight_factor = input()

choice_dict = {}
for i in range(int(num_rounds)):
    choice = random.choice(['Rock', 'Paper', 'Scissors'])#['Peace', 'War'])#
    print(str(i+1)+": " +choice)
    choice_dict[i]=choice

print(choice_dict)
    
    