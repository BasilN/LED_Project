'''
Created on Feb 26, 2013

@author: Basil
'''
from threading import Thread
from datetime import datetime
import time
import thread

class Timer:
    currentTime =0
    startTime= datetime.now
    
    
    def __init__(self):
        global startTime
        startTime = int(round(time.time() * 1000))
    
    #starting new Thread which will update time



    def getTimeElapsed(self):
        global startTime
        millis = int(round(time.time()*1000))
        elapsedTime = millis - startTime;
        elapsedTime = elapsedTime / 1000;

        seconds = str((int)(elapsedTime % 60));
        minutes = str((int)((elapsedTime % 3600) / 60));
        hours = str((int)(elapsedTime / 3600));

        if (seconds.length() < 2):
            seconds = "0" + seconds;

        if (minutes.length() < 2):
            minutes = "0" + minutes;

        if (hours.length() < 2):
            hours = "0" + hours;

        return hours+":"+minutes+":"+seconds;
    
    def updateTime(self):
        global currentTime
        while(True):
            #getting Time in desire format
            currentTime = self.getTimeElapsed();
            #Thread sleeping for 1 sec
            time.sleep(1000);
            
    def runThread(self,number):
        self.updateTime()
        
    def getTime(self):
        global currentTime
        return str(self.currentTime)
        
    def main(self):
        t = Thread(target= self.runThread,args =1)
        t.start()
        thread.start_new_thread(self.runThread(), 1)
        
if __name__ == '__main__':
    Timer().main()
    
            
