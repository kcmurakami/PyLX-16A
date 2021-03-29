from lx16a import *
from math import sin, cos
import time

class MovingMotors:
    
    def HeadSwinging(head, Home):
        t = 0
        while t < 10:
            head.moveTimeWrite(Home+ sin(t)*40)
            t += 0.003
            
    
    def NeckBobbing(neck, Home):
        t = 0
        while t < 10:
            neck.moveTimeWrite(Home+sin(t)*10)
            t += 0.003
            
    def HeadAndNeck(head, HomeHead, neck, HomeNeck):
        t = 0
        while t < 50:
            head.moveTimeWrite(HomeHead+sin(t)*40)
            neck.moveTimeWrite(HomeNeck+sin(t)*10)
            t += 0.003
            
            
    def UpperBody(tupper, head, HomeHead, neck, HomeNeck, lwing, Homelwing, rwing, Homerwing):
        t = 0
        while t < 50:
            head.moveTimeWrite(HomeHead+sin(t)*50)
            neck.moveTimeWrite(HomeNeck+sin(t)*10)
            lwing.moveTimeWrite(Homelwing+sin(t)*40)
            rwing.moveTimeWrite(Homerwing+sin(t)*40)
            t += tupper
            
    def RightForward(lfront, lfHome, lback, lbHome, rfront, rfHome, rback, rbHome):
        t=0
        lfront.moveTimeWrite(lfHome+25, time=2000)
        rfront.moveTimeWrite(rfHome+40, time=2000)
        lback.moveTimeWrite(lbHome+35, time=2000)
        rback.moveTimeWrite(rbHome+40, time=2000)
        time.sleep(2)

    def LeftForward(lfront, lfHome, lback, lbHome, rfront, rfHome, rback, rbHome):
        lfront.moveTimeWrite(lfHome-30, time=2000)
        rfront.moveTimeWrite(rfHome-30, time=2000)
        lback.moveTimeWrite(lbHome-35, time=2000)
        rback.moveTimeWrite(rbHome-40, time=2000)
        time.sleep(2)

            
    def Walking(lfront, lfHome, lback, lbHome, rfront, rfHome, rback, rbHome):
        t = 0
        # rotate back motors backwards
        #lback.moveTimeWrite(lbHome+5,time=1000)
        #rback.moveTimeWrite(rbHome-5,time=1000)
        #lfront.moveTimeWrite(lfHome+10,time=1000)
        #rfront.moveTimeWrite(rfHome-2,time=1000)
        #time.sleep(.1)
        while t < 30:
            lfront.moveTimeWrite(lfHome+25, time=2000)
            rfront.moveTimeWrite(rfHome+40, time=2000)
            lback.moveTimeWrite(lbHome+35, time=2000)
            rback.moveTimeWrite(rbHome+40, time=2000)
            time.sleep(2)
            lfront.moveTimeWrite(lfHome, time=2000)
            rfront.moveTimeWrite(rfHome, time=2000)
            lback.moveTimeWrite(lbHome, time=2000)
            rback.moveTimeWrite(rbHome, time=2000)
            time.sleep(2)
            lfront.moveTimeWrite(lfHome-30, time=2000)
            rfront.moveTimeWrite(rfHome-30, time=2000)
            lback.moveTimeWrite(lbHome-35, time=2000)
            rback.moveTimeWrite(rbHome-40, time=2000)
            time.sleep(2)
            lfront.moveTimeWrite(lfHome, time=2000)
            rfront.moveTimeWrite(rfHome, time=2000)
            lback.moveTimeWrite(lbHome, time=2000)
            rback.moveTimeWrite(rbHome, time=2000)
            time.sleep(2)
            t += 1