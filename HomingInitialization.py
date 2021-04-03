from lx16a import *
from math import sin, cos
import time


def HomingInitialization(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8):

    #Query Initial Motor position
    init1 = servo1.getPhysicalPos()
    if isinstance(init1, int) == False:
        print('Com Error: servo 1 is of type ', type(init1))
    init2 = servo2.getPhysicalPos()
    if isinstance(init2, int) == False:
        print('Com Error: servo 2 is of type ', type(init2))
    init3 = servo3.getPhysicalPos()
    if isinstance(init3, int) == False:
        print('Com Error: servo 3 is of type ', type(init3))
    init4 = servo4.getPhysicalPos()
    if isinstance(init4, int) == False:
        print('Com Error: servo 4 is of type ', type(init4))
    init5 = servo5.getPhysicalPos()
    if isinstance(init5, int) == False:
        print('Com Error: servo 5 is of type ', type(init5))
    init6 = servo6.getPhysicalPos()
    if isinstance(init6, int) == False:
        print('Com Error: servo 6 is of type ', type(init6))
    init7 = servo7.getPhysicalPos()
    if isinstance(init7, int) == False:
        print('Com Error: servo 7 is of type ', type(init7))
    init8 = servo8.getPhysicalPos()
    #init8 = 84
    if isinstance(init8, int) == False:
        print('Com Error: servo 8 is of type ', type(init8))

    # Home Positions
    Home1 = 110
    Home2 = 88   # back right - to rotate back, subtract
    Home3 = 128   # front right - to rotate back, subtract
    Home4 = 124   # front left - to rotate back, add
    Home5 = 122   # back left - to rotate back, add
    Home6 = 120
    Home7 = 100
    Home8 = 85

    # Move to Home Position
    servo1.moveTimeWrite(Home1, time=1000)
    servo2.moveTimeWrite(Home2, time=1000)
    servo3.moveTimeWrite(Home3, time=1000)
    servo4.moveTimeWrite(Home4, time=1000)
    servo5.moveTimeWrite(Home5, time=1000)
    servo6.moveTimeWrite(Home6, time=1000)
    servo7.moveTimeWrite(Home7, time=1000)
    servo8.moveTimeWrite(Home8, time=1000)
    time.sleep(1)

    #Move to Home position and Check for temperature and voltage errors

    lock = 0 # add LOCK if statement


    if not Home1-5 < servo1.getPhysicalPos() < Home1+5:
        print('Homing Error: servo 1:', servo1.getPhysicalPos())
        servo1.moveTimeWrite(Home1)
    if servo1.tempRead() > servo1.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo1.vInRead() > max(servo1.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo1.LEDErrorWrite(temp,volt,lock)


    if not Home2-5 < servo2.getPhysicalPos() < Home2+5:
        print('Homing Error: servo 2:', servo2.getPhysicalPos())
        servo2.moveTimeWrite(Home2)
    if servo2.tempRead() > servo2.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo2.vInRead() > max(servo2.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo2.LEDErrorWrite(temp,volt,lock)


    if not Home3-5 < servo3.getPhysicalPos() < Home3+5:
        print('Homing Error: servo 3:', servo3.getPhysicalPos())
        servo3.moveTimeWrite(Home3)
    if servo3.tempRead() > servo3.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo3.vInRead() > max(servo3.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo3.LEDErrorWrite(temp,volt,lock)


    if not Home4-5 < servo4.getPhysicalPos() < Home4+5:
        print('Homing Error: servo 4:', servo4.getPhysicalPos())
        servo4.moveTimeWrite(Home4)
    if servo4.tempRead() > servo4.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo4.vInRead() > max(servo4.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo4.LEDErrorWrite(temp,volt,lock)


    if not Home5-5 < servo5.getPhysicalPos() < Home5+5:
        print('Homing Error: servo 5:', servo5.getPhysicalPos())
        servo5.moveTimeWrite(Home5)
    if servo5.tempRead() > servo5.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo5.vInRead() > max(servo5.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo5.LEDErrorWrite(temp,volt,lock)


    if not Home6-5 < servo6.getPhysicalPos() < Home6+5:
        print('Homing Error: servo 6:', servo6.getPhysicalPos())
        servo6.moveTimeWrite(Home6)
    if servo6.tempRead() > servo6.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo6.vInRead() > max(servo6.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo6.LEDErrorWrite(temp,volt,lock)


    if not Home7-5 < servo7.getPhysicalPos() < Home7+5:
        print('Homing Error: servo 7:', servo7.getPhysicalPos())
        servo7.moveTimeWrite(Home7)
    if servo7.tempRead() > servo7.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo7.vInRead() > max(servo7.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo7.LEDErrorWrite(temp,volt,lock)


    if not Home8-5 < servo8.getPhysicalPos() < Home8+5:
        print('Homing Error: servo 8:', servo8.getPhysicalPos())
        servo8.moveTimeWrite(Home8)
    if servo8.tempRead() > servo8.tempMaxLimitRead():
        temp = 1
    else:
        temp = 0
    if servo8.vInRead() > max(servo8.vInLimitRead()):
        volt = 1
    else:
        volt = 0
    servo8.LEDErrorWrite(temp,volt,lock)
