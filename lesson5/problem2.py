from turtle import *

lol = Turtle()

lol.color('yellow')
lol.pensize(6)
lol.speed(5)
lol.shape('turtle')

def drawTriangle():
	for x in range(3):
		lol.forward(100)
		lol.left(120)

def drawPizza():
	for x in range(12):
		drawTriangle()
		lol.left(30)

drawPizza()

mainloop()