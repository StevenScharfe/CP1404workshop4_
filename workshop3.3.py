lower = 10
upper = 100


def get_number(lower, upper):

    number = input(("Enter a number ({}-{})".format(lower, upper)))
    number = number.strip()
    while number.isdecimal() == False:
        print("Invalid")
        number = input("Enter a number ({}-{})".format(lower, upper))
        number = number.strip()
        number.isdecimal()

get_number(lower, upper)
