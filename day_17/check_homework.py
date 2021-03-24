number = int(input('what is number: '))
number1 = 1
line = ''
line1 = ''
while number >= 0:
    line = line + ' ' + str(number)
    number = number - 1
    while number1 <= number + 1:
        line1 = line1 + ' ' + str(number1)
        number1 = number1 + 1
print(line  + line1)