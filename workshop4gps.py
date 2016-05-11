import random

MIN_BIRTH_RATE = 0.1
MAX_BIRTH_RATE = 0.2
MIN_DEATH_RATE = 0.05
MAX_DEATH_RATE = 0.25
increase = 0
decrease = 0
population = 1000
yearcounter = 1

print("Welcome to the Gopher Population Simulator\nStarting Population: {}\n".format(population))

while yearcounter < 11:
    print("Year {}".format(yearcounter))
    print("*****")
    birth = random.uniform(MIN_BIRTH_RATE, MAX_BIRTH_RATE)
    increase = int(population * (1 + birth)) - population
    death = random.uniform(MIN_DEATH_RATE, MAX_DEATH_RATE)
    decrease = int(population - (population / (1 + death)))
    population += increase - decrease
    print("{} gophers were born. {} died.\nPopulation: {}\n".format(increase, decrease, population))
    yearcounter += 1

def func_1
    number = 1
    while number = 1
        print("Lol")
