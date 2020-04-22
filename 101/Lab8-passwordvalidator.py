    #   Austin Copley
    #   CSCI 101 – Section F
    #   Python Lab 8

import string as s
import random as r

characters = s.ascii_letters + s.digits + s.punctuation
score = 0
password = ''
upper = 0
lower = 0

print("Would you like to check your own password or a random one? (1 or 2)")
choice = int(input())
vowels = 'AEIOUaeiou'

if choice == 1:
    print("Enter a password to validate:")
    password = input("PASSWORD> ")
elif choice == 2:
    print("Number to initialize the random generator:")
    my_seed = int(input("SEED> "))
    r.seed(my_seed)
    for i in range(0, 8):
        index = int(r.random() * len(s.ascii_letters))
        password += (s.ascii_letters[index])
    for i in range(0,2):
        index = int(r.random() * len(s.digits))
        password += (s.digits[index])
    for i in range(0,2):
        index = int(r.random() * len(s.punctuation))
        password += (s.punctuation[index])
print(password)

print(f"Validating the password {password}")
if s.punctuation not in password and s.digits not in password and len(password) < 8:
    print(f"The password {password} is an invalid password")
    print("OUTPUT INVALID")

else:
    for i in range(len(password)):
        if password[i] in s.ascii_letters:
            score += 4
            if password[i] in vowels:
                score -= 3
            if password[i] in s.ascii_uppercase:
                upper += 1
            elif password[i] in s.ascii_lowercase:
                lower += 1
        elif password[i] in s.digits:
            score += 5
        elif password[i] in s.punctuation:
            score += 6
        
score += (upper - lower) * 2

strength = ""
if score < 20:
    strength = "Weak+"
elif score < 40:
    strength = "Weak"
elif score < 60:
    strength = "Good"
elif score < 80:
    strength = "Strong"
else:
    strength = "Strong+"

print(f"The password {password} is a {strength} password")
print(f"OUTPUT {strength}")
