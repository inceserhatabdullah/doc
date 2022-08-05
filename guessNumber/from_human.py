#!/usr/bin/env python3

import random
def guess_number_from_human():
    random_number = random.randint(0, 50)
    iterator = 0

    while True:
        iterator += 1
        guess_number = int(input(f'Guess a number between 0 and 50. What is your guess? '))

        if guess_number == random_number:
            print(f'The number {guess_number} you guessed was found in {iterator} iteration. I guessed number was {guess_number}')
            break
        elif guess_number < random_number:
            print(f'You guessed {guess_number} it is lower! Please try again to guess higher.')
        else:
            print(f'You guessed {guess_number} it is higher! Please try again to guess lower.')