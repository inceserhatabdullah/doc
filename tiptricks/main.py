""" Write better code to be legend"""

# one line if statement
# from collections import Counter
# import sys


# condition = False --> x = 1 if condition else 0


# large numbers readable ---> price = 1_000_000_000 -> print(f'{price:,}')


# File read words
"""
with open('./<file_path>','r') as f:
    file_content = f.read()
words = file_content.split(' ')
word_Count = len(words)

"""


# list start is for index
# names = ['a', 'b', 'c', 'd', 'e'] --------- heroes = ['a1', 'a2', 'a3', 'a4', 'a5']
# for index, name in enumerate(names, start=0)
# for name, hero in zip(names, heroes)


# from getpass import getpass -> password = getpass('password: ')


# evens = [x for x in range(10) if x % 2 == 0]

# squares --> n_ = [1,2,3,4,5,6,7,8,9,10,11] -> s = list(map(lambda x: x ** 2, n_))


# data = [{'name': 'serhat','age': 1},{'name': 'abdullah','age': 2},{'name': 'ince','age': 3}] -> sorted(data, key=lambda x: x['name'])


# pl = [i for i in range(10_000)] ------------ pl_ = (i for i in range(10_000)) -> less memory than -> print(sys.getsizeof(pl), ' bytes')


# dict_ = {'item': 1, 'price': 0} -> count = dict_.get('count') -> dict_.setdefault('count', 20)


# list__ = [1,1,1,1,2,2,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,]
# counter_ = Counter(list__)
# most_common_counter = counter_.most_common(1)
# print(most_common_counter[0][0])
# print(max(set(list__), key=list__.count))

# merge dictionary
# md_ = {'name': 'serhat', 'age': 25}
# md__ = {'name': 'serhat', 'age': 25, 'job': 'engineer', 'love': 'python'}
# merge_dict = {**md_, **md__}


"""
sub, like, comment = 200, 140, 10
conditions = [
    sub > 50,
    like > 100,
    comment > 5
]

# and 
if all(conditions):
    print('Awesome condition')

# or
if any(conditions):
    print('Awesome condition')
"""


# reverse -->  text = 'example text' -> text[::-1]
# palindrome --> text.find(text[::-1]) == 0  "Return boolean value"