import random

def get_numbers_ticket(min, max, quantity):
    if (1 <= min <= max <= 1000) and quantity <= (max - min +1):
        numbers = random.sample(range(min, max + 1), quantity)
        numbers.sort()
        return numbers
    else:
        return []
    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)