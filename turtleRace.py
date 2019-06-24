from turtle import *
from random import randint
penup()
speed(0)
goto(-140, 140)

for step in range(13):
    write(step, align = "center")
    right(90)
    forward(10)
    for step in range(5):
        pendown()
        forward(15)
        penup()
        forward(15)
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color("red")
ada.shape("turtle")
ada.penup()
ada.goto(-160, 100)
ada.pendown()
for turn in range(1):
    ada.right(360)

bob = Turtle()
bob.color("blue")
bob.shape("turtle")
bob.penup()
bob.goto(-160, 70)
bob.pendown()
for turn in range(1):
    bob.right(360)

may = Turtle()
may.color("magenta")
may.shape("turtle")
may.penup()
may.goto(-160, 40)
may.pendown()
for turn in range(1):
    may.right(360)

jay = Turtle()
jay.color("orange")
jay.shape("turtle")
jay.penup()
jay.goto(-160, 10)
jay.pendown()
for turn in range(1):
    jay.right(360)



for turn in range(95):
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    may.forward(randint(1, 5))
    jay.forward(randint(1, 5))
