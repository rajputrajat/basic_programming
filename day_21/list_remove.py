a = [10, 20, 30, 20, 10, 100, 10]
print(a)
a.extend([10, 40])
print(a)
print('count of 10', a.count(10))
a.remove(10)
print('after removing 10 and before pop:', a)

# list pop
b = a.pop() # this should return last item form this list
print('after pop:', a)
print('popped item:', b)

# list pop specific
c = a.pop(2) # this should return third item form this list
print('after pop:', a)
print('popped item:', c)

a.reverse()
print('after reverse:', a)

a.sort()
print('sorted:', a)