import RPi.GPIO as GPIO
import time

Rpin = 11
Bpin = 13
Gpin = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(Rpin,GPIO.OUT)
GPIO.setup(Bpin,GPIO.OUT)
GPIO.setup(Gpin,GPIO.OUT)

red = GPIO.PWM(Rpin,50)
green = GPIO.PWM(Gpin,50)
blue = GPIO.PWM(Bpin,50)

red.start(30)
green.start(50)
blue.start(100)


COUNT = 100
T = 0.04
I = 0

time.sleep(2)

for _ in xrange(0, COUNT):
    red.ChangeDutyCycle(I)
    blue.ChangeDutyCycle(100 - I)
    time.sleep(T)
    I += 1

I = 0

for _ in xrange(0, COUNT):
    red.ChangeDutyCycle(100-I)
    green.ChangeDutyCycle(I)
    I+=1
    time.sleep(T)

I = 0

for _ in xrange(0, COUNT):
    green.ChangeDutyCycle(100 - I)
    blue.ChangeDutyCycle(I)
    I+=1
    time.sleep(T)


for _ in xrange(0, COUNT):
    red.ChangeDutyCycle(30)
    green.ChangeDutyCycle(50)
    blue.ChangeDutyCycle(70)
    time.sleep(T)



time.sleep(0.5)

red.stop()
green.stop()
blue.stop()

GPIO.cleanup()

