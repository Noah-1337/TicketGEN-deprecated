from ctypes import alignment
import tkinter
import datetime
import os
import random
import time
from turtle import left
import fillpdf
from fillpdf import fillpdfs
from datetime import date
from datetime import datetime
from tkinter import *
from tkinter.ttk import *
import pypdfium2


root = Tk()

# giving title to the main window
root.title("TicketGEN")

# setting the windows size
root.geometry("340x250")

# prevent any resizing of the GUI
root.resizable(False, False)

# setting icon for application
root.iconbitmap("BSVG.ico")

# Tkinter string variable
v = StringVar(root, "1")
 
# Dictionary to create multiple buttons
values = {"Herr" : "Herr",
        "Frau" : "Frau",}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(root, text = text, variable = v,
        value = value).grid(column=1)

# declaring string variable
# for storing name and surname
name_var = StringVar()
passw_var = StringVar()
date_var = StringVar()
code_var = StringVar()
datestart_var = StringVar()

# creating a label for
# name using widget Label
name_label = Label(root, text='Anrede', font=('calibre', 10,)).place(x=0, y=0)
name_label = Label(root, text='Vorname', font=('calibre', 10,)).grid(row=3, column=0, sticky=W)
name_entry = Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)
passw_label = Label(root, text='Nachname', font=('calibre', 10,)).grid(row=4, column=0, sticky=W)
passw_entry = Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal')).grid(row=4, column=1)
date_label = Label(root, text='Geburtsdatum', font=('calibre', 10,)).grid(row=5, column=0, sticky=W)
date_entry = Entry(root, textvariable=date_var, font=('calibre', 10, 'normal')).grid(row=5, column=1)
code_label = Label(root, text='Code (Optional)', font=('calibre', 10,)).grid(row=6, column=0, sticky=W)
code_entry = Entry(root, textvariable=code_var, font=('calibre', 10, 'normal')).grid(row=6, column=1)
datestart_label = Label(root, text='Startdatum/Zeit (Optional)', font=('calibre', 10,)).grid(row=7, column=0, sticky=W)
datestart_entry = Entry(root, textvariable=datestart_var, font=('calibre', 10, 'normal')).grid(row=7, column=1)


#Creatiing a drop down menu for selecting the desired ticket
# Change the label text
def show1():
	label.config( text = clicked.get() )

