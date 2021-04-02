def calculator(a, b, operation):
    if 'sum' == operation:
        return a + b
    elif 'sub' == operation:
        return a - b
    elif 'mul' == operation:
        return a * b
    elif 'div' == operation:
        return a / b
    else:
        print('wrong operation')

var_1 = calculator(10, 5, 'mul')
print(var_1)

print(calculator(100, 20, 'div'))