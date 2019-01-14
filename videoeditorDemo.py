import cv2
import tkinter as tk
from tkinter import *
# import ttk
#
from tkinter import ttk
#
# from ttk import Frame
from PIL import Image, ImageTk
from moviepy.editor import *
from tqdm import tqdm
import threading
import time
import datetime

#####Added to solve %1
from moviepy.config import change_settings

now = time.strftime("%Y%m%d-%H%M%S")
print (now)

tqdm(disable=True, total=0)  # initialise internal lock

#####Added to solve %1
change_settings({"FFMPEG_BINARY":"ffmpeg.exe"})

importedvideo = VideoFileClip('test.mp4')  #Video Imported to System

white 		= "#ffffff"
lightBlue2 	= "#adc5ed"
font 		= "Constantia"
fontButtons = (font, 12)
maxWidth  	= 800
maxHeight 	= 550
playpause = True


def show_frame():
	if playpause == True:

		ret, frame = cap.read()
		cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		img   = Image.fromarray(cv2image).resize((760, 400))
		imgtk = ImageTk.PhotoImage(image = img)
		lmain.imgtk = imgtk
		lmain.configure(image=imgtk)
		lmain.after(10, show_frame)
		
	else:
		print('Pause')

tqdm(disable=True, total=0)            
def good():
    gd=0    
    print("Position : %d" % cap.get(cv2.CAP_PROP_POS_MSEC))
    gd = cap.get(cv2.CAP_PROP_POS_MSEC)/1000
    print(gd)
    if gd>=5 :
      exportedvideo = importedvideo.subclip(gd-5,gd+5)  #Clip the Video
    elif  gd<5 :
      exportedvideo = importedvideo.subclip(0,gd+5)  #Clip the Video
    
    exportedvideo.write_videofile("good1/editted_test_good_"+now+"_.mp4",fps=25) # Final Result on the video
tqdm(disable=True, total=0) 
def bad():
   bd=0     
   print("Position : %d" % cap.get(cv2.CAP_PROP_POS_MSEC))
   bd = cap.get(cv2.CAP_PROP_POS_MSEC)/1000
   print(bd)
   if bd>=5:
     exportedvideo = importedvideo.subclip(bd-5,bd+5)  #Clip the Video
   elif  bd<5 :
     exportedvideo = importedvideo.subclip(0,bd+5)  #Clip the Video
   exportedvideo.write_videofile("bad1/edited_test_bad_"+now+"_.mp4",fps=25) # Final Result on the video 


# playpause = True
def play():
	global playpause
	playpause = True
	show_frame()

def pause():
	global playpause
	playpause = False


#Graphics window
mainWindow = tk.Tk()
mainWindow.configure(bg=lightBlue2)
mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
mainWindow.resizable(0,0)
# mainWindow.overrideredirect(1)

mainFrame = Frame(mainWindow)
mainFrame.place(x=20, y=20)                

#Capture video frames
lmain = tk.Label(mainFrame)
lmain.grid(row=0, column=0)

cap = cv2.VideoCapture('test.mp4')
print("Position : %d" % cap.get(cv2.CAP_PROP_POS_MSEC))
#millis = cap.CV_CAP_PROP_POS_MSEC
#print(millis)           

closeButton = Button(mainWindow, text = "CLOSE", font = fontButtons, bg = white, width = 20, height= 1)
closeButton.configure(command= lambda: mainWindow.destroy())              
closeButton.place(x=270,y=430)
goodButton = Button(mainWindow, text = "GOOD", font = fontButtons, bg = white, width = 20, height= 1, command=good)
badButton = Button(mainWindow, text = "BAD", font = fontButtons, bg = white, width = 20, height= 1, command=bad)
goodButton.place(x=490,y=430)
badButton.place(x=30,y=430)	

## Play pause button
play = Button(mainWindow, text = "PLAY", font = fontButtons, bg = white, width = 20, height= 1, command=play)
pause = Button(mainWindow, text = "PAUSE", font = fontButtons, bg = white, width = 20, height= 1, command=pause)
play.place(x=490,y=500)
pause.place(x=30,y=500)
show_frame()  #Display
mainWindow.mainloop()  #Starts GUI
