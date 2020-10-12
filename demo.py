from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm1 = Adafruit_PCA9685.PCA9685(address=0x41)
pwm2 = Adafruit_PCA9685.PCA9685(address=0x42)


# servo_mid1 = 370  
# servo_min1 = 320
# servo_max1 = 420  

#press
servo_mid1 = 390  
servo_min1 = 320
servo_max1 = 420  

#pluck
servo_min2 = 310  
servo_max2 = 410  

#initalize
pwm2.set_all_pwm(0, 410)
strings = [[0,0], [1,1], [2,1], [3,1], [4,1], [5,1], [6,1]]

pwm1.set_pwm(0, 0, 360)
pwm1.set_pwm(1, 0, 340)
pwm1.set_pwm(2, 0, 350)
pwm1.set_pwm(3, 0, 350)
pwm1.set_pwm(4, 0, 350)
pwm1.set_pwm(5, 0, 350)
pwm1.set_pwm(6, 0, 350)
pwm1.set_pwm(7, 0, 350)
pwm1.set_pwm(8, 0, 295)
pwm1.set_pwm(9, 0, 420)
pwm1.set_pwm(10, 0, 350)

time.sleep(1)

speed = 70 
beat = 70/60

pwm1.set_pwm_freq(60)
pwm2.set_pwm_freq(60)

def pluck(string):
    if(strings[string][1]):
        pwm2.set_pwm(string, 0, 310)
        strings[string][1] = 0
    else:
        pwm2.set_pwm(string, 0, 410)
        strings[string][1] = 1
        
def e2(time_wait):
    pluck(1)
    time.sleep(time_wait)

def a2(time_wait):
    pluck(2)
    time.sleep(time_wait)

def d3(time_wait):
    pluck(3)
    time.sleep(time_wait)

def g3(time_wait):
    pluck(4)
    time.sleep(time_wait)

def b3(time_wait): 
    pluck(5)
    time.sleep(time_wait)

def e4(time_wait):   
    pluck(6)
    time.sleep(time_wait)


def f2(time_wait):
    pwm1.set_pwm(0, 0, 300)
    time.sleep(0.15)
    pluck(1)
    time.sleep(time_wait)
    pwm1.set_pwm(0, 0, 350)

def b2(time_wait):   
    pwm1.set_pwm(1, 0, 410)
    time.sleep(0.15)
    pluck(2)
    time.sleep(time_wait)
    pwm1.set_pwm(1, 0, 350)

def g2(time_wait):   
    pwm1.set_pwm(6, 0, 250)
    time.sleep(0.15)
    pluck(1)
    time.sleep(time_wait)
    pwm1.set_pwm(6, 0, 350)

def c3(time_wait):   
    pwm1.set_pwm(7, 0, 260)
    time.sleep(0.15)
    pluck(2)
    time.sleep(time_wait)
    pwm1.set_pwm(7, 0, 350)

def e3(time_wait):    
    pwm1.set_pwm(2, 0, 405)
    time.sleep(0.15)
    pluck(3)
    time.sleep(time_wait)
    pwm1.set_pwm(2, 0, 350)
    
def f3(time_wait):   
    pwm1.set_pwm(8, 0, 250)
    time.sleep(0.15)
    pluck(3)
    time.sleep(time_wait)
    pwm1.set_pwm(8, 0, 300)

def a3(time_wait):    
    pwm1.set_pwm(3, 0, 330)
    time.sleep(0.15)
    pluck(4)
    time.sleep(time_wait)
    pwm1.set_pwm(3, 0, 350)

def c4(time_wait):    
    pwm1.set_pwm(4, 0, 420)
    time.sleep(0.15)
    pluck(5)
    time.sleep(time_wait)
    pwm1.set_pwm(4, 0, 350)

def d4(time_wait):    
    pwm1.set_pwm(9, 0, 460)
    time.sleep(0.15)
    pluck(5)
    time.sleep(time_wait)
    pwm1.set_pwm(9, 0, 420)

def f4(time_wait):    
    pwm1.set_pwm(5, 0, 480)
    time.sleep(0.15)
    pluck(6)
    time.sleep(time_wait)
    pwm1.set_pwm(5, 0, 400)

def g4(time_wait):    
    pwm1.set_pwm(10, 0, 385)
    time.sleep(0.15)
    pluck(6)
    time.sleep(time_wait)
    pwm1.set_pwm(10, 0, 350)



c3(0.5)
d3(0.5)
e3(0.5)
f3(0.5)
g3(0.5)
a3(0.5)
b3(0.5)
c4(0.5)
c4(0.5)
b3(0.5)
a3(0.5)
g3(0.5)
f3(0.5)
e3(0.5)
d3(0.5)
c3(0.5)

c3(0.25)
d3(0.25)
e3(0.25)
f3(0.25)
g3(0.25)
a3(0.25)
b3(0.25)
c4(0.25)
c4(0.25)
b3(0.25)
a3(0.25)
g3(0.25)
f3(0.25)
e3(0.25)
d3(0.25)
c3(0.25)

c3(0.125)
d3(0.125)
e3(0.125)
f3(0.125)
g3(0.125)
a3(0.125)
b3(0.125)
c4(0.125)
c4(0.125)
b3(0.125)
a3(0.125)
g3(0.125)
f3(0.125)
e3(0.125)
d3(0.125)
c3(0.125)


c3(0.25)
d3(0.25)
e3(0.25)
f3(0.25)
g3(0.25)
a3(0.25)
b3(0.25)
c4(0.25)
c4(0.25)
b3(0.25)
a3(0.25)
g3(0.25)
f3(0.25)
e3(0.25)
d3(0.25)
c3(0.25)

c3(0.5)
d3(0.5)
e3(0.5)
f3(0.5)
g3(0.5)
a3(0.5)
b3(0.5)
c4(0.5)
c4(0.5)
b3(0.5)
a3(0.5)
g3(0.5)
f3(0.5)
e3(0.5)
d3(0.5)
c3(0.5)

