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
            
            
    def UpperBody(head, HomeHead, neck, HomeNeck, lwing, Homelwing, rwing, Homerwing):
        t = 0
        while t < 50:
            head.moveTimeWrite(HomeHead+sin(t)*50)
            neck.moveTimeWrite(HomeNeck+sin(t)*20)
            lwing.moveTimeWrite(Homelwing+sin(t)*40)
            rwing.moveTimeWrite(Homerwing+sin(t)*20)
            t += 0.05
            
    def Walking(lfront, lfHome, lback, lbHome, rfront, rfHome, rback, rbHome):
        t = 0
        # rotate back motors backwards
        #lback.moveTimeWrite(lbHome+5,time=1000)
        #rback.moveTimeWrite(rbHome-5,time=1000)
        #lfront.moveTimeWrite(lfHome+10,time=1000)
        #rfront.moveTimeWrite(rfHome-2,time=1000)
        time.sleep(1)
        while t < 30:
            #lfront.moveTimeWrite(lfHome-sin(t)*2)
            rfront.moveTimeWrite(rfHome-sin(t)*2)
            #lback.moveTimeWrite(lbHome+5+sin(t)*5)
            #rback.moveTimeWrite(rbHome-5+sin(t)*5)
            t += 0.004