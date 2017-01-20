import RPi.GPIO as GPIO
import time

Rpin = 11
Bpin = 13
Gpin = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(Rpin,GPIO.OUT)
GPIO.setup(Bpin,GPIO.OUT)
GPIO.setup(Gpin,GPIO.OUT)


red = GPIO.PWM(Rpin,5)
blue = GPIO.PWM(Bpin,5)
green = GPIO.PWM(Gpin,5)


red.start(100)
green.start(100)
blue.start(100)


def led_light(r1,b1,g1):

 COUNT = 10

 for _ in xrange(0,COUNT):
   red.ChangeDutyCycle(r1)
   blue.ChangeDutyCycle(b1)
   green.ChangeDutyCycle(g1)
   time.sleep(2)
   GPIO.output(Rpin,GPIO.LOW)
   GPIO.output(Bpin,GPIO.LOW)
   GPIO.output(Gpin,GPIO.LOW)
   time.sleep(0.5)

 red.stop()
 blue.stop()
 green.stop()

 GPIO.cleanup()


state = 3

#stop
if state == 1:
  led_light(50,50,0)

#turn
elif state == 2:
  led_light(50,50,50)

#slow
elif state == 3:
  led_light(0,50,50)

#fast
elif state == 4:
  led_light(0,100,50)

#avoid
elif state == 5:
  led_light(50,0,50)
