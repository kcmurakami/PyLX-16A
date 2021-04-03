from lx16a import *


def ShutDownProcedure(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8):

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
    #init8 = servo8.getPhysicalPos()
    init8 = 84
    if isinstance(init8, int) == False:
        print('Com Error: servo 8 is of type ', type(init8))

    # Shutdown Positions
    Shutdown1 = 110
    Shutdown2 = 88   # back right - to rotate back, subtract
    Shutdown3 = 128   # front right - to rotate back, subtract
    Shutdown4 = 124   # front left - to rotate back, add
    Shutdown5 = 122   # back left - to rotate back, add
    Shutdown6 = 120
    Shutdown7 = 100
    Shutdown8 = 85

    # Move to Shutdown position
    servo1.moveTimeWrite(Shutdown1, time=1000)
    servo2.moveTimeWrite(Shutdown2, time=1000)
    servo3.moveTimeWrite(Shutdown3, time=1000)
    servo4.moveTimeWrite(Shutdown4, time=1000)
    servo5.moveTimeWrite(Shutdown5, time=1000)
    servo6.moveTimeWrite(Shutdown6, time=1000)
    servo7.moveTimeWrite(Shutdown7, time=1000)
    servo8.moveTimeWrite(Shutdown8, time=1000)


    #Check for temperature and voltage errors

    lock = 0 # add LOCK if statement

    if not Shutdown1-5 < servo1.getPhysicalPos() < Shutdown1+5:
        print('Shutdown Error: servo 1:', servo1.getPhysicalPos())
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

    if not Shutdown2-5 < servo2.getPhysicalPos() < Shutdown2+5:
        print('Shutdown Error: servo 2:', servo2.getPhysicalPos())
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

    if not Shutdown3-5 < servo3.getPhysicalPos() < Shutdown3+5:
        print('Shutdown Error: servo 3:', servo3.getPhysicalPos())
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

    if not Shutdown4-5 < servo4.getPhysicalPos() < Shutdown4+5:
        print('Shutdown Error: servo 4:', servo4.getPhysicalPos())
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

    if not Shutdown5-5 < servo5.getPhysicalPos() < Shutdown5+5:
        print('Shutdown Error: servo 5:', servo5.getPhysicalPos())
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

    if not Shutdown6-5 < servo6.getPhysicalPos() < Shutdown6+5:
        print('Shutdown Error: servo 6:', servo6.getPhysicalPos())
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

    if not Shutdown7-5 < servo7.getPhysicalPos() < Shutdown7+5:
        print('Shutdown Error: servo 7:', servo7.getPhysicalPos())
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

    if not Shutdown8-5 < servo8.getPhysicalPos() < Shutdown8+5:
        print('Shutdown Error: servo 8:', servo8.getPhysicalPos())
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
