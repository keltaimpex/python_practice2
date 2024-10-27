def print_even_value_keys(input_dict):
    for key, value in input_dict.items():
        if value % 2 == 0:
            print(key)

# An Example
sample_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_value_keys(sample_dict)
