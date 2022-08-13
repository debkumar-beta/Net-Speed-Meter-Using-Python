from tkinter import *
import tkinter
from turtle import bgpic
import speedtest
from PIL import ImageTk,Image


def speedcheak():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),2))+ " Mbps"
    up = str(round(sp.upload()/(10**6),2))+ " Mbps" 
    lab_down.config(text=down)
    lab_up.config(text=up)






sp=Tk()
sp.title("Internet Speed Meter by Deb Kumar Das")
sp.geometry("500x500")
sp.config(bg="BLUE")
bgimg= tkinter.PhotoImage(file = "")
limg= Label(sp, i=bgimg)
limg.pack()

lab=Label(sp,text="Internet Speed Test",font=("Time New Roman",20,"bold"),bg="BLUE",fg="Yellow")
lab.place(x=105,y=40)


lab=Label(sp,text="Download Speed",font=("Time New Roman",20,"bold"),bg="BLUE",fg="WHITE")
lab.place(x=125,y=150)
lab_down=Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="BLUE",fg="RED")
lab_down.place(x=180,y=200)

lab=Label(sp,text="Upload Speed",font=("Time New Roman",20,"bold"),bg="BLUE",fg="WHITE")
lab.place(x=140,y=280)
lab_up=Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="BLUE",fg="RED")
lab_up.place(x=180,y=330)

button=Button(sp,text="CHEAK SPEED",font=("Time New Roman",20,"bold"),relief=RAISED,bg="GREEN",command=speedcheak)
button.place(x=140,y=400)

lab_name=Label(sp,text="by Deb Kumar Das",bg="blue",fg="Green")
lab_name.place(x=400,y=480)






sp.mainloop()