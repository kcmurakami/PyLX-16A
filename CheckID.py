from lx16a import *

LX16A.initialize('/dev/ttyUSB0')

servo1 = LX16A(1) # right wing
servo2 = LX16A(2) # back right leg
servo3 = LX16A(3) # front right leg
servo4 = LX16A(4) # front left leg
servo5 = LX16A(5) # back left leg
servo6 = LX16A(6) # left wing
servo7 = LX16A(7) # neck
servo8 = LX16A(8) # head


"""print('servo current physical position:',servo1.getPhysicalPos())
print('servo current virtual position:',servo1.getVirtualPos())
print('angle offset adjust by -20')
servo1.angleOffsetAdjust(-20)
print('servo after offset physical position:',servo1.getPhysicalPos())
print('servo after offset virtual position:',servo1.getVirtualPos())
#servo1.moveTimeWrite(-10, time=5000)"""

#print(servo.IDRead())