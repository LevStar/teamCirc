# 2nd try at a team branch/merge project

from graphics import *

def draw_circ(cX, cY, cRad, cCol, cWin):
    circ = Circle(Point(cX, cY), cRad)
    circ.setFill(cCol)
    circ.draw(cWin)

ccWin = GraphWin("Team Circ", 500, 500)
ccWin.setCoords(0, 0, 500, 500)

draw_circ(250, 250, 50, "red", ccWin)
