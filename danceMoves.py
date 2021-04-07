from lx16a import *
from math import sin, cos
import time

class DanceMoves:

    def __init__(self):
        pass

    def FullDance(dt, head, HomeHead, neck, HomeNeck, lwing, Homelwing, rwing, Homerwing):
        """
        Flaps wings in opposite directions.
        Bobs neck up and down.
        Swings head back and forth.
        """
        t = 0
        while t < 50:
            head.moveTimeWrite(HomeHead+sin(t)*50)
            neck.moveTimeWrite(HomeNeck+sin(t)*10)
            lwing.moveTimeWrite(Homelwing+sin(t)*40)
            rwing.moveTimeWrite(Homerwing+sin(t)*40)
            t += dt

    def FlapWings(dt, neck, HomeNeck, lwing, Homelwing, rwing, Homerwing):
        """
        Flaps wings in same direction.
        Bobs neck up and down along with the wings.
        """
        t = 0
        while t < 50:
            neck.moveTimeWrite(HomeNeck+sin(t)*10)
            lwing.moveTimeWrite(Homelwing-sin(t)*40)
            rwing.moveTimeWrite(Homerwing+sin(t)*40)
            t += dt

    def PoseLeft(dt, head, HomeHead, lwing, Homelwing, lfront, lfHome, lback, lbHome, rfront, rfHome, rback, rbHome):
        """
        Look to the left.
        Lift left wing.
        Move right foot forward.
        """
        t = 0
        lfront.moveTimeWrite(lfHome+25, time=2000)
        rfront.moveTimeWrite(rfHome+40, time=2000)
        lback.moveTimeWrite(lbHome+35, time=2000)
        rback.moveTimeWrite(rbHome+40, time=2000)
        time.sleep(2)
        head.moveTimeWrite(HomeHead+sin(dt)*50)
        lwing.moveTimeWrite(Homelwing+sin(dt)*40)
        time.sleep(0.5)

    def PoseRight(dt, head, HomeHead, rwing, Homerwing, lfront, lfHome, lback, lbHome, rfront, rfHome, rback, rbHome):
        """
        Look to the right.
        Lift right wing.
        Move left foot forward.
        """
        t = 0
        lfront.moveTimeWrite(lfHome-30, time=2000)
        rfront.moveTimeWrite(rfHome-30, time=2000)
        lback.moveTimeWrite(lbHome-35, time=2000)
        rback.moveTimeWrite(rbHome-40, time=2000)
        time.sleep(2)
        head.moveTimeWrite(HomeHead+sin(dt)*50)
        rwing.moveTimeWrite(Homerwing+sin(dt)*40)
        time.sleep(0.5)

    def Bobbing(dt, neck, HomeNeck):
        """
        Move neck up and down.
        """
        t = 0
        while t < 50:
            neck.moveTimeWrite(HomeNeck+sin(t)*10)
            t += dt

    def HomePositions(head, HomeHead, neck, HomeNeck, lwing, Homelwing, rwing, Homerwing, lfront, lfHome, lback, lbHome, rfront, rfHome, rback, rbHome):
        """
        Move all motors to home positions.
        """
        head.moveTimeWrite(HomeHead, time=1000)
        neck.moveTimeWrite(HomeNeck, time=1000)
        lwing.moveTimeWrite(Homelwing, time=1000)
        rwing.moveTimeWrite(Homerwing, time=1000)
        lfront.moveTimeWrite(lfHome, time=2000)
        lback.moveTimeWrite(lbHome, time=2000)
        rfront.moveTimeWrite(rfHome, time=2000)
        rback.moveTimeWrite(rbHome, time=2000)
        time.sleep(2)
