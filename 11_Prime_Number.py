number = 24
dividers = 0

for i in range(2,17):
    if(number % i == 0):
        dividers = dividers + 1

if(dividers == 0):
    print("Prime")
else:
    print("Not prime")