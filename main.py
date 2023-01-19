from tkinter import *

window = Tk()  # Declare a window object using Tk() method
window.geometry('349x515')  # for window size
# window.configure(width=300,height=600)         #for window size
window.title('Calculator')  # window title
window.configure(bg='light gray')
window.resizable(False, False)

screen = Text(window, font=('calibre',10,'normal'), state="disabled", width=49, height=5)
screen.place(x=0,y=0)

btnC = Button(window, text='C', width=11, height=5,activebackground="#B6F7F8")
btnC.place(x=0,y=85)

btndiv = Button(window, text='/', width=11, height=5,activebackground="#B6F7F8")
btndiv.place(x=87,y=85)

btnmul = Button(window, text='*', width=11, height=5,activebackground="#B6F7F8")
btnmul.place(x=174,y=85)

btnsub = Button(window, text='-', width=11, height=5,activebackground="#B6F7F8")
btnsub.place(x=261,y=85)

btn7 = Button(window, text=7, width=11, height=5,activebackground="#B6F7F8")
btn7.place(x=0,y=171)

btn8 = Button(window, text=8, width=11, height=5,activebackground="#B6F7F8")
btn8.place(x=87,y=171)

btn9 = Button(window, text=9, width=11, height=5,activebackground="#B6F7F8")
btn9.place(x=174,y=171)

btn4 = Button(window, text=4, width=11, height=5,activebackground="#B6F7F8")
btn4.place(x=0,y=257)

btn5 = Button(window, text=5, width=11, height=5,activebackground="#B6F7F8")
btn5.place(x=87,y=257)

btn6 = Button(window, text=6, width=11, height=5,activebackground="#B6F7F8")
btn6.place(x=174,y=257)

btn1 = Button(window, text=1, width=11, height=5,activebackground="#B6F7F8")
btn1.place(x=0,y=343)

btn2 = Button(window, text=2, width=11, height=5,activebackground="#B6F7F8")
btn2.place(x=87,y=343)

btn3 = Button(window, text=3, width=11, height=5,activebackground="#B6F7F8")
btn3.place(x=174,y=343)

btn0 = Button(window, text=0, width=23, height=5,activebackground="#B6F7F8")
btn0.place(x=2,y=429)

btndot = Button(window, text='.', width=11, height=5,activebackground="#B6F7F8")
btndot.place(x=174,y=429)

btnadd = Button(window, text='+', width=11, height=11,activebackground="#B6F7F8")
btnadd.place(x=261,y=171)

btnequal = Button(window, text='=', width=11, height=11,activebackground="#B6F7F8")
btnequal.place(x=261,y=347)



window.mainloop()  # to keep window active