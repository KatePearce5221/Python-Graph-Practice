# Objective - create a function that takes a number as an input and then squares every digit of the number
def squareEveryDigit():
    inNumber = input("Enter a number: ") # input number
    newArr = [] # create a null array for later
    for i in inNumber: # append each of the digits of the integer to the array so they can be manipulated
        newArr.append(int(i))
    for i in range(0, len(newArr)): # square each item in the array
        newArr[i] = newArr[i]**2
    for i in newArr: # print the array as a digit
        print(i, end="")

squareEveryDigit()
