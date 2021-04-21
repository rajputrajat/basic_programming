# Exercise 10: Given a two list of numbers create a new list
# such that new list should contain only odd numbers from the first list
# and even numbers from the second list
# Expected Output:

# list1 =  [10, 20, 23, 11, 17]
# list2 = [13, 43, 24, 36, 12]

# result List is [23, 11, 17, 24, 36, 12]

def make_odd_even_list(l1: list, l2: list) -> list:
    pass

assert(make_odd_even_list(
    [10, 20, 23, 11, 17],
    [13, 43, 24, 36, 12]) == [23, 11, 17, 24, 36, 12])

assert(make_odd_even_list([1, 2, 4], [1, 2, 4]) == [1, 2, 4])

print('passed')