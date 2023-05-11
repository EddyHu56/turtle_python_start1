from turtle import *

color("yellow")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

penup()

goto(-200, 200)
pendown()

forward(200)

penup()
goto(-100, 200)
pendown()
begin_fill()
color("red")
circle(50)
end_fill()
exitonclick()