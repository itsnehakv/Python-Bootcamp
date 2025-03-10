import random
import turtle as t
import turtle

import colorgram
extracted_colors=[]
colors=colorgram.extract('image.jpg',30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_colors=(r,g,b)
    extracted_colors.append(new_colors)
print(extracted_colors)


color_list=[ (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
#delete the white colours (close to 255)

turtle.colormode(255)
tim=t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setheading(220)   #makes the turtle go to the left-bottom of the screen
tim.forward(260)
tim.setheading(0)     #faces right
for dot_count in range(100):  #10 rows x 10 col
    if dot_count%10==0 and not dot_count==0: # if 0 is included this would be applied to the 1st line too & will start from left instead of right
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    tim.dot(20,random.choice(color_list))      #does not require tim.pendown()
    tim.forward(50)



screen=t.Screen()
screen.exitonclick()
