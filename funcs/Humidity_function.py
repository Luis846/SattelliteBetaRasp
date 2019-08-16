from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()


while 1:
    humidity = sense.get_humidity()
    print('Humidity: ' + str(round(humidity,2)))
    time.sleep(10)