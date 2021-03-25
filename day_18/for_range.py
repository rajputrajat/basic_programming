char = input('which character: ')
times = int(input('how many times: '))

for a in range(times):
    print((char + ' ') * (a + 1))

# range(4) == [0, 1, 2, 3]
# range(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]