import random

def odd_or_even_number(random_number):
    if random_number % 2 == 0:
        return 'even'
    else:
        return 'odd'
random_number = random.randint(0,100)
print(odd_or_even_number(random_number))
