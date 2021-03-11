num_fruits = int(input('how many fruits did you buy today: '))
print()

cost = 0.0
while num_fruits >= 1:
    num_fruits = num_fruits - 1

    name = input('name of fruit: ')
    weight_input = 'how much ' + name + ' did you buy: '
    weight = float(input(weight_input))
    rate = float(input('cost of ' + name + ' rs/kg: '))
    cost = cost + (rate * weight)
    print()

print('you spent: ' + str(cost) + ' Rs')