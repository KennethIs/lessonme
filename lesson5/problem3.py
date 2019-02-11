from turtle import *

lol = Turtle()

lol.color("red")
lol.pensize(6)
lol.speed(7)
lol.shape("turtle")

def DrawHex():
	for x in range(6):
		lol.forward(100)
		lol.left(60)

DrawHex()

mainloop()