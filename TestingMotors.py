from lx16a import *
from math import sin, cos
"""
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize('/dev/ttyUSB0')
"""

def Walking(front1, back1, front2, back2):
    print('walking')
    t=0
    while t < 10:
        # Two sine waves out of phase
        front1.moveTimeWrite(100+sin(t)*10)
        back1.moveTimeWrite(130+cos(t)*20)
        front2.moveTimeWrite(110+sin(t)*10)
        back2.moveTimeWrite(130+cos(t)*20)
        t += 0.01
        
        
def headSwinging(head, Home):
    t = 0
    while t < 100:
        head.moveTimeWrite(Home+ sin(t)*40)
        #print(head.getVirtualPos())
        t +=0.003
