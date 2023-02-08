#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    x = number % 10
else:
    x = ((number * -1) % 10) * -1
if x < 6 and x != 0:
    print(f"last digit of {number} is {x} and is less than 6 and not 0")
elif x == 0:
    print(f"last digit of {number} is {x} and is 0")
elif x > 5:
    print(f"last digit of {number} is {x} and is greater than 5")
