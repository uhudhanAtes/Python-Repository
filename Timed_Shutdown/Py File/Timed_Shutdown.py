from tkinter import *
from tkinter import messagebox
import os

def click(): 
    if 0 < var.get() <= 480:
        os.system("shutdown /s /t {}".format(var.get()*60))
        master.quit()
        
    else:
        mesaj="Something went wrong!"
        messagebox.showwarning("Warring",mesaj)


master = Tk()
master.title("Timed Shutdown")
master.resizable(False, False)

mainColor = 'khaki1'
secondColor = 'PaleGreen2'    
buttoncolor = 'old lace'
        
canvas = Canvas(master ,height=210 ,width=460)  
canvas.pack() 

top = Frame(master, bg=mainColor)
top.place(relx=0, rely=0, relwidth=1, relheight=0.8)

down = Frame(master, bg=secondColor)
down.place(relx=0, rely=0.8, relwidth=1, relheight=1)

toplabel = Label(top, text="Timed Shutdown", bg=secondColor, font="Arial 18 bold", anchor='center')
toplabel.place(relx=0, rely=0, relwidth=1, relheight=0.25)

var = IntVar()

time = Spinbox(top, from_=0, to=480, bd=5, bg=buttoncolor, textvariable=var, font='Arial 16', width=16, relief='flat')
time.place(relx=0.27, rely=0.35)

button = Button(top, text='Submit',bd=3, bg=buttoncolor, command=click, font='Arial 12', relief='raised')
button.place(relx=0.40, rely=0.62, relheight=0.25, relwidth= 0.2)
    
label = Label(down,
             text="Time in minutes, time range 1 minute - 480 minutes (8 hours)",
             bg=secondColor,
             font="Arial 12 ",
             anchor='w'
)
label.place(relx=0, rely=0, relheight=0.2, relwidth=1)  

master.mainloop()