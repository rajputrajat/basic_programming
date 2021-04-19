# Exercise 9: Reverse a given number and
# return true if it is the same as the original number
# e.g. if number is 121 => return True
#         number is 120 => return False
# assert(is_magic_number(121) == True)

def is_magic_number(num: int) -> bool:
    nums: str = str(num)
    numl: list = list(nums)
    origl = numl.copy()
    numl.reverse()
    return origl == numl

assert(is_magic_number(121) == True)
assert(is_magic_number(1001) == True)
assert(is_magic_number(12221) == True)
assert(is_magic_number(1222) == False)

print('passed')
