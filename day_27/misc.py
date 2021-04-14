# enumerate
a = 'pynative'
for index, value in enumerate(a):
    if (index + 1) % 2 == 0:
        print(value)

# loop using range(start, stop, step)
print('second solution follows')
###
def get_even_nums(str_var):
    ret_str = ''
    for i in range(1, len(str_var), 2):
        ret_str += str_var[i]
    return ret_str
a = 'pynative'
assert(get_even_nums(a) == 'yaie')

a = 'hello'
b = 'world'
c = a + ' ' + b
print(c)
assert(c == 'hello world')

# range(start_index, stop, step)
# for i in range(5, 100 + 1, 5) => this loop goes 5, 10, 15, 20, ... , 95, 100
# range(5)        number => stop, default start value = 0, default step = 1. [[[0, 1, 2, 3, 4]]]
# range(1, 7)     index => start_index, number => stop, default step = 1. [[[1, 2, 3, 4, 5, 6]]]
# range(1, 7, 2)  [[[1, 3, 5]]]
# for i in range(1, 7, 2):
#     print('range test', i)