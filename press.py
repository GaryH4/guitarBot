# encoding=utf-8
# press.py
# 压弦部分的控制

from smbus2 import SMBus
from PCA9685 import PWM #从PCA9685引入PWM
import time

fPWM = 50
a = 8.5 # 与舵机相匹配
b = 2  # 与舵机相匹配

i2c_addressL = 0x41
i2c_addressR = 0x40

def setupServoL():
    global pwmL
    bus = SMBus(1) # Raspberry Pi revision 2
    pwmL = PWM(bus, i2c_addressL)
    pwmL.setFreq(fPWM)

def setupServoR():
    global pwmR
    bus = SMBus(1) # Raspberry Pi revision 2
    pwmR = PWM(bus, i2c_addressR)
    pwmR.setFreq(fPWM)

def setDirectionL(self, direction):
    duty = a / 180 * direction + b
    pwmL.setDuty(self.channel, duty)

def setDirectionR(self, direction):
    duty = a / 180 * direction + b
    pwmR.setDuty(self.channel, duty)

class servoL:
    def __init__(self,string,fret):
        self.fret = fret
        self.string = string
        self.channel = string + 6*(fret-1) - 1 #先弦后品,0开始计数 #TODO:需要两个驱动板，9*2来控制18个舵机
        if(setDirectionL(self, 90)!=None):
            print("initiated servoL",str(string)+str(fret))

    def press(self, time_wait):
        if(self.fret == 0):
            setDirectionL(self, 90)
        elif(self.fret % 2 == 1):#奇数品
            setDirectionL(self, 120)#根据实际的舵机安装方向调整角度
        elif(self.fret % 2 == 0):#偶数品
            setDirectionL(self, 60)
        time.sleep(time_wait)#TODO:等待duration计算后的值
        setDirectionL(self, 90)#复位
        

class servoR:
    def __init__(self,string):
        self.channel = string - 1
        self.pluck_status = False
        if(setDirectionR(self, 70) != None):
            print("initiated servoR"+str(string))
    
    def pluck(self):
        if(self.pluck_status == False):
            setDirectionR(self, 100)
            self.pluck_status = True
        else:
            setDirectionR(self, 70)
            self.pluck_status = False


def trigger(pitch, keep_time, servoLs, servoRs):  #TODO:complete the mapping of pitches, and make this more elegant
    #string 1:
    if(pitch=="E2"):
        servoRs[1].pluck()
    elif(pitch=="F2"):
        servoLs[1][1].press(keep_time)
        servoRs[1].pluck()
    elif(pitch=="G2"):
        servoLs[1][2].press(keep_time)
        servoRs[1].pluck()
    elif(pitch=="A2"):
        servoLs[1][5].press(keep_time)
        servoRs[1].pluck()
    #string 2:
    elif(pitch=="B2"):
        servoLs[2][2].press(keep_time)
        servoRs[2].pluck()
    elif(pitch=="C3"):
        servoLs[2][3].press(keep_time)#TODO:time_wait
        servoRs[2].pluck()
    #string 3
    elif(pitch=="D3"):
        servoRs[3].pluck()
    elif(pitch=="E3"):
        servoLs[3][2].press(keep_time)
        servoRs[3].pluck()
    elif(pitch=="F3"):
        servoLs[3][3].press(keep_time)
        servoRs[3].pluck()
    #string 4
    elif(pitch=="G3"):
        servoRs[4].pluck()
    elif(pitch=="A3"):
        servoLs[4][2].press(keep_time)
        servoRs[4].pluck()
    #string 5
    elif(pitch=="B3"):
        servoRs[5].pluck()
    elif(pitch=="C4"):
        servoLs[5][1].press(keep_time)
        servoRs[5].pluck()
    elif(pitch=="D4"):
        servoLs[5][3].press(keep_time)
        servoRs[5].pluck()
    #string 6
    elif(pitch=="E4"):
        servoRs[6].pluck()
    elif(pitch=="F4"):
        servoLs[6][1].press(keep_time)
        servoRs[6].pluck()
    elif(pitch=="G4"):
        servoLs[6][3].press(keep_time)
        servoRs[6].pluck()
    elif(pitch=="A4"):
        servoLs[6][5].press(keep_time)
        servoRs[6].pluck()
    print(pitch,"triggered")





  