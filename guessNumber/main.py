import random
import datetime

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

# guess_number_from_human()


def guess_number_from_machine():
    now = datetime.datetime.now()
    now_strftime = now.strftime('%Y-%m-%d %H:%M:%S')
    my_number = 1_245_652
    iterator = 0
    _ = True
    x, y = input(f'Program started at {now_strftime}\nWhat is your range of your numbers? My number is between in: ').split(' ')
    guess_number_list = [*range(int(x), int(y) + 1, 1)]
    copy_guess_number_list = guess_number_list.copy()
    
    # print(f'List created for numbers from {int(x)} to {int(y)}')

    while _:
        _now = datetime.datetime.now()
        iterator += 1
        random_index = random.randint(0, len(copy_guess_number_list) - 1)
        guess_number = copy_guess_number_list[random_index - 1]

        condition = [
            len(copy_guess_number_list) == 1,
            guess_number != my_number,
        ]
        # print(f'List: {copy_guess_number_list}')
        
        if all(condition):
            print(f'You guessed {guess_number} it is not in the list!\nYour number is {my_number} outside the given range, check it!\nTime Difference: {_now - now}')
            break

        if guess_number == my_number:
            print(f'Your guess: {guess_number}\nMy number was {my_number} and you found it in {iterator} iteration.\nTime Difference: {_now - now}')
            _ = False
        elif guess_number < my_number:
            print(f'Your guess: {guess_number} it is lower! Try guess higher.\nTime: {_now}\n')
            copy_guess_number_list.pop(random_index - 1)
            if guess_number != min(copy_guess_number_list):
                del copy_guess_number_list[:random_index - 1]
        else:
            print(f'Your guess: {guess_number} it is higher! Try guess lower.\nTime: {_now}\n')
            copy_guess_number_list.pop(random_index - 1)
            if guess_number != max(copy_guess_number_list):
                del copy_guess_number_list[random_index - 1:]
        

guess_number_from_machine()
