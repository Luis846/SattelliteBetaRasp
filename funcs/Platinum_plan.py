from sense_hat import SenseHat
sense = SenseHat()
import time
from flask import jsonify

def start_measuring():
     while 1:
        
        o = sense.get_orientation()
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()
        raw = sense.get_compass_raw()

           
        t = (t*9/5) + 32
        pitch = o["pitch"] 
        roll = o["roll"]
        yaw = o["yaw"]
        raw_x = raw["x"]
        raw_y= raw["y"]
        raw_z = raw["z"]

        t = round(t, 1)
        p = round(p, 1)
        h = round(h, 1)    

            
            
            
            
            #A dictionary object indexed by the strings x, y and z.
        #The values are Floats representing the magnetic intensity
        #of the axis in microteslas (µT).
        
       
      # Round the values to one decimal place
        
        #pitch = round(pitch,2)
        #roll = round(roll, 2)
        #yaw = round(yaw, 2)
        
      
      # Create the message
      # str() converts the value to a string so it can be concatenated
        print("x: " + str(raw_x) + " y: " + str(raw_y)+ " z: " +str(raw_z) + " µT/Microteslas")
        print("Pitch: {0} Roll: {1} Yaw: {2}".format(pitch, roll, yaw))
        print( "Temp: " + str(round(t)) + " F " + " Pressure: " + str(round(p)) + " Millibars " + "Humidity: " + str(h) + "%")
        
        
        obj = '{"temperature": '+ str(t) + ' , "humidity": '+ str(h) +', "pressure": '+ str(p) +', "pitch": '+ str(pitch) +', "roll": '+ str(roll) +', "yaw": '+ str(yaw) +', "x_axis": '+str(raw_x) +', "y_axis": '+ str(raw_y) +', "z_axis": '+str(raw_z)+'}'
        
        #ob = jsonify(ob)
        #file = open('platinum.json', 'a')
        #file.write('{ "temperature": '+str(t)+'}')
        #contents = file.read('platinum.json')
        #file.close()
       
        #pprint(contents)
        
        file = open('platinum.json', 'a')
        #file.write('{ "temperature": '+str(t)+'}')
        file.write(obj + ',')  
        file.close()
        time.sleep(15)

#start_measuring()

        

     