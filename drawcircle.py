import math
import turtle as t 

# draw the circle using turtle
def drawCircleTurtle(x, y, r) :
    # move to the start of circle
    t.up()
    t.setpos(x + r, y)
    t.down()
     
    #draw the circle
    for i in range (0, 365, 5):
         a = math.radians(i)
         t.setpos(x + r*math.cos(a), y + r*math.sin(a))

drawCircleTurtle(200, 100, 50)
t.mainloop()

