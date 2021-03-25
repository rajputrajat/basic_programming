char = input('which character: ')
times = int(input('how many times: '))

for a in range(times):
    to_print = char + ' '
    how_many_times = a + 1
    make_a_line = to_print * how_many_times
    print(make_a_line)
    # print((char + ' ') * (a + 1))

# range(4) == [0, 1, 2, 3]
# range(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]