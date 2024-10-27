def has_pair_with_sum(numbers, target_sum):
    seen_numbers = set()
    for num in numbers:
        complement = target_sum - num
        if complement in seen_numbers:
            return True
        seen_numbers.add(num)
    return False
#An example
numbers = [10, 15, 3, 7]
target_sum = 17
print(has_pair_with_sum(numbers, target_sum))  # Output: True
