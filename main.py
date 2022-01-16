import tkinter
import datetime
import os
import random
import time
import fillpdf
from fillpdf import fillpdfs
from datetime import date
from tkinter import *
from tkinter.ttk import *


root = Tk()

# giving title to the main window
root.title("TicketGEN")

# setting the windows size
root.geometry("250x140")

# Tkinter string variable
# able to store any string value
v = StringVar(root, "1")
 
# Dictionary to create multiple buttons
values = {"Herr" : "Herr",
        "Frau" : "Frau",
        }
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(root, text = text, variable = v,
        value = value).grid(column=1)

# declaring string variable
# for storing name and password
name_var = StringVar()
passw_var = StringVar()
date_var = StringVar()

# creating a label for
# name using widget Label
name_label = Label(root, text='Anrede', font=('calibre', 10,)).place(x=25, y=0)
name_label = Label(root, text='Vorname', font=('calibre', 10,)).grid(row=3, column=0)
name_entry = Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)
passw_label = Label(root, text='Nachname', font=('calibre', 10,)).grid(row=4, column=0)
passw_entry = Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal')).grid(row=4, column=1)
date_label = Label(root, text='Geburtsdatum', font=('calibre', 10,)).grid(row=5, column=0)
date_entry = Entry(root, textvariable=date_var, font=('calibre', 10, 'normal')).grid(row=5, column=1)

# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    name=name_var.get()
    password=passw_var.get()
    gender=v.get()
    bdate=date_var.get()
    #Getting the current date according to the time zone and reformatting it to DD.MM.YYYY
    today = datetime.datetime.now()
    date_formated = today.strftime("%d.%m.%Y")

    #Randon code generator below the QR-code
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    #First thrid of the code  
    sequence = random.sample(letters,3)
    num      = random.sample(numbers,2)
    sequence.extend(num)
            
    random.shuffle(sequence)
    Code1 = ''.join([str(elem) for elem in sequence])#listToStr 

    #Second thrid of the code
    sequence = random.sample(letters,2)
    num      = random.sample(numbers,3)
    sequence.extend(num)

    random.shuffle(sequence)
    Code2 = ''.join([str(elem) for elem in sequence])#listToStr 

    #Thrid third of the code     
    sequence = random.sample(letters,3)
    num      = random.sample(numbers,2)
    sequence.extend(num)
            
    random.shuffle(sequence)
    Code3 = ''.join([str(elem) for elem in sequence])#listToStr 

    #combining all of the above and adding hyphins
    generatedcode = (Code1+'-'+Code2+'-'+Code3)

    #combining names and prefix
    NamemitAnrede = gender+" "+name+" "+password

    #translating birth date
    Geburtsdatum = bdate

    #Gets the users desktop file path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    #Filling the according space on the pdf with the provided data of the user aswell as the date
    data_dict = {'Date':date_formated,
    'Name':NamemitAnrede,
    'Geburtsdatum':Geburtsdatum,
    'Code':generatedcode,
    }
    fillpdfs.write_fillable_pdf('ticketblankstandardPUBLIC.pdf', os.path.join(desktop, 'DEIN TICKET.pdf'), data_dict, flatten=True)

   
    root=Tk()

    # giving title to the main window
    root.title("TicketGEN")
      
    w = Label(root, text ='DEIN TICKET.pdf wurde erfolgreich auf deinem Desktop gespeichert!', font = "50")
    w.pack()

    root.after(3000, root.quit)


submit_button = Button(root, text ="Submit", command = submit).grid(row=6, column=1)

root.mainloop()
