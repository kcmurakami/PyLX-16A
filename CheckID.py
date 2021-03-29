from lx16a import *
import time
from MovingMotors import MovingMotors


LX16A.initialize('/dev/ttyUSB0')

servo1 = LX16A(1) # right wing
servo2 = LX16A(2) # back right leg
servo3 = LX16A(3) # front right leg
servo4 = LX16A(4) # front left leg
servo5 = LX16A(5) # back left leg
servo6 = LX16A(6) # left wing
servo7 = LX16A(7) # neck
servo8 = LX16A(8) # head


Home1 = 110  # right wing
Home2 = 88  # back right - to rotate back, subtract
Home3 = 128  # front right - to rotate back, subtract
Home4 = 124  # front left - to rotate back, add
Home5 = 122  # back left - to rotate back, add
Home6 = 120
Home7 = 100
Home8 = 85

"""   OLDLEGS
Home1 = 110  # right wing
Home2 = 90  # back right - to rotate back, subtract
Home3 = 130  # front right - to rotate back, subtract
Home4 = 122  # front left - to rotate back, add
Home5 = 120  # back left - to rotate back, add
Home6 = 120
Home7 = 100
Home8 = 85
"""



servo1.moveTimeWrite(Home1, time=1000)
servo2.moveTimeWrite(Home2, time=1000)
servo3.moveTimeWrite(Home3, time=1000)
servo4.moveTimeWrite(Home4, time=1000)
servo5.moveTimeWrite(Home5, time=1000)
servo6.moveTimeWrite(Home6, time=1000)
servo7.moveTimeWrite(Home7, time=1000)
servo8.moveTimeWrite(Home8, time=1000)
time.sleep(3)

# RIGHT FOOT FORWARD
"""
# right front
servo3.moveTimeWrite(Home3+35, time=2000)

# left front
servo4.moveTimeWrite(Home4+25, time=2000)

# right back
servo2.moveTimeWrite(Home2+40, time=2000)

# left back
servo5.moveTimeWrite(Home5+35, time=2000)


"""

# right front
servo3.moveTimeWrite(Home3-30, time=2000)

# left front
servo4.moveTimeWrite(Home4-30, time=2000)

# right back
servo2.moveTimeWrite(Home2-40, time=2000)

# left back
servo5.moveTimeWrite(Home5-35, time=2000)



time.sleep(2)

tupper = 0.01

#MovingMotors.UpperBody(tupper, servo8, Home8, servo7, Home7, servo6, Home6, servo1, Home1)

