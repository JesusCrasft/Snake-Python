import pygame
import random
import Tkinter

def quit() :
	global Instrucciones
	Instrucciones.destroy()

Instrucciones = Tkinter.Tk()
Instrucciones.title("Instrucciones")
AB = Tkinter.Label(Instrucciones,text="No choques con las paredes")
AB.pack()
AC = Tkinter.Label(Instrucciones,text="Comete todos los puntos rojos")
AC.pack()
Iniciar = Tkinter.Button(Instrucciones,text="Iniciar",command=quit)
Iniciar.pack()
Instrucciones.mainloop()
		
pygame.init()
pygame.display.set_caption("Snake-Python")
pantalla = pygame.display.set_mode((1024,600))
salir = False
relog1 = pygame.time.Clock()
rojo = (200,50,20)
azul = (70,20,100)
gris = (1,1,1)
puntos = 0
puntosv = 0
listasp = []
arriba = False
abajo = False
derecha = False
izquierda = False
wr = 15
hr = 15	
fuente1 = pygame.font.SysFont("Arial", 20, True, False)
info = fuente1.render("Comete todos los puntos ", 0, (255,255,255))
infb = fuente1.render("Tus puntos son:"+str(puntos), 0, (255,255,255))
infa = fuente1.render("Puntuacion Alta:"+str(puntosv), 0, (255,255,255))
for x in range(1):
	w = random.randrange(14,15)
	h = random.randrange(14,15)
	x = random.randrange(700)
	y = random.randrange(500)
	listasp.append(pygame.Rect(x,y,w,h))
recta = pygame.Rect(400,100,15,15)
rects = pygame.Rect(recta.left-10,recta.top,15,15)
rectb = pygame.Rect(x,y,w,h)
while salir != True:	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			salir = True	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				abajo = False
				arriba = True
				izquierda = False
				derecha = False
			if event.key == pygame.K_DOWN:
				arriba = False
				abajo = True
				izquierda = False
				derecha = False
			if event.key == pygame.K_LEFT:
				izquierda = True
				derecha = False
				arriba = False
				abajo = False							
			if event.key == pygame.K_RIGHT:
				derecha = True
				izquierda = False
				arriba = False
				abajo = False
		if recta.colliderect(rectb):
			rects.width += 15
			if arriba == True:
				recta.height += 15
				rects.width -= 15
			if abajo == True:	
				recta.height += 15
				rects.width -= 15
			if izquierda == True:
				recta.height -= 15
				rects.width += 15
			if derecha == True:	
				recta.height -= 15
				rects.width += 15
			for x in range(1):
				w = random.randrange(14,15)
				h = random.randrange(14,15)
				x = random.randrange(700)
				y = random.randrange(500)	
				listasp.append(pygame.Rect(x,y,w,h))	
			rectb = pygame.Rect(x,y,w,h)
			puntos += 5
			infb = fuente1.render("Tus puntos son:"+str(puntos), 0, (255,255,255))	
		if recta.top > 500:
			recta.top = 100
			recta.left = 400
			puntosv = puntos
			puntos = 0
			recta.width = 15
			recta.height = 15
			hr = 0
			wr = 0
			infb = fuente1.render("Tus puntos son:"+str(puntos), 0, (255,255,255))
			infa = fuente1.render("Puntuacion Alta:"+str(puntosv), 0, (255,255,255))
		if recta.left > 900:
			abajo = False
			recta.top = 100
			recta.left = 400
			puntosv = puntos
			puntos = 0
			recta.width = 15
			recta.height = 15
			hr = 0
			wr = 0
			infb = fuente1.render("Tus puntos son:"+str(puntos), 0, (255,255,255))
			infa = fuente1.render("Puntuacion Alta:"+str(puntosv), 0, (255,255,255))
		if recta.top < 0:
			izquierda = False
			recta.top = 100
			recta.left = 400
			puntosv = puntos
			puntos = 0
			recta.width = 15
			recta.height = 15
			hr = 0
			wr = 0
			infb = fuente1.render("Tus puntos son:"+str(puntos), 0, (255,255,255))
			infa = fuente1.render("Puntuacion Alta:"+str(puntosv), 0, (255,255,255))
		if recta.left < 0:
			arriba = False
			recta.top = 100
			recta.left = 400
			puntosv = puntos		
			puntos = 0	
			recta.width = 15
			recta.height = 15
			hr = 0
			wr = 0
			infb = fuente1.render("Tus puntos son:"+str(puntos), 0, (255,255,255))
			infa = fuente1.render("Puntuacion Alta:"+str(puntosv), 0, (255,255,255))
	if arriba == True:
		recta.move_ip(0,-10)
		rects = pygame.Rect(recta.left,recta.top-10,rects.width,rects.height)
	if abajo == True:
		recta.move_ip(0,+10)
		rects = pygame.Rect(recta.left,recta.top+10,rects.width,rects.height)
	if derecha == True:
		recta.move_ip(+10,0)
		rects = pygame.Rect(recta.left+10,recta.top,rects.width,rects.height)
	if izquierda == True:
		recta.move_ip(-10,0)	
		rects = pygame.Rect(recta.left-10,recta.top,rects.width,rects.height)

	relog1.tick(20)
	pygame.display.update()
	pantalla.fill(gris)
	pantalla.blit(info,(5,5))
	pantalla.blit(infb,(400,5))
	pantalla.blit(infa,(700,5))
	pygame.draw.rect(pantalla,azul,recta)	
	pygame.draw.rect(pantalla,azul,rects)	
	pygame.draw.rect(pantalla,rojo,rectb)
pygame.quit()