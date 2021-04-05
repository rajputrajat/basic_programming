numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four'
}

# printing keys
keys = ''
for k in numbers:
    keys += str(k) + ' '
print('only keys 1:', keys)

keys = ''
for k in numbers.keys():
    keys += str(k) + ' '
print('only keys 2:', keys)

# printing values
values = ''
for v_is_just_an_ordinary_variable in numbers.values():
    values += v_is_just_an_ordinary_variable + ' '
print('values:', values)

# printing both keys and values
pair = ''
for m, n in numbers.items():
    pair += '(' + str(m) + ' ' + n + ')' + ' '
print(pair)