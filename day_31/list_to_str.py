num = 1223
nstr = str(1223)
nlist = list(nstr)
assert(nlist == ['1', '2', '2', '3'])

str_again = ''
for c in nlist:
    str_again += c

assert(str_again == nstr)

print('passed')
