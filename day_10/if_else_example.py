days = int(input("how many days are there in this month: "))
if days == 31:
    print("jan, mar, may, jul, aug, oct, dec")
elif days == 28 or days == 29:
    print("feb")
elif days == 30:
    print("apr, jun, sep, nov")
else:
    print("invalid input")

a = input("doesn't matter")