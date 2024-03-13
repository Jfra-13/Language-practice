import turtle
import time
import random

posponer = 0.1

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego snake")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Cuerpo Serpiente
segmentos = []


#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
        
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Teclado

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")


while True:
    wn.update()
    
    #Colisiones Bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() < 290 or cabeza.ycor() < -290:
        time.sleep(1) 
    
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        
        nuevoSegmento = turtle.Turtle()
        nuevoSegmento.speed(0)
        nuevoSegmento.shape("square")
        nuevoSegmento.penup()
        nuevoSegmento.color("grey")
        segmentos.append(nuevoSegmento)
        
    #Movimiento del cuerpo
    totalSegmentos = len(segmentos)
    for index in range(totalSegmentos -1, 0 , -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)
        
    if totalSegmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    
    mov()
    time.sleep(posponer)

