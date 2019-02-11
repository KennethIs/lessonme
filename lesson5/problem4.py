from turtle import *

lol = Turtle()

lol.color("red")
lol.pensize(6)
lol.speed(7)
lol.shape("turtle")

def DrawHex(side):
	for x in range(6):
		lol.forward(side)
		lol.left(60)

DrawHex(50)
DrawHex(75)
DrawHex(100)
DrawHex(125)
DrawHex(150)
DrawHex(175)

mainloop()