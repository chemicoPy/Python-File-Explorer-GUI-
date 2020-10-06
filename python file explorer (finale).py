import tkinter
from tkinter.messagebox import askquestion
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import shutil
import os


root = Tk()


root.title(" Welcome to this File explorer system ! .")



def open():
    textbox = ScrolledText()
    # textbox.grid()
    files = askopenfilename(initialdir='c:\\python31\\',
                            filetypes=[('Text files', '.txt'), ('All files', '*')])

    textbox.insert('1', files)


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


def nothing():
    from tkinter import messagebox
    msg = messagebox.showinfo("Warning", "No function assigned yet!.")


def helpline():
    from tkinter import messagebox
    msg = messagebox.showinfo("Problems with operations?", "Reach out to Abiola David.")


def About():
    from tkinter import messagebox
    msg = messagebox.showinfo(' system file explorer tkinter program.')


def quit():
    answer = askquestion(title='Quit?', message='Really quit?')
    if answer == 'yes':
        root.destroy()


root.protocol('WM_DELETE_WINDOW', quit)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0, bd=2, bg='orange')
filemenu.add_command(label="New", command=nothing)
filemenu.add_command(label="Open", command=open)
filemenu.add_command(label="Save", command=nothing)
filemenu.add_command(label="Save as...", command=nothing)
filemenu.add_command(label="Close", command=nothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0, bd=2, bg='brown')
editmenu.add_command(label="Undo", command=nothing)

editmenu.add_separator()
editmenu.add_command(label="Cut", command=nothing)
editmenu.add_command(label="Copy", command=nothing)
editmenu.add_command(label="Paste", command=nothing)
editmenu.add_command(label="Delete", command=nothing)
editmenu.add_command(label="Select All", command=nothing)
menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0, bd=2, bg='purple')
helpmenu.add_command(label="Help Index", command=nothing)
helpmenu.add_command(label="About...", command=About)
helpmenu.add_command(label='Call Author?.', command=helpline)
menubar.add_cascade(label="Help", menu=helpmenu)
aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label='About Project', command=About)

root.config(menu=menubar)




def CreateWidgets():

    link_Label = Label(root, text="Choose File To Work on : ", bg="blue")
    link_Label.place(x=395, y=272)

    root.sourceText = Entry(root, width=50, textvariable=sourceLocation)
    root.sourceText.place(x=540, y=272)

    source_browseButton = Button(root, text="Browse", command=SourceBrowse, width=15)
    source_browseButton.place(x=860, y=272)

    destinationLabel = Label(root, text="Select The Destination  : ", bg="green")
    destinationLabel.place(x=395, y=372)

    root.destinationText = Entry(root, width=50, textvariable=destinationLocation)
    root.destinationText.place(x=540, y=372)

    dest_browseButton = Button(root, text="Browse", command=DestinationBrowse, width=15)
    dest_browseButton.place(x=860, y=372)

    action = ttk.Combobox(root, textvariable=work, values=['Copy', 'Move', 'Delete File'])
    action.place(x=575, y=542)




def SourceBrowse():
    root.files_list = list(filedialog.askopenfilenames(initialdir='c:\\python31\\',
                                                       filetypes=[('Text files', '.txt'), ('All files', '*')]))

    root.sourceText.insert('1', root.files_list)


def DestinationBrowse():
    destinationdirectory = filedialog.askdirectory(initialdir='c:\\python31\\')
    root.destinationText.insert('1', destinationdirectory)






def ok():

    from tkinter import messagebox

    action = work.get()

    if action == 'Copy':
        from tkinter import messagebox

        files_list = root.files_list
        destination_location = destinationLocation.get()

        for f in files_list:
            shutil.copy(f, destination_location)

        messagebox.showinfo(" SUCCESS ", "File successfully copied !.")

    elif action == 'Move':
        from tkinter import messagebox

        files_list = root.files_list

        destination_location = destinationLocation.get()

        for f in files_list:
            shutil.move(f, destination_location)

        messagebox.showinfo(" SUCCESS ", "File successfully moved !.")

    elif action =='Delete File':

        answer = askquestion(title='Delete File?', message='This file will be erased, do you wish to continue?')

        while answer == 'yes':
            shutil.os.remove(str(sourceLocation))
            messagebox.showinfo(" SUCCESS ", "File deleted !.")
            break


    return



okButton = Button(root, text="Ok", font=('calibri', 11, 'bold'), foreground='darkblue', width=10, command=ok)
okButton.place(x=750, y=540)

actionlabel = Label(root, text="What to do?", font=('batang', 9, 'bold'), borderwidth='4')
actionlabel.place(x=465, y=540)


work = StringVar()
sourceLocation = StringVar()
destinationLocation = StringVar()

CreateWidgets()

root.configure(bg='darkred')

root.mainloop()

