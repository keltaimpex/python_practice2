def tuples_to_dict(tuples_list):
    result_dict = {}
    for string, number in tuples_list:
        result_dict[string] = number
    return result_dict
#An example
tuples_input = [("apple", 5), ("banana", 10), ("cherry", 7)]
result = tuples_to_dict(tuples_input)
print(result)
