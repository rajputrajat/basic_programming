def find_smallest_largest_number(a):
    s = a[0]
    l = a[0]
    for n in a:
        if n < s:
            s = n
        if n > l:
            l = n
    return [s, l]

def find_shortest_longest_sequence(a):
    s = a[0]
    l = a[0]
    for n in a:
        if len(n) < len(s):
            s = n
        if len(n) > len(l):
            l = n
    return [s, l]

######################################################

a_list = ['hi', 'bye', 'kya hai', 'naa hai bhai', 'z', ' jayen']
print(find_shortest_longest_sequence(a_list))

b_list = [-2, 10, 54, 38, 23, 101]
print(find_smallest_largest_number(b_list))

c_list = [2.9, -0.3, -0.002, 0.00001, 4000.324, 32.0]
print(find_smallest_largest_number(c_list))

d_list = [[1], [], [2, 0, 4], [2, 3], [0]]
print(find_shortest_longest_sequence(d_list))