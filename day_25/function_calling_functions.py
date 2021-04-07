def increment_by_one(a):
    return a + 1

def multiply_by_2(a):
    return a * 2

def magic(a, b, c):
    return increment_by_one(multiply_by_2(a) + increment_by_one(b)) + multiply_by_2(c)

def do_other_calculation(a):
    return increment_by_one(multiply_by_2(a))

print(do_other_calculation(10))
print(magic(10, 1, 2))