# Dropdown menu options
options = [
	"Fahrschein auswaehlen",
	"Monatskarte Schueler",
	"Einzelfahrschein",
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Fahrschein auswaehlen" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options ).grid(row=8, column=1)

#Creatiing a drop down menu for selecting the desired ticket
# Change the label text
def show2():
	label.config( format = clicked2.get() )

# Dropdown menu options
options = [
	"Format auswaehlen",
	"Bild",
	"PDF",
]

# datatype of menu text
clicked2 = StringVar()

# initial menu text
clicked2.set( "Format auswaehlen" )

# Create Dropdown menu
drop = OptionMenu( root , clicked2 , *options ).grid(row=9, column=1)



#Creatiing a drop down menu for selecting the desired ticket
# Change the label text
def show3():
	label.config( seitenverhältnis = clicked3.get() )

# Dropdown menu options
options = [
	"Seitenverhältnis auswaehlen",
	"Original",
	"9:19,5",
]

# datatype of menu text
clicked3 = StringVar()

# initial menu text
clicked3.set( "Seitenverhältnis auswaehlen" )

# Create Dropdown menu
drop = OptionMenu( root , clicked3 , *options ).grid(row=10, column=1)




# defining a function that will
# get the name and surname and
# print them on the screen
def submit():
 
    name=name_var.get()
    nachname=passw_var.get()
    gender=v.get()
    bdate=date_var.get()
    optionalcode=code_var.get()
    datestart=datestart_var.get()
    #Getting the current date according to the time zone and reformatting it to DD.MM.YYYY
    today = datetime.now()
    date_formated = today.strftime("%d.%m.%Y")

    #Randon code generator below the QR-code
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    #1/3 of the code  
    sequence = random.sample(letters,3)
    num      = random.sample(numbers,2)
    sequence.extend(num)
            
    random.shuffle(sequence)
    Code1 = ''.join([str(elem) for elem in sequence])#listToStr 

    #2/3 of the code
    sequence = random.sample(letters,2)
    num      = random.sample(numbers,3)
    sequence.extend(num)

    random.shuffle(sequence)
    Code2 = ''.join([str(elem) for elem in sequence])#listToStr 

    #3/3 of the code     
    sequence = random.sample(letters,3)
    num      = random.sample(numbers,2)
    sequence.extend(num)
            
    random.shuffle(sequence)
    Code3 = ''.join([str(elem) for elem in sequence])#listToStr 

    #combining all of the above and adding hyphins with the option of using a custom code from user input
    if (optionalcode == ""):
        generatedcode = (Code1+'-'+Code2+'-'+Code3)
    else:
        generatedcode = optionalcode


    #combining names and prefix
    NamemitAnrede = gender+" "+name+" "+nachname

    #translating birth date
    Geburtsdatum = bdate

    #combining names
    NameohneAnrede = name+" "+nachname

    #getting current time and formatting it
    now = datetime.now()
    currenttime = now.strftime("%H:%M")

    #adding time to the current date
    dateandtime = date_formated+" "+currenttime

    if (datestart_var != ""):
        dateandtime = datestart
        date_formated = datestart



    #Gets the users desktop file path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    text = clicked.get()
    format = clicked2.get()
    seitenverhältnis = clicked3.get()
    

    #Creating the different print options
    #Filling the according space on the pdf with the provided data of the user aswell as the date and time
    if (text == "Monatskarte Schueler" and seitenverhältnis == "Original"):
        data_dict = {'Date':date_formated,
        'Name':NamemitAnrede,
        'Geburtsdatum':Geburtsdatum,
        'Code':generatedcode,
        }
        fillpdfs.write_fillable_pdf('ticketblankmonatskartePRIVATE.pdf', os.path.join(desktop, 'DEIN TICKET.pdf'), data_dict, flatten=True)

    elif (text == "Einzelfahrschein" and seitenverhältnis == "Original"):
        data_dict = {'DateandTime':dateandtime,
        'nameohneanrede':NameohneAnrede,
        'Geburtsdatum':Geburtsdatum,
        'Code':generatedcode,
        }
        fillpdfs.write_fillable_pdf('ticketblankeinzelfahrscheinPRIVATE.pdf', os.path.join(desktop, 'DEIN TICKET.pdf'), data_dict, flatten=True)

    elif (text == "Monatskarte Schueler" and seitenverhältnis == "9:19,5"):
        data_dict = {'Date':date_formated,
        'Name':NamemitAnrede,
        'Geburtsdatum':Geburtsdatum,
        'Code':generatedcode,
        }
        fillpdfs.write_fillable_pdf('ticketblankmonatskartePRIVATEmobile.pdf', os.path.join(desktop, 'DEIN TICKET.pdf'), data_dict, flatten=True)

    elif (text == "Einzelfahrschein" and seitenverhältnis == "9:19,5"):
        data_dict = {'DateandTime':dateandtime,
        'nameohneanrede':NameohneAnrede,
        'Geburtsdatum':Geburtsdatum,
        'Code':generatedcode,
        }
        fillpdfs.write_fillable_pdf('ticketblankeinzelfahrscheinPRIVATEmobile.pdf', os.path.join(desktop, 'DEIN TICKET.pdf'), data_dict, flatten=True)







    #Check for desired format and change if desired
    if (format == "Bild"):
        
        pdffile = os.path.join(desktop, 'DEIN TICKET.pdf')
        with pypdfium2.PdfContext(pdffile) as pdf:
            image = pypdfium2.render_page_topil(pdf, 0, 30)
            output = os.path.join(desktop, 'DEIN TICKET.png')
            image.save(output)
        os.remove(pdffile)

    root=Tk()

    # giving title to the main window
    root.title("TicketGEN")
      
    w = Label(root, text ='Dein Ticket wurde erfolgreich auf deinem Desktop gespeichert!', font = "50")
    w.pack()

    root.after(4500, root.quit)


submit_button = Button(root, text ="Erstellen", command = submit).grid(row=11, column=1)

root.mainloop()