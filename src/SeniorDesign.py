'''
Created on Feb 25, 2013

@author: Basil
'''
from javax.swing import JButton,SpringLayout,BorderFactory,JComponent,JComboBox,BoxLayout,Box,JFrame, JLabel,JPanel, JMenuBar, JMenu,JTextField
import javax.swing
from java.awt import Color,GridBagConstraints,GridBagLayout,GridLayout, Dimension,BorderLayout
import java.awt.event

from   java.util    import Calendar
from   threading    import  Timer
from   threading    import  Thread

import time,sched
from pychart import *
from org.jfree import *
from org.jfree.data.xy import  *
from org.jfree.chart import *
from org.jfree.chart.plot import *





#from Timer import Timer

class SeniorDesign(JFrame):
        startTime =0
        endTime =0
        global timeTextField
        global end
        
        def __init__(self):
            self.timeTextField = JTextField("00:00")
            self.end = True
            pass
        
        def drawChart(self):
            data = [(10, 20, 30), (20, 65, 33),
                    (30, 55, 30), (40, 45, 51),
                    (50, 25, 27), (60, 75, 30)]

            ar = area.T(size = (150,120),
            y_grid_interval=10,
            x_axis=axis.X(label="X label", label_offset=(0,-7)),
            y_axis=axis.Y(label="Y label"),
            legend = legend.T(), y_range = (0, None))

            ar.add_plot(bar_plot.T(label="foo", data=data),
            line_plot.T(label="bar", data=data, ycol=2))
            ar.draw()
        def createChart(self):
            ds = XYDataset()
            data = { {0.1, 0.2, 0.3}, {1, 2, 3} }
            ds.addSeries("series1", data)
            chart = ChartFactory.createXYLineChart("DemoChart", "x", "y", PlotOrientation.VERTICAL, ds, True, True, False)
            chartPanel= ChartPanel()
            return chartPanel

        def createMenuBar(self):
            #JMenuBar menuBar;
            #JMenu soccerHub, subscriptions,skin,suggestions,help;
        
            menuBar = JMenuBar();
        
            #SoccerHub menu
            seniorDesign = JMenu("SeniorDesign");
            #seniorDesign.setMnemonic(KeyEvent.VK_0);
            menuBar.add(seniorDesign);
        
            #subscription menu
            statistics = JMenu("Statistics");
            #subscriptions.setMnemonic(KeyEvent.VK_1);
            menuBar.add(statistics);
        
            return menuBar;
        
        def mytimer(self,timeTextField):
            timer = Timer()
            while(True):
                timeTextField.setText(timer.getTime())
                
        def getTimeElapsed(self,elapsed):
            global startTime
            millis = int(round(time.time()*1000))
            #elapsedTime = millis - startTime;
            elapsedTime = elapsed
            #elapsedTime = elapsedTime / 1000;

            seconds = str((int)((elapsedTime/1000) % 60));
            minutes = str((int)((elapsedTime/(1000*60)) % 60));
            hours = str((int)((elapsedTime/(1000*60*60)) % 24));

            if (len(seconds) < 2):
                seconds = "0" + seconds;

            if (len(minutes) < 2):
                minutes = "0" + minutes;

            if (len(hours) < 2):
                hours = "0" + hours;

            return hours+":"+minutes+":"+seconds;
            
        def startTimer(self,event):
            global startTime
            #startTime = time.time()
            startTime = int(Calendar.getInstance().getTimeInMillis())
            self.updateTextField("Running")
            timer = Timer()
            

            

        def stopTimer(self,event):
            global endTime
            endTime = int(Calendar.getInstance().getTimeInMillis())
            self.updateTextField(self.getTimeElapsed(endTime-startTime))
            
        def timerListener(self,textfield):
            time = self.getTimeElapsed()
            textfield.setText(time)
            
        def printTime(self):
            print "Current time"+ self.getTimeElapsed(time.time()*1000)
        
        def updateTextField(self,text):
            self.timeTextField.setText(str(text))
            self.repaint()
            
        def updateText(self,textField,startTime):
            count=1
            while(count < 10000):
                #print "start Time" + str(self.getTimeElapsed(startTime))
                print "start Time: " + str(int(startTime))
                #print "end Time" + str(time.time()-startTime)
                elapsed = Calendar.getInstance().getTimeInMillis() - startTime
                #print "elapsed Time" + self.getTimeElapsed(elapsed)
                timer =Timer(1000,self.printTime,())
                timer.start()
                textField.setText( 'Elapsed: %.2f seconds' % ( float( elapsed ) / 1000.0 ) );
                count =count+1
            #textField.setText(self.getTimeElapsed(elapsed))
        

            
        def addComponentsToPane(self):
            
            global stopWatch
           # global textF
            pane = JPanel()  
            layout = GridLayout(0,2)
            pane.setLayout(layout)
            
            
            distanceLabel = JLabel("Distance")
            pane.add(distanceLabel)
            
            distanceTextField = JTextField("Distance")
            pane.add(distanceTextField)
            
            timeLabel = JLabel("Time")
            pane.add(timeLabel)
            
            elapsed = Calendar.getInstance().getTimeInMillis()
            
            #timeTextField = JTextField("00:00")
            
            pane.add(self.timeTextField)
            
            colorLabel = JLabel("color")
            pane.add(colorLabel)
            
            colors = ["Black", "Blue", "Red"]
            colorCombo = JComboBox(colors)
            pane.add(colorCombo)
            startButton = JButton("Start", actionPerformed =self.startTimer)
            stopButton = JButton("Stop", actionPerformed = self.stopTimer)
            leftpanel = self.createChart()
        

            pane.add(startButton)
            pane.add(stopButton)
            self.add(pane)
            self.add(leftpanel,BorderLayout.EAST)

            

    
        def createAndShowGUI(self):
            frame= SeniorDesign()
            frame.setJMenuBar(self.createMenuBar())
            frame.addComponentsToPane()
            frame.pack()
            frame.setSize(500,500)
            frame.setVisible(True);
            
        def main(self):
            self.createAndShowGUI()
            

    
            
if __name__ == '__main__':
    SeniorDesign().main()