import turtle
import threading

window = turtle.Screen()
window.setup(500, 500)
t = turtle.Turtle()

direction = "right"

def up():
    global direction
    if direction == "right":
        t.left(90)
    elif direction == "down":
        t.left(180)
    elif direction == "left":
        t.right(90)
    direction = "up"
def right():
    global direction
    if direction == "up":
        t.right(90)
    elif direction == "down":
        t.left(90)
    elif direction == "left":
        t.right(180)
    direction = "right"
def left():
    global direction
    if direction == "up":
        t.left(90)
    elif direction == "down":
        t.right(90)
    elif direction == "right":
        t.right(180)
    direction = "left"
def down():
    global direction
    if direction == "up":
        t.right(180)
    elif direction == "right":
        t.right(90)
    elif direction == "left":
        t.left(90)
    direction = "right"

window.listen()
window.onkeypress(up, "w")
window.onkeypress(down, "s")
window.onkeypress(left, "a")   
window.onkeypress(right, "d")

def move_turtle():
    while True:
        t.forward(1)
        print(t.pos())
        if(t.pos()[0] > 250 or t.pos()[1] > 250 or t.pos()[0] < -250 or t.pos()[1] < -250):
            turtle.bye()


move_turtle()