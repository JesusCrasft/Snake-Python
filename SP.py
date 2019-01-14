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
Iniciar = Tkinter.Button(Instrucciones,text="Iniciar",command=quit)
Iniciar.pack()
Instrucciones.mainloop()

pygame.init()
pantalla = pygame.display.set_mode((1024,600))
salir = False
relog1 = pygame.time.Clock()
rojo = (200,50,20)
azul = (70,20,100)
gris = (1,1,1)
puntos = 0
x = 400
y = 100
a = 100
b = 100
arriba = True
ancho = 15
fuente1 = pygame.font.SysFont("Arial", 20, True, False)
info = fuente1.render("Comete todos los puntos ", 0, (255,255,255))
infb = fuente1.render("Tus puntos son:"+str(puntos), 0, (255,255,255))
infa = fuente1.render("No choques", 0, (255,255,255))
recta = pygame.Rect(x,y,ancho,15)
rectb = pygame.Rect(a,b,15,15)
while salir != True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			salir = True
		if recta.colliderect(rectb):	
			ancho = ancho+15
			recta = pygame.Rect(x,y,ancho,15)	
			
	pygame.display.update()
	pantalla.fill(gris)
	pantalla.blit(info,(5,5))
	pantalla.blit(infb,(400,5))
	pantalla.blit(infa,(700,5))
	pygame.draw.rect(pantalla,azul,recta)	
	pygame.draw.rect(pantalla,rojo,rectb)	
pygame.quit()