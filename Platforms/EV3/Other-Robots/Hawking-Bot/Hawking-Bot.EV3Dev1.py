#!/usr/bin/env python3


"""
from https://github.com/EyeTreasure/HawkingBot/blob/master/HawkingBot.py
"""


from ev3dev.auto import *
import time
import random

# HawkingBot and this program are the intellectual property of Berend RAH at EyeTreasure
# the program can be freely distributed and modified but you must clearly provide a link to EyeTreasure, the Github repository and the assembly instructions
# if you plan on any commercial exploitation of this idea then you must contact Berend RAH at EyeTreasure
# you are free to present the HawkingBot on your Youtube channel (or a Blog or a Vlog) and the above does not apply to Youtube channel monetisation

# the Lego assembly instructions can be found here:https: github.com/EyeTreasure/HawkingBot/blob/master/Hawking%20Bot%20Assembly%20Guide.pdf

# the Youtube demo video is here: https://youtu.be/nnCas87dHp8

# the Instructables instructions are here: https://www.instructables.com/id/Hawking-Bot

# you may contact the author at HBot@EyeTreasure.com with the subject 'HBot Project' e.g. to let me know of your project or a fork or ask for permission


class HawkingBot():
    def __init__(self):

        self.medMot=MediumMotor('outD') # Medium motor (the head) connected to port D
        self.mot1=LargeMotor('outA')    # Large motor left side connected to port A
        self.mot2=LargeMotor('outB')    # Large motor right side connected to port B


        self.ps=PowerSupply()
    
        self.r=random
        self.lcd=Screen()
        self.switch="R" 

        try:
            self.USS=UltrasonicSensor() 
        except:        #this will throw an error if not connected
            pass

        # this is the list of constants used    

        self.soundFilesNo=5 #number of all wav files            
        self.minVolt=6.5 #the minimum voltage at which the robot will run
        self.USSdelay_time=0.01 #time the ultrasonic sensor will be inactive to reduce errors
        self.motorDelay=0.1
        self.motorDelay_straight=0.3
        self.UDelay=0.3

    def screenMessage(self, message, duration=5):

        #this gives a simple status message and can be used for errors or other short messages
        #default display time is 5 seconds

        self.lcd.draw.rectangle((0,0,177,40), fill='black')
        self.lcd.draw.text((48,13),'Status Message', fill='white')
        self.lcd.draw.text((36,80), message)
        self.lcd.update()
        time.sleep(duration)

    def checkConnection(self): #method to check all devices are properly connected
        deviceList=[self.medMot,self.mot1,self.mot2,self.USS]
        statusOK=True
        for device in deviceList:
            try:
                assert device.connected
        
            except:

                print(device,' is not connected')
                self.screenMessage('Device Not Connected',1)
                Sound.speak('Please check my connections').wait()
                time.sleep(5)
            
                statusOK=False
        if statusOK:
            Sound.speak('I feel sohhh connected. Yehhhhhh').wait()
            self.screenMessage('All Connected',1)
            time.sleep(5)
            self.USS.mode='US-DIST-CM'  # this sets the units measured by the ultrasonic sensor but distance is actually in mm NOT cm
        return statusOK



    def checkBattery(self): # method to ensure the battery has enough charge
        statusOK=True
        if self.ps.measured_volts<self.minVolt:
            Sound.speak('Low Battery Levels. Please feed me. Please').wait()
            time.sleep(5)
            statusOK=False
        else:
            Sound.speak('I feel energised. Lets get started').wait()
            time.sleep(5)
        return statusOK




    def mDistance(self): #this method lets the ultrasonic sensor determine the distance to the nearest object
                         #be aware the ultrasonic sensor sees only larger objects and sometimes sound reflections can have unpredictable effects
        try:
            time.sleep(self.USSdelay_time)
            return self.USS.value()           # a short delay is required to stop the ultrasonic sensor from malfunctioning
	
        except:   # this is to catch a connection error when it is malfunctioning which would otherwise terminate the programm      
            pass



    def moveAhead(self):

        self.medMot.run_to_abs_pos(position_sp=0, speed_sp=300)
        self.mot1.run_timed(time_sp=2000, speed_sp=-700)
        self.mot2.run_timed(time_sp=2000, speed_sp=-700)
        self.mot2.wait_while('running')
        time.sleep(self.motorDelay_straight)

    def moveRight(self):

        self.mot1.run_timed(time_sp=1000, speed_sp=-500)
        self.mot2.run_timed(time_sp=1000, speed_sp=500)
        self.mot2.wait_while('running')
        self.moveAhead()    
        time.sleep(self.motorDelay)
    

    def moveLeft(self):

        self.mot1.run_timed(time_sp=1000, speed_sp=500)
        self.mot2.run_timed(time_sp=1000, speed_sp=-500)
        self.mot2.wait_while('running')
        self.moveAhead()    
        self.time.sleep(self.motorDelay)


    def findMidMax(self,x):    #this method returns the maximum value and the middle position between two maxima
        max=0
        pos=0
        for i in range(len(x)):   #the length of the array
            if x[i]>max:
                max=x[i]
                pos=i

            if x[i]==max:
                finalPos=i

        return max,pos+(finalPos-pos)/2
 

    def ranTalk(self):
        ranNo=self.r.randint(1,self.soundFilesNo)   #wav files are numbered from 1 onwards
        filename="SH"+str(ranNo)+".wav"
        Sound.play(filename).wait
        time.sleep(3)
 
    def motionDetector(self,switch):

        # this function responds to movements
        # Hawking talks and moves roughly in the direction of the movement
        # the ultrasonic sensor is at times erratic so you may see random moves
        # if you want to improve on this you could write a routine to detect erroneous measurements
        # usually one of the distance measurements is way different from the others when there is 'false' movement detection
        # you are welcome to improve on this method and make it more reliable and robust

 
        disA=[]
        disB=[]
        disC=[]
        self.mDistance()  #initialising ultrasonic sensor
        self.mDistance()  #first readings are erratic
        time.sleep(0.3)
        stop=False

        if switch=="R":
            for i in range(9): 
                self.medMot.run_to_abs_pos(position_sp=-60+i*15, speed_sp=100)
                self.medMot.wait_while('running')
                time.sleep(0.2)        
                disA.append(self.mDistance())
                time.sleep(0.1)
                disB.append(self.mDistance())
                time.sleep(0.1)
                disC.append(abs(disA[i]-disB[i]))
                if disA[i]<500:
                    stop=True             # distances of less than 50cm act as stop signal to avoid bumping into an obstacle
            switch="L"
 
            #print(disA) #uncomment to see measurement
            #print(disB)
 
        else:
            for i in range(8,-1,-1):     #head moving from right to left
                self.medMot.run_to_abs_pos(position_sp=-60+i*15, speed_sp=100)
                self.medMot.wait_while('running')
                time.sleep(0.2)        
                disA.append(self.mDistance())
                time.sleep(0.1)
                disB.append(self.mDistance())
                time.sleep(0.1)
                if disA[8-i]<500:
                    stop=True
            switch="R"
            for i in range(9):
                disC.append(abs(disA[8-i]-disB[8-i]))
                
            #print(disA)
            #print(disB)


        max,midPo=self.findMidMax(disC)
        return switch, stop, disC,max,midPo
         


        
    def rightMax(self,x):   # determines the maximum most to the right

        Rmax=0
        pos=0
        for i in range(len(x)):
            if x[i]>=Rmax:
                Rmax=x[i]
                pos=i

        return Rmax,pos

    def checkTerrain(self,switch):

        dis=[]       

        if switch=="R":             #head moving left to right
            for i in range(9):
                  self.medMot.run_to_abs_pos(position_sp=-60+i*15, speed_sp=100)
                  dis.append(self.mDistance())                
                  time.sleep(0.1)
            maxd=max(dis)
            indexMax=dis.index(max(dis))
            switch="L"
        else:
            for i in range(8,0,-1):     #head moving right to left
                  self.medMot.run_to_abs_pos(position_sp=-60+i*15, speed_sp=100)
                  dis.append(self.mDistance())
                  time.sleep(0.1)
            maxd,indexMax=self.rightMax(dis)
            switch="R"
  
        return switch, maxd, dis[4], indexMax

    # max distance, middle distance and position of max distance // if there is more than on max positon it chooses the leftmost one


    def goStraight(self):

        self.medMot.run_to_abs_pos(position_sp=0, speed_sp=100)
        self.mot1.run_forever(speed_sp=-1000)
        self.mot2.run_forever(speed_sp=-1000)
        goOn=True
        while goOn:
            if self.mDistance()<1000:
                goOn=False
            time.sleep(self.motorDelay_straight)
        self.mot1.stop()
        self.mot2.stop()
         

    def straightAhead(self):

        self.medMot.run_to_abs_pos(position_sp=0, speed_sp=100)
        self.mot1.run_timed(time_sp=2000, speed_sp=-700)
        self.mot2.run_timed(time_sp=2000, speed_sp=-700)
        self.mot2.wait_while('running')
        time.sleep(self.motorDelay_straight)

    def turnRight(self):

        self.mot1.run_timed(time_sp=1000, speed_sp=-700)
        self.mot2.run_timed(time_sp=1000, speed_sp=-500)
        self.mot2.wait_while('running')    
        time.sleep(0.1)
    

    def turnLeft(self):

        self.mot1.run_timed(time_sp=1000, speed_sp=-500)
        self.mot2.run_timed(time_sp=1000, speed_sp=-700)
        self.mot2.wait_while('running')    
        time.sleep(0.1)

    def UTurn(self):     # needs adjusting for terrain
    
        self.mot1.stop()
        self.mot2.stop()        
       #step back a bit
        self.mot1.run_timed(time_sp=1000, speed_sp=500)
        self.mot2.run_timed(time_sp=1000, speed_sp=500)
        self.mot2.wait_while('running')
        time.sleep(self.UDelay)
        self.mot1.stop()
        self.mot2.stop()
        # needs a random left or right turn here
                        
        #turn around - may need adjusting and depends on surface
        self.mot1.run_timed(time_sp=1500, speed_sp=-500)
        self.mot2.run_timed(time_sp=1500, speed_sp=500)
        self.mot2.wait_while('running')
        time.sleep(0.3)

    def findfreeCor(self):
        
        #step back a bit
        self.mot1.run_timed(time_sp=1000, speed_sp=500)
        self.mot2.run_timed(time_sp=1000, speed_sp=500)
        self.mot2.wait_while('running')
        time.sleep(0.3)
        self.mot1.stop()
        self.mot2.stop()

        self.medMot.run_to_abs_pos(position_sp=0, speed_sp=100)
        self.mot1.run_forever(speed_sp=-500)
        self.mot2.run_forever(speed_sp=500)
        goOn=True
        while goOn:
            if self.mDistance()>=1000:
                goOn=False
                time.sleep(0.2)
        self.mot1.stop()
        self.mot2.stop()
        time.sleep(1)
 

    def stopNow(self):
        self.mot1.stop()
        self.mot2.stop()
        time.sleep(1)



