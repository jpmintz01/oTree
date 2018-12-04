# generate list of random participant ids
import random
import string

print('Enter number of participants:')
num_participants = input()

print('Enter number of characters per participant ID:')
num_chars = input()

print('Enter filename')
filename = input()
f=open(filename, "w+")

participants = []
for i in range(int(num_participants)):
    participants.append('')
    
    for j in range (int(num_chars)-2):
        choice = random.choice(string.ascii_lowercase + string.digits)
        participants[i] += choice
    
    participants[i] += str(random.choice([1,2,3,4,5,6,7,8])) #adds random character 1-8 (app will select PW first or second based on whether this character is even or odd)      
    participants[i] += str(random.choice([1,2,3,4,5,6])) #adds random character 1-6 (app will select which counterbalance of the RPS game based on this)
    f.write(participants[i]+"\n")
    
f.close()

    
    