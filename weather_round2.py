from tkinter import *
from tkinter import ttk
import requests

def data_get():
    lat_data=lat.get()
    long_data=long.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+lat_data+"&lon="+long_data+"&appid=?????").json()


    wval_label.config(text=data["weather"][0]["main"])
    descval_label.config(text=data["weather"][0]["description"])
    tempval_label.config(text=str(int((data["main"]["temp"]-273.15)))+(chr)(176)+"C")
    hmdtval_label.config(text=str(data["main"]["humidity"]))
    presval_label.config(text=str(data["main"]["pressure"]))
    wspdval_label.config(text=str(int(data["wind"]["speed"]*3.6))+" kmph")
    


win=Tk()
win.title("Surya's Weather App")
win.config(bg="black")
win.geometry("1000x800")
head_label=Label(win,text="WEATHER FORECAST",font=("broadway",40,"bold",'underline'),bg="black",fg="white")
head_label.place(x=100,y=50,height=100,width=800)

lat=StringVar()
long=StringVar()
dialog1=Label(win,text="LATTITUDE : ",font=(10),bg="black",fg="white")
dialog1.place(x=100,y=175)
lat_entry=Entry(win,width=50,bg="white",fg="black",font=(10),textvariable=lat).place(x=240,y=175)
dialog2=Label(win,text="LONGITUDE : ",font=(10),bg="black",fg="white")
dialog2.place(x=100,y=235)
long_entry=Entry(win,width=50,bg="white",fg="black",textvariable=long,font=(10)).place(x=240,y=235)

w_label=Label(win,text="WEATHER : ",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
w_label.place(x=150,y=400,height=50,width=300)

wval_label=Label(win,text="",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
wval_label.place(x=500,y=400,height=50,width=300)

desc_label=Label(win,text="DESCRIPTION : ",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
desc_label.place(x=150,y=465,height=50,width=300)

descval_label=Label(win,text="",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
descval_label.place(x=500,y=465,height=50,width=300)

temp_lable=Label(win,text="TEMPERATURE : ",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
temp_lable.place(x=150,y=530,height=50,width=300)

tempval_label=Label(win,text="",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
tempval_label.place(x=500,y=530,height=50,width=300)

hmdt_label=Label(win,text="HUMIDITY : ",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
hmdt_label.place(x=150,y=595,height=50,width=300)

hmdtval_label=Label(win,text="",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
hmdtval_label.place(x=500,y=595,height=50,width=300)

pres_label=Label(win,text="PRESSURE: ",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
pres_label.place(x=150,y=660,height=50,width=300)

presval_label=Label(win,text="",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
presval_label.place(x=500,y=660,height=50,width=300)

wspd_label=Label(win,text="WIND SPEED : ",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
wspd_label.place(x=150,y=725,height=50,width=300)

wspdval_label=Label(win,text="",font=("Rockwell Condensed",25,"bold"),bg="black",fg="white")
wspdval_label.place(x=500,y=725,height=50,width=300)

doneButton=Button(win,text="SUBMIT",font=("Roman",25,"bold"),command=data_get)
doneButton.place(x=400,y=300,height=50,width=200)

win.mainloop()
