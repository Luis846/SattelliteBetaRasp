from sense_hat import SenseHat
import time

sense = SenseHat()

file = open('preassure.json', 'w+')
file.write('{ "pu": "pu" }')
file.close()

while 1:
    t = sense.get_temperature()
    print (int(t))
    time.sleep(10)