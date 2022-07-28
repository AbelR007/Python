# Drawing Text inside a Heart using Turtle Graphics | Python
# =================================================
import turtle

# Object
pen = turtle.Turtle()
pen.pensize(3)
pen.color("red")

def curve():
	for i in range(200):
		pen.right(1)
		pen.forward(1)

def heart():
	pen.fillcolor('pink')
	pen.begin_fill()

	pen.left(140)
	pen.forward(113)

	curve()
	pen.left(120)

	curve()

	pen.forward(112)

	pen.end_fill()

def txt(X):

	pen.up()
	pen.setpos(-68, 95)
	pen.down()

	pen.color('lightyellow')

	pen.write(f"{X}", font=(
	"Verdana", 12, "bold"))

heart()
txt("Sophia")

pen.ht()
turtle.done()
# ================================================
# Code by Abel Roy #
