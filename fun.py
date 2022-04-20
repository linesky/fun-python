import RPi.GPIO as GPIO
import thread;
from Tkinter import *
import tkMessageBox;

root=Tk()
root.title("fun")
root.geometry("500x300")

def checkers():
	GPIO.output(4,GPIO.HIGH)
	print "on"
	return
def checkers2():
	GPIO.output(4,GPIO.LOW)
	print "off"
	return
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
cmd=Button(root,text="fun on",command=checkers)
cmd2=Button(root,text="fun off",command=checkers2)
cmd.pack()
cmd2.pack()   
root.mainloop()            
