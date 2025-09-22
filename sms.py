from tkinter import *
from PIL import ImageTk
import time
from tkinter import ttk
from tkinter.ttk import Treeview


#function to display time and date
def clock():
    date = time.strftime('%d-%m-%Y')
    current_time = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'     Date: {date}\n Time: {current_time}')
    datetimeLabel.after(1000, clock)


#GUI 
root = Tk()

root.geometry('1280x700+0+0')
root.title("Student Management System")
root.resizable(0, 0)

bgImage = ImageTk.PhotoImage(file='bg.jpg')
backLabel = Label(root, image=bgImage, )
backLabel.place(x=0, y=0)

datetimeLabel = Label(root, text= clock, font=('Arial', 16), bg='#fff4ec', fg='black')
datetimeLabel.place(x=3, y=3)
clock()

s = 'STUDENT MANAGEMENT SYSTEM'
headLabel = Label(root, text=s, font=('Arial', 30, 'bold'), bg='#fff4ec', fg='black')
headLabel.place(x=320, y=10)

connectButton = Button(root, text='Connect to Database', font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
connectButton.place(x=1020, y=15)

leftFrame = Frame(root, bg='#fff4ec', width=300, height=600)
leftFrame.place(x=50, y=80)

logo_image = PhotoImage(file='student_logo.png')
logoLabel = Label(leftFrame, image=logo_image, bg='#fff4ec')
logoLabel.grid(row=0, column=0)

addstudent_button = Button(leftFrame, text='Add Student', width=20, state=DISABLED, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
addstudent_button.grid(row=1, column=0, pady=15)

searchstudent_button = Button(leftFrame, text='Search Student', width=20, state=DISABLED, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
searchstudent_button.grid(row=2, column=0, pady=15)

deletestudent_button = Button(leftFrame, text='Delete Student', width=20, state=DISABLED, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
deletestudent_button.grid(row=3, column=0, pady=15)

updatestudent_button = Button(leftFrame, text='Update Student', width=20, state=DISABLED, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
updatestudent_button.grid(row=4, column=0, pady=15)

showstudent_button = Button(leftFrame, text='Show Student', width=20, state=DISABLED, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
showstudent_button.grid(row=5, column=0, pady=15)

exportstudent_button = Button(leftFrame, text='Export Student', width=20, state=DISABLED, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
exportstudent_button.grid(row=6, column=0, pady=15)

exitstudent_button = Button(leftFrame, text='Exit', width=20, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
exitstudent_button.grid(row=7, column=0, pady=15)

rightFrame = Frame(root, bg='#fff4ec' )
rightFrame.place(x=360, y=80, width=900, height=600)

ScrollbarX = Scrollbar(rightFrame, orient=HORIZONTAL)
ScrollbarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = Treeview(rightFrame, columns=('Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 
                                             'DOB', 'Added Date', 'Added Time'), 
                                            xscrollcommand=ScrollbarX.set, yscrollcommand=ScrollbarY.set) 
ScrollbarX.config(command=studentTable.xview)
ScrollbarY.config(command=studentTable.yview)

ScrollbarX.pack(side=BOTTOM, fill=X)
ScrollbarY.pack(side=RIGHT, fill=Y)
studentTable.pack(fill='both', expand=True)

studentTable.config(show='headings')

studentTable.heading('Id', text='Id')
studentTable.heading('Name', text='Name')
studentTable.heading('Mobile', text='Mobile')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('DOB', text='DOB')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')



root.mainloop()