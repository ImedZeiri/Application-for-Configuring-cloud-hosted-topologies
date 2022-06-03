from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
import json
from random import *
import smtplib
import pyttsx3

#############################################


def talk(text):
    say = pyttsx3.init()
    say.say(text)
    say.runAndWait()

def app():
    # Create an instance of Tkinter Frame
    win = Tk()
    win.title("Adminstrateur")

    # Set the geometry of Tkinter Frame
    win.geometry("1000x650")

    # Open the Image File
    bg = ImageTk.PhotoImage(file="Backg.png")

    # Create a Canvas
    canvas = Canvas(win, width=700, height=3500)
    canvas.pack(fill=BOTH, expand=True)

    # Add Image inside the Canvas
    canvas.create_image(0, 0, image=bg, anchor='nw')

    # Function to resize the window
    def resize_image(e):
       global image, resized, image2
       # open image to resize it
       image = Image.open("Backg.png")
       # resize the image with width and height of root
       resized = image.resize((e.width, e.height), Image.ANTIALIAS)

       image2 = ImageTk.PhotoImage(resized)
       canvas.create_image(0, 0, image=image2, anchor='nw')

    # Bind the function to configure the parent window
    win.bind("<Configure>", resize_image)


    #Entry for the token
    Entry1 = Entry(win)
    Entry1.place(relx=0.065, rely=0.373, height=50, relwidth=0.340)
    Entry1.configure(background="#EBDEF0")
    Entry1.configure(disabledforeground="#a3a3a3", bd=0)
    Entry1.configure(font="TkFixedFont")
    Entry1.configure(foreground="#000000")
    Entry1.configure(insertbackground="blue")
    Entry1.insert(0, ' Insert Token ')


    def Result():
       Frame1 = Frame(win)
       Frame1.place(relx=0.53, rely=0.125, relheight=0.81, relwidth=0.398)
       Frame1.configure(relief='solid')
       Frame1.configure(borderwidth="0")
       Frame1.configure(relief="solid")
       Frame1.configure(background="white",bd=0)


       tab_parent = ttk.Notebook(Frame1)
       tab1 = ttk.Frame(tab_parent)
       tab2 = ttk.Frame(tab_parent)
       tab_parent.add(tab1, text="Filtred Result")
       tab_parent.add(tab2, text="Original Result")
       tab_parent.pack(expand=1, fill='both')


       def Result():
          try:
              key = Entry1.get()
              url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
              payload = {}
              headers = {
                 'X-Auth-Token': key
              }
              Statut= False
              response = requests.request("GET", url, verify=Statut, headers=headers, data=payload)
              row_data = json.loads(response.text)
              if not Statut:
                  talk("Please Check Your account Statut")
                  messagebox.askyesnocancel("", "Please Check Your account Statut : Not Verified")



              f = open("DeviceList.txt", "w")
              f.write(str(row_data))
              f.close()

              f="DeviceList.txt"
              fichier = open(f,"r")
              content = fichier.read()
              fichier.close()

              text = Text(tab2,  height=41, width=45,bd=0)  #Fenêtre d'info du fichier deviceList.txt
              text.grid(column=1, row=1, padx=6, pady=6, sticky="nw")
              text.insert("end", content)

              devices = row_data["response"]

              text_widget = Text(tab1, height=40, width=55)
              text_widget.pack(side=LEFT)

              scroll_bar = Scrollbar(tab1)
            # Pack the scroll bar
              # Place it to the right side, using tk.RIGHT
              scroll_bar.pack(side=RIGHT)


              for device in devices:
                 l=("Hostname : {}".format(device["hostname"])+"\n")
                 mac=("macAddress : {}".format(device["macAddress"])+"\n")
                 soft=("softwareType : {}".format(device["softwareType"])+"\n")
                 r=("type : {}".format(device["type"])+"\n")
                 f=("serial-Number : {}".format(device["serialNumber"])+"\n")
                 i=("instance-Uuid : {}".format(device["instanceUuid"])+"\n")
                 m=("management-State : {}".format(device["managementState"])+"\n")
                 b=("boot-Date-Time : {}".format(device["bootDateTime"])+"\n")
                 t=("management-Ip-Address : {}".format(device["managementIpAddress"])+"\n")
                 mm= ("memorySize : {}".format(device["memorySize"])+"\n")
                 id=("id : {}".format(device["id"])+"\n")
                 up=("lastUpdated : {}".format(device["lastUpdated"])+"\n")
                 ping=("Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),\nDurée approximative des boucles en millisecondes :\nMinimum = 32ms, Maximum = 37ms, Moyenne = 34ms")
                 separateur=("-"*50)
                 text_widget.insert("end", l)
                 text_widget.insert("end", mac)
                 text_widget.insert("end", soft)
                 text_widget.insert("end", r)
                 text_widget.insert("end", f)
                 text_widget.insert("end", i)
                 text_widget.insert("end", m)
                 text_widget.insert("end", b)
                 text_widget.insert("end", t)
                 text_widget.insert("end", mm)
                 text_widget.insert("end", id)
                 text_widget.insert("end", up)
                 text_widget.insert("end",ping)
                 text_widget.insert("end",separateur)
          except :
              messagebox.showwarning("error","Token Exipired")

       Result()

    #Validation button
    SentImg = PhotoImage(file="sent1.png")
    B_Sent = Button(win)
    B_Sent.place(relx=0.13, rely=0.80, height=60, width=160)
    B_Sent.configure(pady="0", bd=0)
    B_Sent.configure(image=SentImg, command=Result)
    win.mainloop()

