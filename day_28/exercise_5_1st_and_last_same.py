# Exercise 5: Given a list of numbers,
# return True if first and last number of a list is same
# input: a list of number
# output: True => 1st and last number is same
#         False => if those are different

def are_first_and_last_same(number_list):
    first = number_list[0]
    last = number_list[len(number_list) - 1]
    return first == last

assert(are_first_and_last_same([1, 2, 3, 5]) == False)
assert(are_first_and_last_same([10, 20, 9]) == False)
assert(are_first_and_last_same([20, 40, 2, 20]) == True)
assert(are_first_and_last_same([100, 100]) == True)
assert(are_first_and_last_same([100, 101]) == False)

print('passed')
