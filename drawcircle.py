import math
import turtle as t 

# draw the circle using turtle
# def drawCircleTurtle(x, y, r) :
#     # move to the start of circle
#     t.up()
#     t.setpos(x + r, y)
#     t.down()
     
#     #draw the circle
#     for i in range (0, 365, 5):
#          a = math.radians(i)
#          t.setpos(x + r*math.cos(a), y + r*math.sin(a))

# drawCircleTurtle(200, 100, 50)
# t.mainloop()

# print("hello, world!")

# 太阳线
# import turtle as t
# import time
# t.color("red","yellow")
# t.speed(10)
# t.begin_fill()
# for x in range(50):
#     t.forward(200)
#     t.left(170)
# end_fill()
# time.sleep(2)

#彩虹线

# import turtle as t 
# from random import randint as rint
# t.shape("turtle")
# t.pensize(5)
# t.colormode(255)
# t.bgcolor("black")
# t.tracer(False)
# for x in range(700):
#     t.color(rint(0,255),rint(0,255),rint(0,255))
#     t.circle(2*(1+x/4),5)
#     t.speed(30)
#     t.tracer(True)