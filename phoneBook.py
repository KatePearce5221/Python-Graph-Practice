''' Basically, this program basically has one dictionary, the phone book, and several options for what to do with it. Add contacts (adding keys and values), delete
contacts (deleting keys and values), finding a contact (finding a specific value of a key), and viewing the phone book (printing the dictionary and using a for loop
to omit the ugly stuff). Each option has its own function. I've done this type of thing before, but I always have trouble with dictionaries so I thought this would
be nice review. Enjoy! '''

phoneBook = {"Kate": 1234567890, "Lisa": 567890} # Initialize the dictionary

def startingMenu(): # starting options for users
    print("1 - Add A Contact\n2 - Delete A Contact\n3 - Find a Specific Contact\n4 - View Whole Phone Book\n5 - Quit") # text gives directions
    startingChoice = int(input("Enter a choice: "))
    if startingChoice == 1: # selection starts here and routes user to appropriate function
        addAContact()
    elif startingChoice == 2:
        deleteAContact()
    elif startingChoice == 3:
        findAContact()
    elif startingChoice == 4:
        viewPhoneBook()
    elif startingChoice == 5:
         print("See ya!")
    else:
        print("Invalid")

def addAContact(): # first choice
    newContactName = str(input("Enter a name: "))
    if newContactName in phoneBook: # selection to see if name is already in the phone book
        print(str(newContactName) + " is already in the phone book.")
        startingMenu()
    newContactNumber = input("Enter their number: ")
    phoneBook[newContactName] = newContactNumber # makes a new entry in dictionary using the name as the key
    print (str(newContactName) + " has been added.")
    startingMenu()

def deleteAContact(): # second choice
    deletedContact = str(input("Enter the name of the contact you want to delete: "))
    if deletedContact in phoneBook: # selection to see if name is in the phone book
        del phoneBook[deletedContact] # delete the contact with that key
        print (str(deletedContact) + " has been deleted.")
        startingMenu()
    else: # if name is not in the phone book
        print (str(deletedContact) + " is not in your phone book.")
        startingMenu()

def findAContact(): # third choice
    findContactName = str(input("Enter the contact name: "))
    if findContactName in phoneBook: # selection if name is in phone book
        print("The number for " + str(findContactName) + " is " + str(phoneBook[findContactName])) # concatenation with finding the number associated with the name key
        startingMenu()
    else: # if name is not in phone book
        print(str(findContactName) + " is not in your phone book.")
        startingMenu()

def viewPhoneBook(): # fourth choice
    for key, value in phoneBook.items(): # for each key and value in the phone book, omit the brackets
        print("{}: {}".format(key, value))
    startingMenu()


startingMenu()
