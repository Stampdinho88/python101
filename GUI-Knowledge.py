from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # This is mainwindow of the program
GUI.title('Program record  data') # name of the program
GUI.geometry('500x400')# size of the program

L1 = Label(GUI,text = 'Program record a Exam date schedule',font=('Angsana New',30),fg='green')
L1.place(x=60,y=0)
#############
def Button2():
    text = 'July 2023'
    messagebox.showinfo('Midterm Exam schedule',text)
    text = ('Monday, 10 July 2023 ,Math 08.00 am-11.00 am , English 13.00 pm - 15.00 pm\n'),('Wednesday, 12 July 2023 , Science 08.00 am-11.00 am.,Physics 13.00 pm -15.00 pm\n'),('Friday,14 July 2023, Social 08.00 am.-11.00 am,Chemistry 13.00 pm - 15.00 pm\n'),('Monday,17 July 2023 Biology, 08.00 am - 11.00 am,Thai 13.00 pm - 15.00 pm\n')
    messagebox.showinfo('Exam schedule',text)

FB1 = Frame(GUI)#similar board
FB1.place(x=55,y=170)
B2 = ttk.Button(FB1,text='midterm Exam schedule',command=Button2)
B2.place(x=80,y=70)
B2.pack(ipadx=20,ipady=20)
#############
def Button3():
    text = 'October 2023'
    messagebox.showinfo('Final Exam schedule',text)
    text = ('Friday, 6 October, Physics 08.00 am - 11.00 am,Biology 13.00 pm - 15.00 pm\n'),('Monday, 9 October 2023, Math 08.00 am - 11.00 am,Chemistry 13.00 pm.- 15.00 pm.\n'),('Wednesday, 11 October 2023, Social 08.00-11.00 am ,Thai 13.00 pm - 15.00 pm\n'),('Friday,13 October 2023 ,English 08.00 am - 11.00 pm, Science 13.00 pm- 15.00 pm \n')
    messagebox.showinfo('Exam schedule',text)

FB2 = Frame(GUI)#similar board
FB2.place(x= 290,y=170)
B3 = ttk.Button(FB2,text='Final Exam schedule',command=Button3)
B3.place(x=80,y=70)
B3.pack(ipadx=20,ipady=20)
#############
GUI.mainloop()