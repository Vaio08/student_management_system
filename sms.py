from tkinter import *
from PIL import ImageTk
import time
from tkinter import ttk, messagebox
from tkinter.ttk import Treeview
import sqlite3

# functions

def add_student():
    def addData():
        if idEntry.get() == '' or nameEntry.get() == '' or mobileEntry.get() == '' or emailEntry.get() == '' or addressEntry.get() == '' or genderEntry.get() == '' or dobEntry.get() == '':
            messagebox.showerror('Error', 'All Fields are Required', parent=addWindow)
        else:
                current_date = time.strftime('%d-%m-%Y') # Correct date format
                current_time = time.strftime('%H:%M:%S') # Correct time format
                con = sqlite3.connect('studentManagementSystem.db')
                mycursor = con.cursor()
                query = 'INSERT INTO student(id, name, mobile, email, address, gender, dob, date, time) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'
                values = (idEntry.get(), nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get(), current_date, current_time)
                mycursor.execute(query, values)
                con.commit()
                result = messagebox.askyesno('Confirm','Data Successfully Added. Do you want to clean the form?', parent=addWindow)
                print(result)
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    mobileEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    dobEntry.delete(0, END)
                else:
                    pass
                
                query = 'SELECT * FROM student'
                mycursor.execute(query)
                fetched_data = mycursor.fetchall()
                studentTable.delete(*studentTable.get_children())
                for data in fetched_data:
                    dataList = list(data)
                    studentTable.insert('', END, values=dataList)
                    
                
    addWindow = Toplevel()
    addWindow.grab_set()
    addWindow.resizable(False, False)
    idLabel = Label(addWindow, text='Id:', font=('Arial', 16, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=10, sticky=W)
    idEntry = Entry(addWindow, font=('Arial', 16), bd=5, fg='royal blue')
    idEntry.grid(row=0, column=1, padx=20, pady=10)
    nameLabel = Label(addWindow, text='Name:', font=('Arial', 16, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=10, sticky=W)
    nameEntry = Entry(addWindow, font=('Arial', 16), bd=5, fg='royal blue')
    nameEntry.grid(row=1, column=1, padx=20, pady=10)
    mobileLabel = Label(addWindow, text='Mobile:', font=('Arial', 16, 'bold'))
    mobileLabel.grid(row=2, column=0, padx=20, pady=10, sticky=W)
    mobileEntry = Entry(addWindow, font=('Arial', 16), bd=5, fg='royal blue')
    mobileEntry.grid(row=2, column=1, padx=20, pady=10)
    emailLabel = Label(addWindow, text='Email:', font=('Arial', 16, 'bold'))
    emailLabel.grid(row=3, column=0, padx=20, pady=10, sticky=W)
    emailEntry = Entry(addWindow, font=('Arial', 16), bd=5, fg='royal blue')
    emailEntry.grid(row=3, column=1, padx=20, pady=10)
    addressLabel = Label(addWindow, text='Address:', font=('Arial', 16, 'bold'))
    addressLabel.grid(row=4, column=0, padx=20, pady=10, sticky=W)
    addressEntry = Entry(addWindow, font=('Arial', 16), bd=5, fg='royal blue')
    addressEntry.grid(row=4, column=1, padx=20, pady=10)
    genderLabel = Label(addWindow, text='Gender:', font=('Arial', 16, 'bold'))
    genderLabel.grid(row=5, column=0, padx=20, pady=10, sticky=W)
    genderEntry = Entry(addWindow, font=('Arial', 16), bd=5, fg='royal blue')
    genderEntry.grid(row=5, column=1, padx=20, pady=10)
    dobLabel = Label(addWindow, text='DOB:', font=('Arial', 16, 'bold'))
    dobLabel.grid(row=6, column=0, padx=20, pady=10, sticky=W)
    dobEntry = Entry(addWindow, font=('Arial', 16), bd=5, fg='royal blue')
    dobEntry.grid(row=6, column=1, padx=20, pady=10)
    
    addStudentButton = Button(addWindow, text='ADD STUDENT', command=addData, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
    addStudentButton.grid(row=7, columnspan=2, pady=20)
    
    
# DATABASE CONNECTION

def connect_database():
    def connect():
        global mycursor, con
        try:
            # Use a file name for SQLite, not host
            db_name = hostEntry.get()
            if not db_name:
                messagebox.showerror('Error', 'Please enter database file name', parent=connectWindow)
                return
            con = sqlite3.connect(db_name)
            mycursor = con.cursor()
            # Create table if not exists
            try: 
                query = '''CREATE TABLE IF NOT EXISTS student(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    mobile TEXT,
                    email TEXT,
                    address TEXT,
                    gender TEXT,
                    dob TEXT,
                    date TEXT,
                    time TEXT
                )'''
                mycursor.execute(query)
                con.commit()
            except:
                query = 'use studentManagementSystem'
                mycursor.execute(query)
            
            messagebox.showinfo('Success', 'Database Connection Successful', parent=connectWindow)
            connectWindow.destroy()
            # Enable buttons after successful connection
            for btn in [addstudent_button, searchstudent_button, deletestudent_button, updatestudent_button, showstudent_button, exportstudent_button]:
                btn.config(state=NORMAL)
        except Exception as e:
            messagebox.showerror('Error', f'Invalid Details\n{e}', parent=connectWindow)

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x200+730+250')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0, 0)

    hostName = Label(connectWindow, text='Database File:', font=('Arial', 16, 'bold'))
    hostName.grid(row=0, column=0, padx=20, pady=10)
    hostEntry = Entry(connectWindow, font=('Arial', 16), bd=5, fg='royal blue')
    hostEntry.grid(row=0, column=1, padx=20, pady=10)
    hostEntry.insert(0, 'studentManagementSystem.db')  # Default file name

    connectBotton = Button(connectWindow, text='Connect', command=connect, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
    connectBotton.grid(row=1, columnspan=2, pady=20)

# clock
def clock():
    date = time.strftime('%d-%m-%Y')
    current_time = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'Date: {date}\nTime: {current_time}')
    datetimeLabel.after(1000, clock)

# GUI
root = Tk()
root.geometry('1280x700+0+0')
root.title("Student Management System")
root.resizable(0, 0)

# Safe image loading
try:
    bgImage = ImageTk.PhotoImage(file='bg.jpg')
except Exception:
    bgImage = None
backLabel = Label(root, image=bgImage, bg='#fff4ec')
backLabel.place(x=0, y=0)

datetimeLabel = Label(root, font=('Arial', 16), bg='#fff4ec', fg='black')
datetimeLabel.place(x=3, y=3)
clock()

s = 'STUDENT MANAGEMENT SYSTEM'
headLabel = Label(root, text=s, font=('Arial', 30, 'bold'), bg='#fff4ec', fg='black')
headLabel.place(x=320, y=10)

connectButton = Button(root, text='Connect to Database', command=connect_database, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
connectButton.place(x=1020, y=15)

leftFrame = Frame(root, bg='#fff4ec', width=300, height=600)
leftFrame.place(x=50, y=80)

try:
    logo_image = PhotoImage(file='student_logo.png')
except Exception:
    logo_image = None
logoLabel = Label(leftFrame, image=logo_image, bg='#fff4ec')
logoLabel.grid(row=0, column=0)

addstudent_button = Button(leftFrame, text='Add Student', width=20, state=DISABLED, command=add_student, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2')
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

exitstudent_button = Button(leftFrame, text='Exit', width=20, font=('Arial', 16), bg='#fff4ec', fg='black', activebackground='#eab676', activeforeground='white', cursor='hand2', command=root.destroy)
exitstudent_button.grid(row=7, column=0, pady=15)

rightFrame = Frame(root, bg='#fff4ec')
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