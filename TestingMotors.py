from lx16a import *
from math import sin, cos
"""
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize('/dev/ttyUSB0')
"""

def Walking(servo1, servo2, servo3, servo4):
    while t < 5:
        # Two sine waves out of phase
        servo1.moveTimeWrite(100+sin(t)*10)
        servo2.moveTimeWrite(120+cos(t)*20)
        servo3.moveTimeWrite(100+sin(t)*10)
        servo4.moveTimeWrite(120+cos(t)*20)
        t += 0.01
