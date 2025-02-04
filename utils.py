def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

def find_minimum(numbers):cd
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum