# Exercise 4: Given a string and an integer number n,
# remove characters from a string starting from zero
# up to n and return a new string

def remove_first_chars(a_str, num):
    v1 = ''
    for i in range(num, len(a_str)):
        v1 += a_str[i]
    return v1

new_str = remove_first_chars('pynative', 4)
assert(new_str == 'tive')

new_str_2 = remove_first_chars('a new example', 5)
assert(new_str_2 == ' example')

new_str_3 = remove_first_chars('hello world', 9)
assert(new_str_3 == 'ld')

print('all good')