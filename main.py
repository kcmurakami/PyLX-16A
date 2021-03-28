from lx16a import *
from BootSelfTest import *
from HomingInitilization import *
from HealthCheck import *
from ShutDownProcedure import *
from TestingMotors import *

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

BootSelfTest.BootSelfTest(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8)
print('Boot Self Test Completed')
HomingInitilization.HomingInitilization(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8)
print('Homing Initilization Completed')

#TestingMotors.Walking(servo1, servo2, servo3, servo4)

HealthCheck.HealthCheck(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8)
print('Health Check Completed')

ShutDownProcedure.ShutDownProcedure(servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8)
print('Shut Down Procedure Completed')
