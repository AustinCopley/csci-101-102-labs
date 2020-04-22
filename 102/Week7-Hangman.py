        #   Austin Copley
        #   ​CSCI 102 – Section B
        #   Week 7 - Hangman

#Start
print("Welcome to Simple Hang Man")
print("Enter a secret word:")
ogword = input("WORD> ")
word = list(ogword)
print()
print()
print()
print()
print()
print("Enter the number of guesses allowed:")
guesslim = int(input("NUM> "))

#initialize vars
count = 0
i = 0
guess = []
guesses = []
empty = ''

#create guessed list
while i < len(ogword):
    guess.append('_')
    i += 1


while 0 < guesslim:
    i = 0
#ask for character input
    print("Please enter a character:")
    character = input("CHAR> ")
    guesses.append(character)
    guesslim -= 1
    delim = ' '

    if character not in word:
        print("OUTPUT Boo! You guessed incorrectly")
        delimiter = ", "
        print(guesslim, "guesses remaining")
        print("Characters guessed: [", delimiter.join(guesses), "]")
        delim = ' '
        print("OUTPUT Secret word: ", delim.join(guess))
        print('')
    else:
        while i < len(word):
            if word[i] == character:
                guess[i] = word[i]
            i += 1
        if guess == word:
            print("OUTPUT Congratulations! You guessed the secret word!")
            delimiter = ", "
            print(guesslim, "guesses remaining")
            print("Characters guessed: [", delimiter.join(guesses), "]")
            delim = ' '
            print("OUTPUT Secret word: ", delim.join(guess))
            print('')
            break
        elif guesslim == 0 and guess != word:
            print("OUTPUT You ran out of guesses! Better luck next time!")
            print("OUTPUT Secret word:", delim.join(word))
            print('')
        else:
            print("OUTPUT Success! You guessed a character in the word!")
            delimiter = ", "
            print(guesslim, "guesses remaining")
            print("Characters guessed: [", delimiter.join(guesses), "]")
            delim = ' '
            print("OUTPUT Secret word: ", delim.join(guess))
            print('')
