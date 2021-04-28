# https://www.w3resource.com/python-exercises/python-basic-exercises.php
# string formatting
# python doc link for string formatting:
# https://docs.python.org/3/library/string.html?highlight=string%20format

var1 = 100
var2 = 'hello there!'
var_float = 10.03

var3 = f'{var2} can you give me {var_float:.4f} rs.'
print(var3)
var4 = var2 + ' can you give me ' + str(var1) + ' rs.'

assert(var3 == 'hello there! can you give me 10.0300 rs.')
assert(var4 == 'hello there! can you give me 100 rs.')

names = ['ira', 'akku', 'rainbow', 'rainbee', 'maharani slushi ji ek sau aath']
bank_balance = [5, 12, 0.5, 50, 100000]

for n, b in zip(names, bank_balance):
    print(f'{n} : {b}')

print()
print()

for n, b in zip(names, bank_balance):
    print(f'{n:>40} : {b:>10.2f}')

print()
print()

for n, b in zip(names, bank_balance):
    print(f'{n:<40} : {b:<10.2f}')

print()
print()

for n, b in zip(names, bank_balance):
    print(f'{n:^40} : {b:^10.2f}')