#############################################

n = randint(1000, 9999)
def try_login():               # this my login function
    if name_entry.get()==default_name and password_entry.get() == "admin":
       messagebox.showinfo("LOGIN SUCCESSFULLY","WELCOME")
       log.destroy()
       app()
    else:
        if name_entry.get()==default_name and password_entry.get() != default_password :
            messagebox.showwarning("login failed ","verifier votre mot de passe ")
        else:
            messagebox.showwarning("login failed ","verifier user name")

def cancel_login():        # exit function
    talk("Au revoir")
    log.destroy()

def ConnectGoogle():
    if password_entry.get() == "" and name_entry.get() != "":
        print(n)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('imedzairi1996@gmail.com', '20725789')
            server.sendmail('imedzairi1996@gmail.com',
                            name_entry.get(),
                            str(n))
            messagebox.showinfo("Mailling", " mail sent Successfully")
        except:
            messagebox.showwarning("error", "Error: unable to send email")
    else:
        if password_entry.get() == str(n):
           messagebox.showinfo("LOGIN SUCCESSFULLY","WELCOME")
           log.destroy()
           app()
        else:
            if password_entry.get() != str(n) :
                messagebox.showwarning("login failed ","verifier votre mot de passe ")

default_name=("admin")      #DEFAULT LOGIN ENTRY
default_password = str(n)



log = Tk()
# Set the geometry of Tkinter Frame
log.geometry("1000x650")
log.title("Login")
# Open the Image File
bg = ImageTk.PhotoImage(file="Bgl.png")
# Create a Canvas
canvas = Canvas(log, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)
# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')
# Function to resize the window
def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open("Bgl.png")
    # resize the image with width and height of root
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')
# Bind the function to configure the parent window
log.bind("<Configure>", resize_image)

lgimg = PhotoImage(file="cgb.png")
BUTTON_1=Button(log,command=try_login)
BUTTON_1.place(x=605,y=330,height=50, width=246)
BUTTON_1.configure(bd=0)
BUTTON_1.configure(image=lgimg)

CnLg = PhotoImage(file="qtb.png")
BUTTON_2=Button(log,command=cancel_login)
BUTTON_2.place(x=685,y=540,height=50, width=96)
BUTTON_2.configure(bd=0)
BUTTON_2.configure(image=CnLg)

CnGoogle = PhotoImage(file="Lgb.png")
BUTTON_3=Button(log,command=ConnectGoogle)
BUTTON_3.place(x=635,y=435,height=50, width=206)
BUTTON_3.configure(bd=0)
BUTTON_3.configure(image=CnGoogle)

name_entry=Entry(log)
name_entry.place(x=560, y=140)
password_entry=ttk.Entry(log,show="*")
password_entry.place(x=560, y=220)

log. mainloop()