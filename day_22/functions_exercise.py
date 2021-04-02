# take - how many numbers in a list
# take individual number, and create a list
# print that list
# find out maximum and minimum number in that list

def make_list():
    count = int(input('how many numbers: '))
    numbers = []
    for n in range(count):
        num = int(input('enter number: '))
        numbers.append(num)
    return numbers

def print_min_max(a_list):
    max = a_list[0]
    min = a_list[0]
    for num in a_list:
        if num > max:
            max = num
        if num < min:
            min = num
    print('max:', max)
    print('min:', min)

# actual python excution starts from below
# list_of_numbers = make_list()
# print(list_of_numbers)
# print_min_max(list_of_numbers)

print_min_max([10, 23, -1, 20])

b_list = [10.2, 43.0, -0.2]
print_min_max(b_list)