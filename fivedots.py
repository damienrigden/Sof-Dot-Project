#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:21:55 2019

@author: damienrigden


This program draws 5 colorful dots that count up with the seconds and reset.

"""

from graphics import GraphWin, Point, Circle
from time import strftime, sleep

win = GraphWin('Fivedots', 500, 100)

pt1 = Point(50, 50)
pt2 = Point(150, 50)
pt3 = Point(250, 50)
pt4 = Point(350, 50)
pt5 = Point(450, 50)

cir1 = Circle(pt1, 30)
cir2 = Circle(pt2, 30)
cir3 = Circle(pt3, 30)
cir4 = Circle(pt4, 30)
cir5 = Circle(pt5, 30)

cir1.setFill('red')
cir2.setFill('orange')
cir3.setFill('yellow')
cir4.setFill('green')
cir5.setFill('blue')    

ones = [1,6,11,16,21,26,31,36,41,46,51,56]
twos = [2,7,12,17,22,27,32,37,42,47,52,57]
threes = [3,8,13,18,23,28,33,38,43,48,53,58]
fours = [4,9,14,19,24,29,34,39,44,49,54,59]
fives = [0,5,10,15,20,25,30,35,40,45,50,55]    

while True:

    if int(strftime('%S')) in ones:
        cir1.undraw()
        cir1.draw(win)
        cir2.undraw()
        cir3.undraw()
        cir4.undraw()
        cir5.undraw()

    if int(strftime('%S')) in twos:
        cir2.draw(win)
    
    if int(strftime('%S')) in threes:
        cir3.draw(win)
        
    if int(strftime('%S')) in fours:
        cir4.draw(win)

    if int(strftime('%S')) in fives:
        cir5.draw(win)
          
    sleep(1)
    
    if win.checkKey() == 'q':
        win.close()
    