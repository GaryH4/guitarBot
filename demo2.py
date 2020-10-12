import serial    


ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)   #1s timeout

#press

queue = []

try:
  while(queue):
    ser.write(queue.pop())
    response = ser.readall()
    print(response)
except:
    ser.close()