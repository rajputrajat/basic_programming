a = (1, 2, 3)

b = [1, 2, 3]

assert(b[0] == 1)
b[0] += 1
assert(b[0] == 2)
assert(b == [2, 2, 3])

b.append(100)
assert(b == [2, 2, 3, 100])

a[0] += 1
assert(a == (2, 2, 3))
