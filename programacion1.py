#Developer: Test
from Tkinter import *
import ttk
import os
import subprocess
import tkFont
import tkMessageBox



def encender17():
    print("Encendido 17")
    os.system("sudo /./home/uth/Programacion/on17.sh")

def apagar17():
    print("Apagado 17")
    os.system("sudo /./home/uth/Programacion/off17.sh")

def encender27():
    print("Encendido 27")
    os.system("sudo /./home/uth/Programacion/on27.sh")

def apagar27():
    print("Apagado 27")
    os.system("sudo /./home/uth/Programacion/off27.sh")

def cerrar():
    v0.destroy()

#crear ventana
v0=Tk()
v0.title("Control GPIO")
v0.geometry("400x300+0+0")

#Fuente
texto1 = tkFont.Font(family = "Helvetica", size = 18)
texto2 = tkFont.Font(family = "Helvetica", size = 14)

#Zona de etiqueta
label1 =  Label(v0, text="CONTROL GPIO", font = texto1).place(x=100, y=5)
label2 =  Label(v0, text="Control GPIO 17", font = texto2).place(x=10, y=40)
label2 =  Label(v0, text="Control GPIO 27", font = texto2).place(x=10, y=120)


#Zona de Botones
btn_on17 = Button(v0, text="ON", command=encender17).place(x=10, y=65)
btn_off17 = Button(v0, text="OFF", command=apagar17).place(x=60, y=65)

btn_on27 = Button(v0, text="ON", command=encender27).place(x=10, y=145)
btn_off27 = Button(v0, text="OFF", command=apagar27).place(x=60, y=145)

btn_close = Button(v0, text="CERRAR", command=cerrar).place(x=300, y=250)


v0.mainloop()

