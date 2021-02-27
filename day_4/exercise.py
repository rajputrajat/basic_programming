temp = input("what is the current temperature: ")
temp_in_int = int(temp)
if temp_in_int < 20:
    print('turn on heater')
else:
    print('turn on air-conditioner')