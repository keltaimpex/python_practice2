def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# an Example
numbers_tuple = (10, 20, 30, 40, 50)
print(find_largest_number(numbers_tuple))
