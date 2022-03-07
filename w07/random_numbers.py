import random
import math


def main():

    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print('This is appended.')
    print(numbers)
    append_random_numbers(numbers, 3)
    print('This has three more')
    print(numbers)


def append_random_numbers(numbers, quantity=1):

    #if quantity ==1:
    for _ in range(quantity):
        number = round(random.uniform(1, 99), 1)
        numbers.append(number)


main()