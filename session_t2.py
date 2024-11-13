
listnew = []

for i in range(1,50,2):
    listnew.append(i)

listnew2 = []

for num in listnew:
    if num % 3 == 0 or num % 5 == 0:
        listnew2.append(num)

listnew.extend(listnew2)

print(f"list : {listnew}")