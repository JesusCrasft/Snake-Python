import pygame
import random
import Tkinter

def quit() :
	global Instrucciones
	Instrucciones.destroy()

Instrucciones = Tkinter.Tk()
Instrucciones.title("Instrucciones")
AB = Tkinter.Label(Instrucciones,text="Tiene 3 vidas no choques con las paredes")
AB.pack()
AC = Tkinter.Label(Instrucciones,text="Comete todos los puntos rojos")
AC.pack()
AD = Tkinter.Label(Instrucciones,text="Si quieres poner un nombre abajo")
AD.pack()
AE = Tkinter.Entry()
AE.pack()
Iniciar = Tkinter.Button(Instrucciones,text="Iniciar",command=quit)
Iniciar.pack()
Instrucciones.mainloop()