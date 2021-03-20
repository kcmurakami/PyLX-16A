from lx16a import *
from math import sin, cos
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize('/dev/ttyUSB0')

servo1 = LX16A(1)
servo2 = LX16A(2)
servo3 = LX16A(3)
servo4 = LX16A(4)
servo5 = LX16A(5)
servo6 = LX16A(6)
servo7 = LX16A(7)
servo8 = LX16A(8)
t = 0

#Query Initial Motor position
init1 = servo1.getPhysicalPos()
init2 = servo2.getPhysicalPos()
init3 = servo3.getPhysicalPos()
init4 = servo4.getPhysicalPos()
init5 = servo5.getPhysicalPos()
init6 = servo6.getPhysicalPos()
init7 = servo7.getPhysicalPos()
init8 = servo8.getPhysicalPos()

#Move to Home position and Check for temperature and voltage errors

lock = 0 # add LOCK if statement

servo1.moveTimeWrite(100)
if servo1.tempRead() > servo1.tempMaxLimitRead():
    temp = 1
else:
    temp = 0
if servo1.vInRead() > max(servo1.vInLimitRead()):
    volt = 1
else:
    volt = 0
servo1.LEDErrorWrite(temp,volt,lock)

servo2.moveTimeWrite(130)
if servo2.tempRead() > servo2.tempMaxLimitRead():
    temp = 1
else:
    temp = 0
if servo2.vInRead() > max(servo2.vInLimitRead()):
    volt = 1
else:
    volt = 0
servo2.LEDErrorWrite(temp,volt,lock)

servo3.moveTimeWrite(120)
if servo3.tempRead() > servo3.tempMaxLimitRead():
    temp = 1
else:
    temp = 0
if servo3.vInRead() > max(servo3.vInLimitRead()):
    volt = 1
else:
    volt = 0
servo3.LEDErrorWrite(temp,volt,lock)

servo4.moveTimeWrite(100)
if servo4.tempRead() > servo4.tempMaxLimitRead():
    temp = 1
else:
    temp = 0
if servo4.vInRead() > max(servo4.vInLimitRead()):
    volt = 1
else:
    volt = 0
servo4.LEDErrorWrite(temp,volt,lock)

servo5.moveTimeWrite(20)
if servo5.tempRead() > servo5.tempMaxLimitRead():
    temp = 1
else:
    temp = 0
if servo5.vInRead() > max(servo5.vInLimitRead()):
    volt = 1
else:
    volt = 0
servo5.LEDErrorWrite(temp,volt,lock)

servo6.moveTimeWrite(120)
if servo6.tempRead() > servo6.tempMaxLimitRead():
    temp = 1
else:
    temp = 0
if servo6.vInRead() > max(servo6.vInLimitRead()):
    volt = 1
else:
    volt = 0
servo6.LEDErrorWrite(temp,volt,lock)

servo7.moveTimeWrite(100)
if servo7.tempRead() > servo7.tempMaxLimitRead():
    temp = 1
else:
    temp = 0
if servo7.vInRead() > max(servo7.vInLimitRead()):
    volt = 1
else:
    volt = 0
servo7.LEDErrorWrite(temp,volt,lock)

servo8.moveTimeWrite(85)
if servo8.tempRead() > servo8.tempMaxLimitRead():
    temp = 1
else:
    temp = 0
if servo8.vInRead() > max(servo8.vInLimitRead()):
    volt = 1
else:
    volt = 0
servo8.LEDErrorWrite(temp,volt,lock)
