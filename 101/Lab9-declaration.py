        #   Austin Copley
        #   ​CSCI 101 – Section F
        #   Python Lab 9

import random as r
import string as s

print("Would you like to print the number of times a specific word appears OR print the number of words of a specific length? (1 or 2)")
choice = int(input("CHOICE> "))
targetlen = []
words = []
target_amnt = 0

if choice == 1:
    print("Enter a word:")
    target = input("WORD> ")
    with open ("Declaration_of_independence.txt", 'r') as dec:
        lines = dec.readlines()
        for line in lines:
            words += (line[0:-1]).split(' ')
        for word in words:
            word = list(word)
            i = 0
            while i < len(word):
                if word[i] in s.punctuation:
                    word.pop(i)
                i += 1
            word = ''.join(word)
            if word.lower() == target.lower():
                target_amnt += 1

    print("The number of times", target, "appears in the document is", target_amnt)
    print("OUTPUT", target_amnt)
                        
elif choice == 2:
    print("Enter a length:")
    length = int(input("LENGTH> "))
    with open ("Declaration_of_independence.txt", 'r') as dec:
        lines = dec.readlines()
        for line in lines:
            words += (line[0:-1]).split(' ')
        for word in words:
            word = list(word)
            i = 0
            while i < len(word):
                if word[i] in s.punctuation:
                    word.pop(i)
                i += 1
            word = ''.join(word)
            if len(word) == length:
                word = ''.join(word)
                targetlen.append(word)
                
    print("Number to initialize the random generator: ")
    seed = int(input("SEED> "))
    r.seed(seed)

    if targetlen == []:
        print("The number of words in the document with length", length, "is: 0")
        print("OUTPUT 0")
        print("No example of random word of this length exists")
        print("OUTPUT ERROR")
        
    else:
        rang = len(targetlen)
        print("The number of words in the document with length", length, "is:", rang)
        print("OUTPUT", rang)
        print("One example random word of this length is:", length)
        index = r.randint(0, rang - 1)
        print("OUTPUT", targetlen[index])
