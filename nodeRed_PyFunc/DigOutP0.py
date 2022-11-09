from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

import piplates.DAQCplate as DAQC
port = 0
for port in range(0, 7):
    DAQC.setDOUTbit(0, port)
    sleep(.5)
    DAQC.clrDOUTbit(0, port)
    sleep(.5)
port = 0
pwm1 = GPIO.PWM(21,500)
pwm2 = GPIO.PWM(20,600)
pwm3 = GPIO.PWM(16,700)
pwm4 = GPIO.PWM(12,800)
pwm5 = GPIO.PWM(26,900)
pwm6 = GPIO.PWM(19,1000)

pwm1.start(100)
pwm2.start(75) #Channel1
pwm3.start(60) #Channel2
pwm4.start(50) #Channel3
pwm5.start(35) #Channel5
pwm6.start(25) #Channel6
sleep(40)
