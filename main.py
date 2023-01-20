from tkinter import *

window = Tk()  # Declare a window object using Tk() method
window.geometry('349x515')  # for window size
# window.configure(width=300,height=600)         #for window size
window.title('Calculator')  # window title
window.configure(bg='light gray')
window.resizable(False, False)

value = ""
txt = StringVar()

def button_click(num):
    global value
    value = value + str(num)
    txt.set(value)

def clear_button():
    global value
    value=''
    txt.set(value)

def equal_clicked():
    global value
    result= eval(value)
    txt.set(result)
    value = ''



entry = Entry(window, textvariable=txt, bg="powderblue", bd=5, width=10,font=("default", 47))
entry.place(x=0, y=0)

btnC = Button(window, text='C', width=11, height=5, activebackground="#B6F7F8",command=lambda: clear_button())
btnC.place(x=0, y=85)

btndiv = Button(window, text='/', width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click('/'))
btndiv.place(x=87, y=85)

btnmul = Button(window, text='*', width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click('*'))
btnmul.place(x=174, y=85)

btnsub = Button(window, text='-', width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click('-'))
btnsub.place(x=261, y=85)

btn7 = Button(window, text=7, width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click(7))
btn7.place(x=0, y=171)

btn8 = Button(window, text=8, width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click(8))
btn8.place(x=87, y=171)

btn9 = Button(window, text=9, width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click(9))
btn9.place(x=174, y=171)

btn4 = Button(window, text=4, width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click(4))
btn4.place(x=0, y=257)

btn5 = Button(window, text=5, width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click(5))
btn5.place(x=87, y=257)

btn6 = Button(window, text=6, width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click(6))
btn6.place(x=174, y=257)

btn1 = Button(window, text=1, width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click(1))
btn1.place(x=0, y=343)

btn2 = Button(window, text=2, width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click(2))
btn2.place(x=87, y=343)

btn3 = Button(window, text=3, width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click(3))
btn3.place(x=174, y=343)

btn0 = Button(window, text=0, width=23, height=5, activebackground="#B6F7F8", command=lambda: button_click(0))
btn0.place(x=2, y=429)

btndot = Button(window, text='.', width=11, height=5, activebackground="#B6F7F8", command=lambda: button_click('.'))
btndot.place(x=174, y=429)

btnadd = Button(window, text='+', width=11, height=11, activebackground="#B6F7F8", command=lambda: button_click('+'))
btnadd.place(x=261, y=171)

btnequal = Button(window, text='=', width=11, height=11, activebackground="#B6F7F8", command=lambda : equal_clicked())
btnequal.place(x=261, y=347)

window.mainloop()  # to keep window active
