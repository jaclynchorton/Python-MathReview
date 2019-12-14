#---------------------------From the course Learning the Python 3 Standard Library--------------
#--------------------------------------------Random Module--------------------------------------
import random


#-------------------------------------------Random Numbers--------------------------------------
#Random generator that will print heads if number generated is 0 or Tails if
#the number generated is 1
print(random.random())
decider = random.randrange(2)

if decider == 0:
    print('HEADS')
else:
    print('TAILS')
print(decider)
#Creates a random number between 0 and 7 representing the role of a dice
print ("You rolled a " + str(random.randrange(1,7)))

#-------------------------------------------Random Choices--------------------------------------
lotteryWinners = random.sample(range(100), 5)
print(lotteryWinners)

possiblePets = ["cat", "dog", "fish"]
print(random.choice(possiblePets))

cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
print(cards)
