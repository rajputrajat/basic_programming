# loop will run 6 times. if condition will fail in first go. and 5 will be printed.
var1 = 20
var2 = 20
counter = 0
while var2 <= 25 and var1 > 0:
    if var2 > var1:
        counter += 1
    var2 += 1
    var1 -= 1
print(counter)


# loop will run 5 times. and 6 will be printed
# var1 = 15
# var2 = 15
# counter = 1
# while var1 > 0 and var2 < 20:
#     var1 -= 1
#     var2 += 1 
#     counter += 1
# print(counter)

# 20 will be printed
# var = 25
# if var < 30:
#     while var > 20:
#         var -= 1
# print(var)

# this will not print anything. the while loop will run forever.
# var = 25
# if var < 30:
#     while var > 20:
#         var += 1
# print(var)