
MIN_LENGTH = 5
MAX_LENGTH = 15

valid = False
password = input("Enter a valid Password")
print("Your password must be between 5 and 15 characters, and contain:")

while not valid:

        lowerCounter = 0
        upperCounter = 0
        digitCounter = 0
        for char in password:
            if char.islower():
                lowerCounter += 1
            if char.isupper():
                upperCounter += 1
            if char.isdigit():
                digitCounter += 1
        if lowerCounter < 0 or upperCounter < 0 or digitCounter < 0 or password.__len__() > 15 or password.__len__() < 5:
            pass