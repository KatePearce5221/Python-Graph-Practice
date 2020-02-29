''' Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters,
numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.'''

import random # need random module to choose random words

# random words to use for passwords
randomWords = ["cruel", "ride", "bulletin", "height", "put", "convert", "straw", "taste", "suggest", "salvation", "certain", "certain", "ring", "toast", "army", "mayor", "novel", "tragedy", "recession", "jail", "tire", "card", "cheque", "mail", "Sunday", "elaborate", "economics"]
randomSymbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", ":", ";", "?", ">", "<", "{", "}"]


def restart(): # very beginning, written as a function to allow restarts
    print("Welcome to password generator! You can use this to generate weak, medium, or strong passwords.")
    startingChoice = int(input("To begin, press 1: "))
    if startingChoice == 1:
        passwordSelection() # user will select if they want a weak, medium, or strong password
    else:
        print("Invalid.")

def passwordSelection():
    print("Weak passwords have one or two lowercase words, medium passwords have two words, a capital letter, and a number, strong passwords have multiple uppercase")
    print("letters and lowercase letters, multiple words and numbers, and a symbol.")
    print("1 - Weak 2 - Medium 3 - Strong")
    selection = int(input("Enter your choice: ")) # selection to make a choice
    if selection == 1:
        weakPassword()
    elif selection == 2:
        mediumPassword()
    elif selection == 3:
        strongPassword()
    else:
        print("Invalid")

def weakPassword():
    weakWord1 = random.choice(randomWords) # picks a random element from the words list
    weakWord2 = random.choice(randomWords)
    if weakWord1 == weakWord2: # makes it much less likely the words will be the same, but not impossible
        weakWord2 = random.choice(randomWords)
    print("Your password is: " + str(weakWord1) + str(weakWord2))
    tryAgain = int(input("Want another password? Press 1: "))
    if tryAgain == 1:
        restart()
    else:
        print("Invalid.")

def mediumPassword():
    mediumWord1 = random.choice(randomWords) # pick a random word from the random words list
    mediumWord2 = random.choice(randomWords)
    newNumber = random.randrange(0, 100, 1) # pick a random number from 0-100 with an increment of 1
    print("Your password is: " + str(mediumWord1.capitalize()) + str(mediumWord2) + str(newNumber)) # concatenate them all and capitalize word 1
    tryAgain = int(input("Want another password? Press 1: "))
    if tryAgain == 1:
        restart()
    else:
        print("Invalid.")

def strongPassword():
    strongWord1 = random.choice(randomWords) # pick a random word from the random word list
    strongWord2 = random.choice(randomWords)
    strongWord3 = random.choice(randomWords)
    number = random.randrange(0, 250, 1) # pick a random number 1-250 with an increment of 1
    symbol = random.choice(randomSymbols) # pick a random symbol from the random symbols list
    password = str((str(strongWord1.capitalize()) + str(strongWord2) + str(strongWord3.capitalize()) + str(number) + str(symbol))) # concatenate them and capitalize words 1 and 3
    print("Your password is: " + str(password))
    tryAgain = int(input("Want another password? Press 1: "))
    if tryAgain == 1:
        restart()
    else:
        print("Invalid.")

restart()
