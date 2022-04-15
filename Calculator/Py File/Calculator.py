from tkinter import *
from tkinter import messagebox

def click(*args):
            ekran.insert(15, args) 

def clear():
        ekran.delete(0,END)
        
def total():
        top = eval(var.get())
        ekran.delete(0, END)
        ekran.insert(0, str(round(top,4)))

master = Tk()
master.title("Calculator")
master.resizable(False, False)
master.configure(background='lemon chiffon')

canvas = Canvas(master, bg='lemon chiffon', height = 500, width = 500)
canvas.pack()


ust = Frame(master, bg = 'lemon chiffon')
ust.place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.12)

alt_1 = Frame(master, bg="lemon chiffon")
alt_1.place(relx=0.01, rely=0.14, relwidth=0.788, relheight=0.20)

alt_2 = Frame(master, bg="lemon chiffon")
alt_2.place(relx=0.01, rely=0.35, relwidth=0.788, relheight=0.20)

alt_3 = Frame(master, bg="lemon chiffon")
alt_3.place(relx=0.01, rely=0.56, relwidth=0.788, relheight=0.20)

alt_4 = Frame(master, bg="lemon chiffon")
alt_4.place(relx=0.01, rely=0.77, relwidth=0.788, relheight=0.20)

yan = Frame(master, bg="lemon chiffon")
yan.place(relx=0.8, rely=0.14, relwidth=0.19, relheight=0.83)


var = StringVar()
var.set("0")

ekran = Entry(ust, textvariable=var, width=100, font='Vedana 35', bg='khaki',bd=10, justify= RIGHT)
ekran.pack(padx=0.1, pady=0.1)


buton_1 = Button(alt_1, text='1', font="Candara 20 bold", padx=28, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click(1))      
buton_1.pack(side=LEFT)

buton_2 = Button(alt_1, text='2', font="Candara 20 bold", padx=28, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click(2))
buton_2.pack(side=LEFT)

buton_3 = Button(alt_1, text='3', font="Candara 20 bold", padx=28, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click(3))
buton_3.pack(side=LEFT)

buton_topla = Button(alt_1, text='+', font="Candara 20 bold", padx=28, pady=16, relief='groove', bd=8, bg='khaki', command= lambda :click('+'))
buton_topla.pack(side=LEFT)

buton_4 = Button(alt_2, text='4', font="Candara 20 bold", padx=25.5, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click(4))
buton_4.pack(side=LEFT)

buton_5 = Button(alt_2, text='5', font="Candara 20 bold", padx=28, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click(5))
buton_5.pack(side=LEFT) 

buton_6 = Button(alt_2, text='6', font="Candara 20 bold", padx=28, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click(6))
buton_6.pack(side=LEFT)

buton_cikart = Button(alt_2, text='-', font="Candara 20 bold", padx=30, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click('-'))
buton_cikart.pack(side=LEFT)

buton_7 = Button(alt_3, text='7', font="Candara 20 bold", padx=26, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click(7))
buton_7.pack(side=LEFT)

buton_8 = Button(alt_3, text='8', font="Candara 20 bold", padx=28, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click(8))
buton_8.pack(side=LEFT)

buton_9 = Button(alt_3, text='9', font="Candara 20 bold", padx=28, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click(9))
buton_9.pack(side=LEFT)

buton_carp = Button(alt_3, text='x', font="Candara 20 bold", padx=26, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click('*'))
buton_carp.pack(side=LEFT)

buton_nokta = Button(alt_4, text='.', font="Candara 20 bold", padx=28, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click('.'))
buton_nokta.pack(side=LEFT)

buton_0 = Button(alt_4, text='0', font="Candara 20 bold", padx=80, pady=37, relief='groove', bd=8, bg='khaki', command= lambda: click(0))
buton_0.pack(side=LEFT)

buton_bol = Button(alt_4, text='/', font="Candara 20 bold", padx=30, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: click('/'))
buton_bol.pack(side=LEFT)

buton_c = Button(yan, text='c', font="Candara 20 bold", padx=28, pady=16, relief='groove', bd=8, bg='khaki', command= lambda: clear())
buton_c.pack()

buton_esittir = Button(yan, text='=', font="Candara 20 bold", padx=37, pady=160, relief='groove', bd=8, bg='khaki', command= lambda: total())
buton_esittir.pack()

master.mainloop()
