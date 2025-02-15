import random

print("Welcome to the World's greatest Dice Roller App")
print('-'*48)
print('how many dice would you like to roll?')

while True:
    try: 
        numberPicked = int(input('Type an integer between 1 and 10: '))
        if(numberPicked>0 and numberPicked<=10):
            break
        else: 
            print('Invalid Input. Try again.')
    except: 
        print('Invalid input. Please provide an integer.')
    
def rollDice(numberPicked):
    totalSum = 0
    possibleFaces=[1,2,3,4,5,6]
    for die in range(numberPicked):
        roll = random.choice(possibleFaces)
        print('Die ', die+1, ": ", roll)
        totalSum+=roll
    average=totalSum/numberPicked
    print(f"Total Sum of {numberPicked} die/dice: {totalSum}")
    print(f"Your Average/Dice of {numberPicked} die/dice: {average}")

    
rollDice(numberPicked)

