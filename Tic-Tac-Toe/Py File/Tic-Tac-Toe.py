from time import sleep
from tkinter import *
from tkinter import font
import random                           
from tkinter import messagebox

def x(num):     
    b_list = (button0, button1, button2, button3, button4, button5, button6, button7, button8)
    b_temp = b_list[num]
    var.set('X')
    b_temp["text"] = var.get()
    b_temp["state"] = DISABLED

    ToWin()

    key=0
    for i in b_list:
        if i['state']== DISABLED: key+=1 
        else: pass
        
    if key<8: o(num)
    else: pass


def o(num):
    b_list = (button0, button1, button2, button3, button4, button5, button6, button7, button8)
    b_temp = b_list[num]
    
    while b_temp['state']==DISABLED:

        rand = random.randint(0,8)
        b_temp = b_list[rand]

    var.set('O')
    b_temp["text"] = var.get()
    b_temp["state"] = DISABLED

    ToWin()


def ToWin():
    b_list = (button0, button1, button2, button3, button4, button5, button6, button7, button8)

    if (b_list[0]['text']==b_list[1]['text']==b_list[2]['text']=='X' or
        b_list[3]['text']==b_list[4]['text']==b_list[5]['text']=='X' or 
        b_list[6]['text']==b_list[7]['text']==b_list[8]['text']=='X' or 
        b_list[0]['text']==b_list[3]['text']==b_list[6]['text']=='X' or 
        b_list[1]['text']==b_list[4]['text']==b_list[7]['text']=='X' or 
        b_list[2]['text']==b_list[5]['text']==b_list[8]['text']=='X' or 
        b_list[0]['text']==b_list[4]['text']==b_list[8]['text']=='X' or 
        b_list[2]['text']==b_list[4]['text']==b_list[6]['text']=='X'    ):
            messagebox.showinfo("TO WIN", "Kullanıcı Kazandı :)")
            master.destroy()

    elif(b_list[0]['text']==b_list[1]['text']==b_list[2]['text']=='O' or 
         b_list[3]['text']==b_list[4]['text']==b_list[5]['text']=='O' or
         b_list[6]['text']==b_list[7]['text']==b_list[8]['text']=='O' or 
         b_list[0]['text']==b_list[3]['text']==b_list[6]['text']=='O' or 
         b_list[1]['text']==b_list[4]['text']==b_list[7]['text']=='O' or 
         b_list[2]['text']==b_list[5]['text']==b_list[8]['text']=='O' or
         b_list[0]['text']==b_list[4]['text']==b_list[8]['text']=='O' or 
         b_list[2]['text']==b_list[4]['text']==b_list[6]['text']=='O'   ) :
            messagebox.showinfo("TO WIN", "Bilgisayar Kazandı :(")
            master.destroy()

    elif(b_list[0]['state']==b_list[1]['state']==b_list[2]['state']==
         b_list[3]['state']==b_list[4]['state']==b_list[5]['state']==
         b_list[6]['state']==b_list[7]['state']==b_list[8]['state']==DISABLED):
            messagebox.showinfo("TO WIN", "Oyun Berabere  :|")
            master.destroy()

    else:
        pass


master = Tk()
master.title("X O X")

myfont = font.Font(family='Arial', size=40, weight='bold') 
maincolor = 'peach puff'
#secondcolor = 'papaya whip'
secondcolor = 'bisque'

canvas = Canvas(master, height=400, width=400, bg=maincolor)
canvas.pack()

var = StringVar()
var.set('')

button0 = Button(canvas, text=var.get(), font=myfont, bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(0))
button0.place(relx=0.005, rely=0.005, relheight=0.33, relwidth=0.33) 

button1 = Button(canvas, text=var.get(), font=myfont, bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(1))
button1.place(relx=0.335, rely=0.005, relheight=0.33, relwidth=0.33) 

button2 = Button(canvas, text=var.get(), font=myfont, bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(2))
button2.place(relx=0.665, rely=0.005, relheight=0.33, relwidth=0.33) 

button3 = Button(canvas, text=var.get(), font=myfont, bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(3))
button3.place(relx=0.005, rely=0.335, relheight=0.33, relwidth=0.33) 

button4 = Button(canvas, text=var.get(), font=myfont, bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(4))
button4.place(relx=0.335, rely=0.335, relheight=0.33, relwidth=0.33) 

button5 = Button(canvas, text=var.get(), font=myfont, bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(5))
button5.place(relx=0.665, rely=0.335, relheight=0.33, relwidth=0.33) 

button6 = Button(canvas, text=var.get(), font=myfont, bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(6))
button6.place(relx=0.005, rely=0.665, relheight=0.33, relwidth=0.33) 

button7 = Button(canvas, text=var.get(), font=myfont, bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(7))
button7.place(relx=0.335, rely=0.665, relheight=0.33, relwidth=0.33) 

button8 = Button(canvas, text=var.get(), font=myfont, bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(8))
button8.place(relx=0.665, rely=0.665, relheight=0.33, relwidth=0.33) 

master.mainloop()