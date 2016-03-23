#
# outFile = open("name.txt", "w")
# name = input("What is your name? ")
# outFile.write(name)
# outFile.close()
#
# inFile = open("name.txt", 'r')
# name = inFile.read().strip()
# print("Your name is", name)
# inFile.close()

in_file = open("numbers.txt", "r")
result = 0
for line in in_file:
    number = int(line)
    result += number
print(result)
in_file.close()