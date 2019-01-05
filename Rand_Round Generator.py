# generate list of random choices
import random

print('Enter number of rounds:')
num_rounds = input()
choice_dict = {}
for i in range(int(num_rounds)):
    choice = random.choice(['Rock', 'Paper', 'Scissors'])#['Peace', 'War'])#
    print(str(i+1)+": " +choice)
    choice_dict[i]=choice

print(choice_dict)
    
    