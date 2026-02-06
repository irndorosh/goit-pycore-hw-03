import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    else:
        numbers = list(range(min, max+1))
        lottery_numbers = random.sample(numbers, quantity)
        
        lottery_numbers.sort()
        return lottery_numbers

random_lottery_numbers = get_numbers_ticket(1, 49, 6)
print(random_lottery_numbers)