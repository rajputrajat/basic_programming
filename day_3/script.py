# DO NOT WORRY ABOUT BELOW TEXT FOR NOW
def read_temperature():
    return 34.99999999999
def turn_on_air_conditioner():
    print("thanda-thanda cool-cool")
def turn_on_heater():
    print("heater is on")
def turn_on_fan():
    print("fans layak to garmi ho gayi hai")
def turn_on_tv():
    print("cartoon lagao tv pe")
def going_to_sleep():
    print("good night")

name = 'Hemal'
if name == 'Vinay':
    print('hi vinay')
elif name == 'Shubham':
    print('where is Vinay, Shubham?')
else:
    print('kahan hain donon kaam-chor')

temp = read_temperature()
if temp <= 20.0:
    turn_on_heater()
elif temp >= 35.0:
    turn_on_air_conditioner()
elif temp >= 30.0:
    turn_on_fan()
else:
    turn_on_tv()
going_to_sleep()