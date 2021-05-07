from tkinter import *

gui = Tk()
gui.geometry("450x300")
gui.title("Temperature Conversion Tool")


myLabel_1 = Label(gui, text="Enter temperature: ")
myLabel_2 = Label(gui, text="       ")
myLabel_1.grid(row=0,column=0)
myLabel_2.grid(row=1,column=0)

e=Entry(gui, width=10)
e.grid(row=0,column=1)


def convert():
	base=clicked.get()
	if base =="Fahrenheit":
		f=Entry(frame1, width=10)
		f.grid(row=0,column=1)
		f.insert(0,e.get())
		c=Entry(frame1, width=10)
		c.grid(row=1,column=1)
		tempf= float(e.get())
		value = round((tempf-32)/1.8,4) #convert F to C
		c.insert(0,value)
		k=Entry(frame1, width=10)
		k.grid(row=2,column=1)
		value = value +273.15 #convert F to K
		k.insert(0,value)
	elif base =="Celcius":
		f=Entry(frame1, width=10)
		f.grid(row=0,column=1)
		tempc= float(e.get())
		value = round((tempc*1.8)+32,4) #convert C to F
		f.insert(0,value)
		c=Entry(frame1, width=10)
		c.grid(row=1,column=1)
		c.insert(0,e.get())
		k=Entry(frame1, width=10)
		k.grid(row=2,column=1)
		value = tempc +273.15 #convert C to K
		k.insert(0,value)		
	elif base =="Kelvin":
		f=Entry(frame1, width=10)
		f.grid(row=0,column=1)
		tempk= float(e.get())
		value = round((tempk*1.8)-459.67,4) #convert K to F
		f.insert(0,value)
		c=Entry(frame1, width=10)
		c.grid(row=1,column=1)
		value = tempk-273.15 #convert K to C
		c.insert(0,value)
		k=Entry(frame1, width=10)
		k.grid(row=2,column=1)
		k.insert(0,e.get())	

clicked = StringVar()
clicked.set("Temp")

dropMenu= OptionMenu(gui, clicked, "Fahrenheit","Celcius","Kelvin")
dropMenu.grid(row=0,column=2)
# Button
myButton = Button(gui, text="Convert", command=convert)
myButton.grid(row=0,column=3)

frame1 = LabelFrame(gui,text="Conversion results", padx=30, pady=50)
frame1.grid(row=2,column=0)

myLabel_3 = Label(frame1, text="Fahrenheit: ")
myLabel_4 = Label(frame1, text="Celcius: ")
myLabel_5 = Label(frame1, text="Kelvin: ")
f=Entry(frame1, width=10,state='disabled')
c=Entry(frame1, width=10,state='disabled')
k=Entry(frame1, width=10,state='disabled')
myLabel_3.grid(row=0,column=0) #puts widget above into the window
f.grid(row=0,column=1)
myLabel_4.grid(row=1,column=0)
c.grid(row=1,column=1)
myLabel_5.grid(row=2,column=0) 
k.grid(row=2,column=1)

gui.mainloop()