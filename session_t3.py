import random

choicess = ['hello', 'yello', 'mello', 'hallo']

newlist = []

for i in range(101):
    newlist.append(random.choice(choicess))
    
print(newlist)