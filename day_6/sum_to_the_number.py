number = int(input("enter the number: "))
orig_number = number

sum = 0
print('sum = ', sum)
while number >= 1:
    sum = number + sum
    print('sum = ', sum)
    number = number - 1
    print('number = ', number)

print("sum of numbers from 1 to ", orig_number, " is ", sum)