#main body of programm

HBot=HawkingBot()
navTime=60
followTime=45
switch="R"

if HBot.checkConnection() and HBot.checkBattery():

    startTime=time.time()
    print('Navigating terrain...')
    while time.time()-startTime<navTime:    #this programm segment lasts navTime seconds
        switch, maxd, midd, indexd=HBot.checkTerrain(switch)
        print ('switch=',switch, ' maxd=',maxd,' midd=',midd, ' indexd=',indexd, '\n')
        if midd>2000:  # just go straight until less than 200 cm
            HBot.goStraight()

        elif midd>400:  # distance ahead over 40 cm 
            if midd>=maxd:   # largest free distance is straight ahead 
                HBot.straightAhead()
            else:
                if indexd<4:
                    print('Going left')
                    HBot.turnLeft()
                else:
                    print('Going right')
                    HBot.turnRight()
        else:
            print('stopping and making U-turn')
            HBot.stopNow()
            HBot.UTurn()           

        HBot.stopNow()
        HBot.medMot.run_to_abs_pos(position_sp=0, speed_sp=100)

    startTime=time.time()
    print('Searching for moving object....')
    HBot.medMot.run_to_abs_pos(position_sp=0, speed_sp=100)
    stop=False
    while time.time()-startTime<followTime and not stop:  #waits followTime seconds for a movement
        if HBot.mDistance()>1000:
            diff=[]
            switch, stop, diff,max,midPo=HBot.motionDetector(switch)
            print(diff)
            print('Maximum= ',max)
    
            if max>40:
  
                if midPo<4:
                    print('Going left')
                    HBot.moveLeft()
                elif midPo==4:
                    print('Straight ahead')
                    HBot.moveAhead()
                else:
                    print('Going right')
                    HBot.moveRight()
                HBot.ranTalk()
                print('Talking')
        else:
            HBot.findfreeCor()           

    HBot.medMot.run_to_abs_pos(position_sp=0, speed_sp=100)
