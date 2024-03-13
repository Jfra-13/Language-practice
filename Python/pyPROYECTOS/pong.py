import turtle

#ventana 
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Marcador
marcadorA = 0
marcadorB = 0

#Jugador A
jugadorA = turtle.Turtle()
jugadorA.speed(3)
jugadorA.shape("square")
jugadorA.color("White")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid = 5,stretch_len = 1)

#Jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(3)
jugadorB.shape("square")
jugadorB.color("White")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid = 5,stretch_len = 1)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("White")
pelota.penup()
pelota.goto(0,0)

#Velocidad de la pelota
pelota.dx= 0.3
pelota.dy= 0.3

#Linea Divisoria
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador A: 0         Jugador B: 0", align = "center", font=("Courier", 24, "normal"))

#Funciones
def jugadorA_up():
    y = jugadorA.ycor()
    y = y + 20
    jugadorA.sety(y)
    
def jugadorA_down():
    y = jugadorA.ycor()
    y = y - 20
    jugadorA.sety(y)
    
def jugadorB_up():
    y = jugadorB.ycor()
    y = y + 20
    jugadorB.sety(y)
    
def jugadorB_down():
    y = jugadorB.ycor()
    y = y - 20
    jugadorB.sety(y)

#Teclado 
wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")

while True:
    wn.update()
    
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    
    #Bordes
    if pelota.ycor() > 290:
        pelota.dy *= -1
        
    if pelota.ycor() < -290:
        pelota.dy *= -1
        
    #Bordes derecha/izquierda
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("Jugador A: {}         Jugador B: {}".format(marcadorA,marcadorB), align = "center", font=("Courier", 24, "normal"))
        
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("Jugador A: {}         Jugador B: {}".format(marcadorA, marcadorB), align = "center", font=("Courier", 24, "normal"))
        
    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and (pelota.ycor() < jugadorB.ycor() + 50
            and pelota.ycor() > jugadorB.ycor() -50)):
        pelota.dx *= -1
        pelota.dy *= -1
        
    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < jugadorA.ycor() + 50
            and pelota.ycor() > jugadorA.ycor() -50)):
        pelota.dx *= -1
        pelota.dy *= -1