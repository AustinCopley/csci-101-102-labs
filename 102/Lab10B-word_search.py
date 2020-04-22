        #   Austin Copley
        #   CSCI 102 – Section B
        #   Week 10 - Part B

import random as r

print("Enter the length of the word you are looking for:")
length = int(input("LENGTH> "))

print("Number to initialize the random generator: ")
seed = int(input("SEED> "))
r.seed(seed)
targetlen = []
words = []

with open("dictionary.txt", 'r') as dictionary:
    lines = dictionary.readlines()
    for line in lines:
        words += (line[0:-1]).split(' ')
    for word in words:
        if len(word) == length:
            word = ''.join(word)
            targetlen.append(word)
if targetlen == []:
    print("There is no word of length", length, "in this file.")
    print("OUTPUT ERROR")
else:
    rang = len(targetlen)
    print("There are", rang, "words in the dictionary with length", length)
    print("OUTPUT", rang)
    print("Here is one random word in the dictionary with length", length)
    index = r.randint(0, rang - 1)
    print("OUTPUT", targetlen[index])
