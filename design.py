import time
import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
turtle.bgcolor("black")  
turtle.pensize(2)  
turtle.speed(0)  
chance = 2
while (True):
    chance -= 1
    if chance == 0:
        exit()
    for i in range(6):  
        for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:  
            turtle.color(colors)  
            turtle.circle(100)  
            turtle.left(10)
turtle.hideturtle()  
turtle.mainloop()

