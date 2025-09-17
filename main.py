from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if userNameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Please enter both username and password')
    elif userNameEntry.get() == 'admin' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success', 'Login Successful')
    else:
        messagebox.showerror('Error', 'Invalid username or password')


window = Tk()
window.geometry('1280x700+0+0')
window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg_L.jpg')
backLabel = Label(window, image=backgroundImage)
backLabel.place(x=0, y=0)

loginFrame = Frame(window, bg='#fff4ec')
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame, text='Username', image=usernameImage, font=('Arial', 22,), compound=LEFT, bg='#fff4ec')
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

userNameEntry = Entry(loginFrame, font=('Arial', 20), bd=5, fg= 'royal blue')
userNameEntry.grid(row=1, column=1, pady=10, padx=20)

PasswordImage = PhotoImage(file='password.png')
PasswordLabel = Label(loginFrame, text='Password', image=PasswordImage, font=('Arial', 22,), compound=LEFT, bg='#fff4ec')
PasswordLabel.grid(row=2, column=0, pady=10, padx=20)

passwordEntry = Entry(loginFrame, font=('Arial', 20), bd=5, fg= 'royal blue')
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

loginButton = Button(loginFrame, text='Login', font=('Arial', 16), bg='royal blue', fg='white', activebackground='blue', activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, column=0, columnspan=2, pady=20)

window.mainloop()