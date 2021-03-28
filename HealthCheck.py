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

def HealthCheck(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8):

    #Query Initial Motor position
    init1 = servo1.getPhysicalPos()
    init2 = servo2.getPhysicalPos()
    init3 = servo3.getPhysicalPos()
    init4 = servo4.getPhysicalPos()
    init5 = servo5.getPhysicalPos()
    init6 = servo6.getPhysicalPos()
    init7 = servo7.getPhysicalPos()
    #init8 = servo8.getPhysicalPos()

    #Check that each motor is receiving sufficient power
    lock = 0
    if max(servo1.vInLimitRead()) > servo1.vInRead() > min(servo1.vInLimitRead()):
        volt = 0
    else:
        volt = 1
        print('Voltage Error: servo 1:', servo1.vInRead())
    if servo1.tempRead() > servo1.tempMaxLimitRead():
        temp = 1
        print('Temperature Error: servo 1')
    else:
        temp = 0
    servo1.LEDErrorWrite(temp,volt,lock)

    if max(servo2.vInLimitRead()) > servo2.vInRead() > min(servo2.vInLimitRead()):
        volt = 0
    else:
        volt = 1
        print('Voltage Error: servo 2:', servo2.vInRead())
    if servo2.tempRead() > servo2.tempMaxLimitRead():
        temp = 1
        print('Temperature Error: servo 2')
    else:
        temp = 0
    servo2.LEDErrorWrite(temp,volt,lock)

    if max(servo3.vInLimitRead()) > servo3.vInRead() > min(servo3.vInLimitRead()):
        volt = 0
    else:
        volt = 1
        print('Voltage Error: servo 3:', servo3.vInRead())
    if servo3.tempRead() > servo3.tempMaxLimitRead():
        temp = 1
        print('Temperature Error: servo 3')
    else:
        temp = 0
    servo3.LEDErrorWrite(temp,volt,lock)

    if max(servo4.vInLimitRead()) > servo4.vInRead() > min(servo4.vInLimitRead()):
        volt = 0
    else:
        volt = 1
        print('Voltage Error: servo 4:', servo4.vInRead())
    if servo4.tempRead() > servo4.tempMaxLimitRead():
        temp = 1
        print('Temperature Error: servo 4')
    else:
        temp = 0
    servo4.LEDErrorWrite(temp,volt,lock)

    if max(servo5.vInLimitRead()) > servo5.vInRead() > min(servo5.vInLimitRead()):
        volt = 0
    else:
        volt = 1
        print('Voltage Error: servo 5:', servo5.vInRead())
    if servo5.tempRead() > servo5.tempMaxLimitRead():
        temp = 1
        print('Temperature Error: servo 5')
    else:
        temp = 0
    servo5.LEDErrorWrite(temp,volt,lock)

    if max(servo6.vInLimitRead()) > servo6.vInRead() > min(servo6.vInLimitRead()):
        volt = 0
    else:
        volt = 1
        print('Voltage Error: servo 6:', servo6.vInRead())
    if servo6.tempRead() > servo6.tempMaxLimitRead():
        temp = 1
        print('Temperature Error: servo 6')
    else:
        temp = 0
    servo6.LEDErrorWrite(temp,volt,lock)

    if max(servo7.vInLimitRead()) > servo7.vInRead() > min(servo7.vInLimitRead()):
        volt = 0
    else:
        volt = 1
        print('Voltage Error: servo 7:', servo7.vInRead())
    if servo7.tempRead() > servo7.tempMaxLimitRead():
        temp = 1
        print('Temperature Error: servo 7')
    else:
        temp = 0
    servo7.LEDErrorWrite(temp,volt,lock)

    if max(servo8.vInLimitRead()) > servo8.vInRead() > min(servo8.vInLimitRead()):
        volt = 0
    else:
        volt = 1
        print('Voltage Error: servo 8:', servo8.vInRead())
    if servo8.tempRead() > servo8.tempMaxLimitRead():
        temp = 1
        print('Temperature Error: servo 8')
    else:
        temp = 0
    servo8.LEDErrorWrite(temp,volt,lock)

    #Checksum / COM errors
    #if servo1.checksum()
