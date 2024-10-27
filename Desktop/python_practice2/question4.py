def reverse_strings(strings):
    return [s[::-1] for s in strings]

# Example
words = ["apple", "banana", "cherry"]
reversed_words = reverse_strings(words)
print(reversed_words)
