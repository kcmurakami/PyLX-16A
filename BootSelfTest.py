from lx16a import *
import time


def BootSelfTest(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8):

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
    if isinstance(init8, int) == False:
        print('Com Error: servo 8 is of type ', type(init8))

    #Check that each motor is receiving sufficient power
    temp = 0
    lock = 0
    if servo1.vInRead() < min(servo1.vInLimitRead()):
        volt = 1
        print('Voltage Error: servo 1:', servo1.vInRead())
    else:
        volt = 0
    servo1.LEDErrorWrite(temp,volt,lock)
    if servo2.vInRead() < min(servo2.vInLimitRead()):
        volt = 1
        print('Voltage Error: servo 2:', servo2.vInRead())
    else:
        volt = 0
    servo2.LEDErrorWrite(temp,volt,lock)
    if servo3.vInRead() < min(servo3.vInLimitRead()):
        volt = 1
        print('Voltage Error: servo 3:', servo3.vInRead())
    else:
        volt = 0
    servo3.LEDErrorWrite(temp,volt,lock)
    if servo4.vInRead() < min(servo4.vInLimitRead()):
        volt = 1
        print('Voltage Error: servo 4:', servo4.vInRead())
    else:
        volt = 0
    servo4.LEDErrorWrite(temp,volt,lock)
    if servo5.vInRead() < min(servo5.vInLimitRead()):
        volt = 1
        print('Voltage Error: servo 5:', servo5.vInRead())
    else:
        volt = 0
    servo5.LEDErrorWrite(temp,volt,lock)
    if servo6.vInRead() < min(servo6.vInLimitRead()):
        volt = 1
        print('Voltage Error: servo 6:', servo6.vInRead())
    else:
        volt = 0
    servo6.LEDErrorWrite(temp,volt,lock)
    if servo7.vInRead() < min(servo7.vInLimitRead()):
        volt = 1
        print('Voltage Error: servo 7:', servo7.vInRead())
    else:
        volt = 0
    servo7.LEDErrorWrite(temp,volt,lock)
    if servo8.vInRead() < min(servo8.vInLimitRead()):
        volt = 1
        print('Voltage Error: servo 8:', servo8.vInRead())
    else:
        volt = 0
    servo8.LEDErrorWrite(temp,volt,lock)

    #Flash each motor LED 3 times
    for i in range(1,9):
        for k in range(3):
            LX16A(i).LEDCtrlWrite(1)
            time.sleep(.1)
            LX16A(i).LEDCtrlWrite(0)
            time.sleep(.1)
        print('servo{} LED Flashing'.format(i))
