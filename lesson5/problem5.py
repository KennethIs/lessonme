from turtle import *

star = Turtle()

star.color("red")
star.pensize(6)
star.speed(7)
star.shape("classic")

def DrawStar():
	for x in range(5):
		star.forward(50)
		star.left(144)

DrawStar()

mainloop()