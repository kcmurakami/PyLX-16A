from lx16a import *
"""
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
"""

def BootSelfTest(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8):

    #Query Initial Motor position
    init1 = servo1.getPhysicalPos()
    if type(init1) != 'int':
        print('Com Error: servo 1 is of type ', type(init1))
    init2 = servo2.getPhysicalPos()
    if type(init2) != 'int':
        print('Com Error: servo 2 is of type ', type(init2))
    init3 = servo3.getPhysicalPos()
    if type(init3) != 'int':
        print('Com Error: servo 3 is of type ', type(init3))
    init4 = servo4.getPhysicalPos()
    if type(init4) != 'int':
        print('Com Error: servo 4 is of type ', type(init4))
    init5 = servo5.getPhysicalPos()
    if type(init5) != 'int':
        print('Com Error: servo 5 is of type ', type(init5))
    init6 = servo6.getPhysicalPos()
    if type(init6) != 'int':
        print('Com Error: servo 6 is of type ', type(init6))
    init7 = servo7.getPhysicalPos()
    if type(init7) != 'int':
        print('Com Error: servo 7 is of type ', type(init7))
    init8 = servo8.getPhysicalPos()
    if type(init8) != 'int':
        print('Com Error: servo 8 is of type ', type(init8))

    #Check that each motor is receiving sufficient power
    temp = 0
    lock = 0
    if servo1.vInRead() < min(servo1.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo1.LEDErrorWrite(temp,volt,lock)
    if servo2.vInRead() < min(servo2.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo2.LEDErrorWrite(temp,volt,lock)
    if servo3.vInRead() < min(servo3.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo3.LEDErrorWrite(temp,volt,lock)
    if servo4.vInRead() < min(servo4.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo4.LEDErrorWrite(temp,volt,lock)
    if servo5.vInRead() < min(servo5.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo5.LEDErrorWrite(temp,volt,lock)
    if servo6.vInRead() < min(servo6.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo6.LEDErrorWrite(temp,volt,lock)
    if servo7.vInRead() < min(servo7.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo7.LEDErrorWrite(temp,volt,lock)
    if servo8.vInRead() < min(servo8.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo8.LEDErrorWrite(temp,volt,lock)

    #Flash each motor LED 3 times
    for i in 8:
        for k in 3:
            LX16A(i),LEDErrorWrite(1,0,0)
        print('servo{} LED Flashing'.format(i))
