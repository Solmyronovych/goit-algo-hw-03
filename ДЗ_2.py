from random import randint

def get_numbers_ticket(min, max, quantity):
    result_array = set()
    while len(result_array) != quantity:
        result_array.add(randint(min, max))
    return sorted(result_array)

numbers = get_numbers_ticket(1, 1000, 6)
print(numbers)