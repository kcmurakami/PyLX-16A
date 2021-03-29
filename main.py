from lx16a import *
from BootSelfTest import *
from HomingInitialization import *
from HealthCheck import *
from ShutDownProcedure import *
from TestingMotors import Walking
from TestingMotors import headSwinging
from MovingMotors import MovingMotors
import time

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize('/dev/ttyUSB0')

servo1 = LX16A(1) # right wing
servo2 = LX16A(2) # right back leg
servo3 = LX16A(3) # right front leg
servo4 = LX16A(4) # left front leg
servo5 = LX16A(5) # left back leg
servo6 = LX16A(6) # left wing
servo7 = LX16A(7) # neck
servo8 = LX16A(8) # head
t = 0


# Home Positions
Home1 = 20  # right wing
Home2 = 95  # back right - to rotate back, subtract
Home3 = 128  # front right - to rotate back, subtract
Home4 = 122  # front left - to rotate back, add
Home5 = 115  # back left - to rotate back, add
Home6 = 120
Home7 = 100
Home8 = 85


init8 = servo8.getPhysicalPos()
#print(init8)

"""servo8.moveTimeWrite(120)
servo7.moveTimeWrite(70)
servo1.moveTimeWrite(50)
servo6.moveTimeWrite(90)"""

BootSelfTest(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8)
print('Boot Self Test Completed')

HomingInitialization(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8)
print('Homing Initialization Completed')

HealthCheck(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8)
print('Health Check Completed')
# init8 in HealthCheck is commented out

time.sleep(1)

MovingMotors.UpperBody(servo8, Home8, servo7, Home7, servo6, Home6, servo1, Home1)

STOP


MovingMotors.Walking(servo4, Home4, servo5, Home5, servo3, Home3, servo2, Home2)
STOP

HomingInitialization(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8)
print('Homing Initialization Completed')
STOP



ShutDownProcedure(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8)
print('Shut Down Procedure Completed')
