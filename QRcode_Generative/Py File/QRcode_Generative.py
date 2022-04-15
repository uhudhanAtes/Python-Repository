from tkinter import *
import qrcode
import os

def send():
    url = var.get()
    if url.split("/")[0] == "https:":
        code = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_L)
        code.add_data(url)
        code.make(fit = True)
        
        image = code.make_image(fill_color = "black", back_color = "white") 
        image.save(os.environ.get("USERPROFILE")+"\\Desktop\\QRcode.png")   ## os.environ.get("USERPROFILE") 
                                                                            ## user's directory
    else:
        login.delete(0,END)
        text = "URL not detected"
        login.insert(0, text)
    
def clear():
        login.delete(0,END)



master = Tk()
master.title("QR code")
master.resizable(False, False)

maincolor = "snow2"
secondcolor = "snow"

canvas = Canvas(master, bg=maincolor, height=150, width=420)
canvas.pack()

top = Frame(canvas, bg=maincolor)
top.place(relx=0.01, rely=0.01, relwidth = 0.98, relheight = 0.45)

mid = Frame(canvas, bg=maincolor)
mid.place(relx=0.01, rely=0.50, relwidth = 0.98, relheight = 0.40)

label = Label(top, text="Enter URL : ", bg=maincolor, font="arrial 15")
label.pack(padx=1, pady=10, side=LEFT)

var = StringVar()
login = Entry(top, bd=5, font="arrial 12", bg=secondcolor, textvariable=var)
login.place(x=110, y=14, relheight=0.6, relwidth= 0.70)

send_button = Button(mid, text="Save Destop", font="arrial 12", relief="groove", bd=4, bg=secondcolor, command = lambda:send())
send_button.place(x=40, y=1, relheight=0.75, relwidth= 0.4)

clear_button = Button(mid, text="Clear", font="arrial 12", relief="groove", bd=4, bg=secondcolor, command = lambda:clear())
clear_button.place(x=230, y=1, relheight=0.75, relwidth= 0.3)       

master.mainloop()