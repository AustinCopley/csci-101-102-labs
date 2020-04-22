        #   Austin Copley
        #   CSCI 102 – Section B
        #   Week 9 - Part B

#import random library
import random as r

print("Would you like to provide your own string or generate a random one? (1 or 2)")
choice = int(input("CHOICE> "))

#init vars
kevin = 0
stacy = 0
alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
vowel = "AEIOU"
string = ''

#Enter string
if choice == 1:
    print("Enter a string for the game:")
    string = input("STRING> ")
    string = string.upper()

#Random string
elif choice == 2:
    print("Number to initialize the random generator:")
    my_seed = int(input("SEED> "))
    r.seed(my_seed)
    for i in range(0, 6):
        index = int(r.random() * len(alphabet))
        string += (alphabet[index])

#Loop for substrings
length = 1
while len(string) >= length:
    i = 0
    while (len(string) - length) >= i:
        #print(string[i: i + length])
        if string[i] in vowel:
            kevin += 1
        elif string[i] not in vowel:
            stacy += 1
        i += 1
    length += 1

#Print scores
print(f"With the string {string}, Kevin's score is {kevin} and Stacy's score is {stacy}")

#Determine winner
if kevin > stacy:
    print("Kevin wins!")
    print(f"OUTPUT {kevin}")
    print(f"OUTPUT {stacy}")
    print("OUTPUT Kevin")
elif kevin < stacy:
    print("Stacy wins!")
    print(f"OUTPUT {kevin}")
    print(f"OUTPUT {stacy}")
    print("OUTPUT Stacy")
elif kevin == stacy:
    print("It's a tie!")
    print(f"OUTPUT {kevin}")
    print(f"OUTPUT {stacy}")
    print("OUTPUT Draw")
    
