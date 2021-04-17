def get_nums(num):
    nums = ''
    for i in range(num):
        nums += str(num)
    return nums

assert(get_nums(4) == '4444')
assert(get_nums(1) == '1')

def make_triangle(num):
    for i in range(1, num + 1):
        print(get_nums(i))
        #print(str(i) * i)

make_triangle(5)
print()
make_triangle(9)
print()
make_triangle(1)