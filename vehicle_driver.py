
"""vehicle_driver controller."""

import math
from controller import Lidar
from vehicle import Driver
from controller import Robot
from controller import Camera

#lidar = Lidar()


drive= Driver()    
camera= drive.getCamera('camera')
camera.enable(50)
#camera.hasRecognition()
#camera.recognitionEnable(300)
#robot.setSteeringAngle(.4)





#drive.setSteeringAngle(0)
drive.setCruisingSpeed(30)

timestep = int(drive.getBasicTimeStep())

step = 0
while drive.step() != -1:
    #if step==100:
        image = camera.getImageArray()
# display the components of each pixel
        for y in range(0,camera.getWidth()):
            for x in range(0,camera.getHeight()):
                #print(' ')
                #print('x= '+str(x))
                red   = image[x][y][0]
                green = image[x][y][1]
                blue  = image[x][y][2]
                gray  = (red + green + blue) / 3
                if y== 50 and x <30 and red >100 :
                    factor = 30-x
                    drive.setSteeringAngle(-factor*(0.003))
                    #print("turn left")
                if y== 50 and x >35 and red >100 :
                    factor= x-40
                    turn = int(factor)*float((.003))
                    drive.setSteeringAngle(turn)
                    #print("turn right"+ str(float(factor)*float((.2))))    
                #print 'r='+str(red)+' g='+str(green)+' b='+str(blue)
            #print('LINE '+str(x)+' ends')
        #print("END!!!!!!!!!!!!!!!!!!!!")
        step=step+1
        pass

    #print(step)
    #if step == 275:
       #drive.setSteeringAngle(.08)
       
    #if step == 350:
       #drive.setSteeringAngle(-.04)  
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  led.set(1)
   # print(ca.getRecognitionObjects())
     
