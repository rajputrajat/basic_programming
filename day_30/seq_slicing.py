a = 'hello there'
assert(a == 'hello there')

b = a[0:4]
assert(b == 'hell')

c = a[5:7]
assert(c == ' t')

d = a[1:8:2]
assert(d == 'el h')

e = a[-2]
assert(e == 'r')

f = a[2: -2]
assert(f == 'llo the')

g = a[-1:-4:-1]
assert(g == 'ere')

h = [2, 34, 200, 4, 2032]
assert(h[-3] == 200)
assert(h[1:-2] == [34, 200])

i = 221
assert(type(i) == int)
j = str(i)
assert(type(j) == str)
k = int(j)
assert(k == i)
assert(type(k) == type(i))

print('passed')
