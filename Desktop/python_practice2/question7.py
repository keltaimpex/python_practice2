def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example
sample_list = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(sample_list))
