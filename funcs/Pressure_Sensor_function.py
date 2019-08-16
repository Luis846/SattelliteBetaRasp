from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

#Atmospheric Pressure /PSI

while 1:
    
    pressure = sense.get_pressure()
    print('PSI: ' + str(pressure))
    time.sleep(10)
    