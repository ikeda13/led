#!/usr/bin/python
# -*- coding: utf-8 -*-
# License removed for brevity

import rospy
from ros_electro.msg import Length
import RPi.GPIO as GPIO
import time
#from ros_electro.msg import Rstate


Rpin = 11
Bpin = 13
Gpin = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(Rpin,GPIO.OUT)
GPIO.setup(Bpin,GPIO.OUT)
GPIO.setup(Gpin,GPIO.OUT)

red = GPIO.PWM(Rpin,60)
blue = GPIO.PWM(Bpin,60)
green = GPIO.PWM(Gpin,60)


red.start(100)
green.start(100)
blue.start(100)


#sensor
def S_callback(sdata):
 #0-7
 state = sdata.l


 if state == 0:
   led_light(0,100,0)

# elif state == 1:
#   led_light(50,50,50)

# elif state == 2:
#   led_light(0,50,50)

# elif state == 3:
#   led_light(70,50,50)

# elif state == 4:
#   led_light(50,0,50)

# elif state == 5:
#   led_light(0,50,50)
 
 elif state == 6:
   led_light(100,100,0)

 elif state == 7:
   led_light(100,0,0)
 


def led_light(r1,b1,g1):

 
 red.ChangeDutyCycle(r1)
 blue.ChangeDutyCycle(b1)
 green.ChangeDutyCycle(g1)
 time.sleep(0.5)
# GPIO.output(Rpin,GPIO.LOW)
# GPIO.output(Bpin,GPIO.LOW)
# GPIO.output(Gpin,GPIO.LOW)




def light():
 rospy.init_node('light',anonymous = True)

 rospy.Subscriber('Sensor', Length, S_callback)
 
 rospy.spin()



if __name__ == '__main__':
  light()

  GPIO.cleanup()
