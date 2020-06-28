from tkinter import *
import os
import time


def delete_notes1():
    global filename3
    filename3 = raw_filename2.get()
    os.remove(filename3)
    screen8 = Toplevel(screen)
    screen8.geometry("300x250")
    screen8.title("view notes")
    Label(screen8, text=filename3+"removed").pack()

def delete_notes():
    global screen7
    global raw_filename2
    screen7 = Toplevel(screen)
    screen7.geometry("300x250")
    screen7.title("view notes")
    allfiles = os.listdir()
    Label(screen7, text="please use one of the file below").pack()
    Label(screen7, text=allfiles).pack()
    raw_filename2 = StringVar()
    Entry(screen7, text=raw_filename2).pack()
    Button(screen7, text="ok", command=delete_notes1).pack()


def view_notes1():
    filename1 = raw_filename1.get()
    data = open(filename1, "r")
    data1 = data.read()
    screen6 = Toplevel(screen)
    screen6.geometry("300x250")
    screen6.title("view notes")
    Label(screen6, text=data1).pack()
    data.close()


def view_notes():
    global screen5
    global raw_filename1
    screen5 = Toplevel(screen)
    screen5.geometry("300x250")
    screen5.title("view notes")
    allfiles = os.listdir()
    Label(screen5, text="please use one of the file below").pack()
    Label(screen5, text=allfiles).pack()
    raw_filename1 = StringVar()
    Entry(screen5, text=raw_filename1).pack()
    Button(screen5, text="ok", command=view_notes1).pack()


def save():
    filename = raw_filename.get()
    notes = raw_notes.get()
    data = open(filename, "w")
    data.write(notes)
    data.close()
    print("saved")


def create_notes():
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()
    global screen4
    screen4 = Toplevel(screen)
    screen4.geometry("300x250")
    screen4.title("Create notes")
    Label(screen4, text="enter the filename ").pack()
    Entry(screen4, textvariable=raw_filename).pack()
    Label(screen4, text="enter the text ").pack()
    Entry(screen4, textvariable=raw_notes).pack()
    Button(screen4, text="Save", command=save).pack()


def session():
    global screen3
    screen3 = Toplevel(screen)
    screen3.geometry("300x250")
    screen3.title("Dashbaord")
    Label(screen3, text="welcome ").pack()
    Button(screen3, text="create note", command=create_notes).pack()
    Button(screen3, text="view note", command=view_notes).pack()
    Button(screen3, text="delete note", command=delete_notes).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text="Registeration is done", fg="green",
          font="lucida 10 bold ").pack()


def login_user():
    username1 = username_verify.get()
    password1 = password_verify.get()
    password_entry1.delete(0, END)
    username_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login = Label(screen2, text="Login success",
                          fg="green", font="lucida 10 normal")
            login.pack()
            session()

        else:
            password = Label(screen2, text="Please check Password again!!",
                             fg="red", font="lucida 10 normal")
            password.pack()
    else:
        user = Label(screen2, text="User not found",
                     fg="red", font="lucida 10 normal")
        user.pack()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("300x250")
    screen1.title("Register System ")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please Enter Details below ").pack()
    Label(screen1, text="Username").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text=" ").pack()
    Button(screen1, text="Register", width=10,
           height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("300x250")
    screen2.title("Login System ")

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Please Enter Details below ").pack()
    Label(screen2, text="Username").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="Password").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10,
           height=1, command=login_user).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.wm_iconbitmap("notepad.ico")
    screen.geometry("300x300")
    screen.title("Login and Register system")
    Label(text="Notes 1.0", bg="grey", width="300",
          height="2", font="lucida 15 normal").pack()
    Button(text="Login", width="20", height=2,
           command=login).pack()
    Button(text="Register", width="20", height=2,
           command=register).pack()

    screen.mainloop()


main_screen()
