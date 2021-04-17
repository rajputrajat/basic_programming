# Exercise 7:
# Return the count of sub-strings appears in the given string

def sub_string_count(in_str, in_substr):
    return in_str.count(in_substr)

assert(sub_string_count('come here. come here fast.', 'come') == 2)
assert(sub_string_count('return the returned item with some returns', 'return') == 3)
assert(sub_string_count('there are 45 lions in this park. and 450 pigeons', '45') == 2)

print('passed')