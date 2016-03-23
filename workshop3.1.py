
import random
MAX_INCREASE = 0.175 # 10%
MAX_DECREASE = 0.05 # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
price = INITIAL_PRICE


def format_currency(value):
    newFormat = ("${:,.2f}".format(value))
    return newFormat

print("Starting Price: " + format_currency(price))
counter = 0
while price >= MIN_PRICE and price <= MAX_PRICE:

    priceChange = 0
    if random.randint(1, 2) == 1:
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        priceChange = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + priceChange)
    counter += 1
    print("On Day {}, price is: {}".format(counter, format_currency(price)))

