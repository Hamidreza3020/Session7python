import random

choicess = ['hello', 'yello', 'mello', 'hallo']

newlist = []

newlist2 = []

for i in range(101):
    
    newlist.append(random.choice(choicess))
for i in newlist:
    if i == "hello":
        newlist2.append(i)

print(newlist2)