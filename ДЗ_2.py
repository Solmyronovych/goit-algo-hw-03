from random import randint

def get_numbers_ticket(min, max, quantity):
    if max < min:
        return []
    if min < 1:
        return []
    if quantity < 0 or quantity > (max - min):
        return []
    result_array = set()
    while len(result_array) != quantity:
        result_array.add(randint(min, max))
    return sorted(result_array)

numbers = get_numbers_ticket(10, 11, 10)
print(numbers)