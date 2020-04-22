        #   Austin Copley
        #   CSCI 102 – Section B
        #   Week 9 - Part A
#Import random library
import random as r

print("Number to initialize the random generator:")
my_seed = int(input("SEED> "))
r.seed(my_seed)

#Create random int

num = r.randint(1, 100)

#Check guesses
guess = 101
while guess != num:
    guess = int(input("Enter a number between 1 and 100: "))
    if guess == num:
        print("OUTPUT Congrats! You won!")
    elif guess > 100:
        continue
    elif guess < 1:
        continue
    elif abs(num - guess) >= 50:
        print("OUTPUT You're cold!")
    elif abs(num - guess) >= 25:
        print("OUTPUT You're lukewarm!")
    elif abs(num - guess) >= 15:
        print("OUTPUT You're getting warm!")
    elif abs(num - guess) >= 5:
        print("OUTPUT You're getting hot!")
    else:
        print("OUTPUT You're so close!")
    print()
        
