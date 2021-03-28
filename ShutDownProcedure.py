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

def ShutDownProcedure(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8):

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

    # Shutdown Positions
    Shutdown1 = 100
    Shutdown2 = 130
    Shutdown3 = 120
    Shutdown4 = 100
    Shutdown5 = 20
    Shutdown6 = 120
    Shutdown7 = 100
    Shutdown8 = 85

    #Move to Home position and Check for temperature and voltage errors

    lock = 0 # add LOCK if statement

    servo1.moveTimeWrite(Shutdown1, time=1)
    if servo1.getPhysicalPos() != Shutdown1:
        print('Shutdown Error: servo 1 did not reach Shutdown Position')
        servo1.moveTimeWrite(Shutdown1)
    if servo1.tempRead() > servo1.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo1.vInRead() > max(servo1.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo1.LEDErrorWrite(temp,volt,lock)

    servo2.moveTimeWrite(Shutdown2, time=1)
    if servo2.getPhysicalPos() != Shutdown2:
        print('Shutdown Error: servo 2 did not reach Shutdown Position')
        servo2.moveTimeWrite(Shutdown2)
    if servo2.tempRead() > servo2.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo2.vInRead() > max(servo2.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo2.LEDErrorWrite(temp,volt,lock)

    servo3.moveTimeWrite(Shutdown3, time=1)
    if servo3.getPhysicalPos() != Shutdown3:
        print('Shutdown Error: servo 3 did not reach Shutdown Position')
        servo3.moveTimeWrite(Shutdown3)
    if servo3.tempRead() > servo3.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo3.vInRead() > max(servo3.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo3.LEDErrorWrite(temp,volt,lock)

    servo4.moveTimeWrite(Shutdown4, time=1)
    if servo4.getPhysicalPos() != Shutdown4:
        print('Shutdown Error: servo 4 did not reach Shutdown Position')
        servo4.moveTimeWrite(Shutdown4)
    if servo4.tempRead() > servo4.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo4.vInRead() > max(servo4.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo4.LEDErrorWrite(temp,volt,lock)

    servo5.moveTimeWrite(Shutdown5, time=1)
    if servo5.getPhysicalPos() != Shutdown5:
        print('Shutdown Error: servo 5 did not reach Shutdown Position')
        servo5.moveTimeWrite(Shutdown5)
    if servo5.tempRead() > servo5.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo5.vInRead() > max(servo5.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo5.LEDErrorWrite(temp,volt,lock)

    servo6.moveTimeWrite(Shutdown6, time=1)
    if servo6.getPhysicalPos() != Shutdown6:
        print('Shutdown Error: servo 6 did not reach Shutdown Position')
        servo6.moveTimeWrite(Shutdown6)
    if servo6.tempRead() > servo6.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo6.vInRead() > max(servo6.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo6.LEDErrorWrite(temp,volt,lock)

    servo7.moveTimeWrite(Shutdown7, time=1)
    if servo7.getPhysicalPos() != Shutdown7:
        print('Shutdown Error: servo 7 did not reach Shutdown Position')
        servo7.moveTimeWrite(Shutdown7)
    if servo7.tempRead() > servo7.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo7.vInRead() > max(servo7.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo7.LEDErrorWrite(temp,volt,lock)

    servo8.moveTimeWrite(Shutdown8, time=1)
    if servo8.getPhysicalPos() != Shutdown8:
        print('Shutdown Error: servo 8 did not reach Shutdown Position')
        servo8.moveTimeWrite(Shutdown8)
    if servo8.tempRead() > servo8.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo8.vInRead() > max(servo8.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo8.LEDErrorWrite(temp,volt,lock)
