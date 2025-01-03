# week 2/六角形.py

import turtle
turtle.setup(650,350,200,200)
turtle.pensize(15)
turtle.pencolor("blue")
turtle.penup()
turtle.fd(-100)
turtle.pendown()
for i in [270, 210, 150, 90, 30, -30]:
    turtle.seth(i)
    turtle.fd(60)
    turtle.seth(i-120)
    turtle.fd(60)
    turtle.seth(i-240)
    turtle.fd(120)
turtle.exitonclick()  # exitonclick() causes the turtle window to stay open until the user clicks somewhere inside that space.

