# encoding=utf-8
# play.py
# 主程序

from press import *
from xml.dom import minidom
import enhancedminidom
import time

#init
filename="/home/pi/servo/lg-202876558.xml" #TODO: convert from mxl to xml
queue=[]


setupServoL() #string,fret
# servoLs = [ [], #按弦部分的
#             [0, servoL(1,1), servoL(1,2), servoL(1,3), servoL(1,4), servoL(1,5), servoL(1,6)], #1弦 
#             [0, servoL(2,1), servoL(2,2), servoL(2,3), servoL(2,4), servoL(2,5), servoL(2,6)], #2弦
#             [0, servoL(3,1), servoL(3,2), servoL(3,3), servoL(3,4), servoL(3,5), servoL(3,6)], #3弦
#             [0, servoL(4,1), servoL(4,2), servoL(4,3), servoL(4,4), servoL(4,5), servoL(4,6)], #4弦
#             [0, servoL(5,1), servoL(5,2), servoL(5,3), servoL(5,4), servoL(5,5), servoL(5,6)], #5弦
#             [0, servoL(6,1), servoL(6,2), servoL(6,3), servoL(6,4), servoL(6,5), servoL(6,6)]  #6弦
#         ]没意义

setupServoR()
servoRs = [0,servoR(1),servoR(2),servoR(3),servoR(4),servoR(5),servoR(6)]
#init done

#process XML file
#TODO:xml解析，装载到queue列表（二维），计算每小节的时间，分小节（measure）同时按压弦，时序拨弦
queue=[[0]] #init 0是占位符

scoreFile = minidom.parse(filename)
score = scoreFile.documentElement
measures=score.getElementsByTagName("measure")
speed=score.getElementsByTagName("per-minute")
if(speed==None):
    speed=60 #default 60 beats per minute


for measure in measures:
    measure_list = []
    measure_list.append(int(measure.getAttribute("number")))
    notes = measure.getElementsByTagName("note")
    for note in notes:
        note_list = []
        if(note.getElementsByTagName("rest")!=[]):
            note_list.append("rest")
        else:
            step = note.getElementsByTagName("step")[0].childNodes[0].data
            octave = note.getElementsByTagName("octave")[0].childNodes[0].data
            note_list.append(step+octave)
        duration = int(note.getElementsByTagName("duration")[0].childNodes[0].data)
        note_list.append(duration)
        measure_list.append(note_list)
    queue.append(measure_list)




while(queue):
    pitch_play=queue.pop(0)
    trigger(pitch_play[0], pitch_play[1], servoLs, servoRs)


