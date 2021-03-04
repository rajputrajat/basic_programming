number_from = int(input("number from: "))
number_to = int(input("number to: "))

counter = number_from

sum = 0

while counter <= number_to:
    sum = sum + counter
    counter = counter + 1

print('sum from ', number_from, ' to ', number_to, ' is ', sum)