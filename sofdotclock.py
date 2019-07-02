#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:21:55 2019

@author: damienrigden

This program crates a graphical window of a clock drawn using sofdot numbers.
It takes as an argument the desired clock face size

"""

from graphics import GraphWin, Point, Circle, Rectangle
from time import strftime
from sofdotClass import Sofdot as Sd
from sys import argv


try:
    face = int(argv[1])
    if face < 50:
        face = 50

except:
    print('Argument should be an integer equal to desired clock face size.')
    print('Default face size 400 used.')
    face = 400

r = face * .075 /2
bgc = '#f8f1e2'
tgc = '#4b3106'

win = GraphWin('Sof-Dot Clock', face, face)
win.setBackground(bgc)

seconds = '%S'
minutes = '%M'
hours   = '%H'

def main():
    hourflag = strftime(hours)
    minuteflag = strftime(minutes)
    secondflag = strftime(seconds)
    
    ctrltograph(timetoctrl(seconds), secgeom)
    ctrltograph(timetoctrl(minutes), mingeom)
    ctrltograph(timetoctrl(hours), hourgeom)
    
    while True:
        if  strftime(seconds) != secondflag:  
            ctrltograph(timetoctrl(seconds), secgeom)
            secondflag = strftime(seconds)
        
        if strftime(minutes) != minuteflag:
            ctrltograph(timetoctrl(minutes), mingeom)
            minuteflag = strftime(minutes)
    
        if strftime(hours) != hourflag:
            ctrltograph(timetoctrl(hours), hourgeom)
            hourflag = strftime(hours)
        
        if win.checkKey() == 'q':
            win.close()

def timetoctrl(time):
    ctrl = Sd(strftime(time))
    
    return ctrl.getcontrol()

def ctrltograph(ctrl, elements):
    for i in range(1,3):
        for j in range(7):
            elements[0][i][j].undraw()
            if ctrl[0][i][j]:
                elements[0][i][j].draw(win)
    
    
"""Hours Geometry"""
hc8 = Point(face * .1375,face * .1375)
hc10 = Point(face * .2875,face * .1375)
hc12 = Point(face * .4375,face * .1375)
hc14 = Point(face * .5875,face * .1375)
hc1 = Point(face * .1375,face * .31875)
hc3 = Point(face * .2875,face * .31875)
hc5 = Point(face * .4375,face * .31875)
hc7 = Point(face * .5875,face * .31875)

hr5 = Point(face * .1375, face * .175)
hr6 = Point(face * .2875, face * .1)
hr7 = Point(face * .4375, face * .175)
hr8 = Point(face * .5875, face * .1)
hr1 = Point(face * .1375, face * .35625)
hr2 = Point(face * .2875, face * .28125)
hr3 = Point(face * .4375, face * .35625)
hr4 = Point(face * .5875, face * .28125)

H1 = Circle(hc1, r)
H3 = Circle(hc3, r)
H5 = Circle(hc5, r)
H7 = Circle(hc7, r)
H8 = Circle(hc8, r)
H10 = Circle(hc10, r)
H12 = Circle(hc12, r)
H14 = Circle(hc14, r)

H2 = Rectangle(hr1, hr2)
H4 = Rectangle(hr2, hr3)
H6 = Rectangle(hr3, hr4)
H9 = Rectangle(hr5, hr6)
H11 = Rectangle(hr6, hr7)
H13 = Rectangle(hr7, hr8)

#List of graphical elements structured to match the Sofdot control, hours
hourgeom = [([None], [H8, H9, H10, H11, H12, H13, H14], [H1, H2, H3, H4, H5, H6, H7])] 

#Set properties for hour elements
#triple nested loops is messy but N is small, getting around sofdot control structure
for u in range(1,3):
    for v in range(7):
        for geomh in hourgeom:
            geomh[u][v].setFill(tgc)
            geomh[u][v].setOutline(tgc)
            geomh[u][v].draw(win)

"""Minutes Geometry"""
mc8 = Point(face * .1375,face * .68125)
mc10 = Point(face * .2875,face * .68125)
mc12 = Point(face * .4375,face * .68125)
mc14 = Point(face * .5875,face * .68125)
mc1 = Point(face * .1375,face * .8625)
mc3 = Point(face * .2875,face * .8625)
mc5 = Point(face * .4375,face * .8625)
mc7 = Point(face * .5875,face * .8625)

mr5 = Point(face * .1375, face * .71875)
mr6 = Point(face * .2875, face * .64375)
mr7 = Point(face * .4375, face * .71875)
mr8 = Point(face * .5875, face * .64375)
mr1 = Point(face * .1375, face * .9)
mr2 = Point(face * .2875, face * .825)
mr3 = Point(face * .4375, face * .9)
mr4 = Point(face * .5875, face * .825)

M1 = Circle(mc1, r)
M3 = Circle(mc3, r)
M5 = Circle(mc5, r)
M7 = Circle(mc7, r)
M8 = Circle(mc8, r)
M10 = Circle(mc10, r)
M12 = Circle(mc12, r)
M14 = Circle(mc14, r)

M2 = Rectangle(mr1, mr2)
M4 = Rectangle(mr2, mr3)
M6 = Rectangle(mr3, mr4)
M9 = Rectangle(mr5, mr6)
M11 = Rectangle(mr6, mr7)
M13 = Rectangle(mr7, mr8)

#List of graphical elements structured to match the Sofdot control, minutes
mingeom = [([None], [M8, M9, M10, M11, M12, M13, M14], [M1, M2, M3, M4, M5, M6, M7])] 

#Set properties for minute elements
#triple nested loops is messy but N is small, getting around sofdot control structure
for w in range(1,3):
    for x in range(7):
        for geomm in mingeom:
            geomm[w][x].setFill(tgc)
            geomm[w][x].setOutline(tgc)
            geomm[w][x].draw(win)
           
"""Seconds Geometry"""
sc8 = Point(face * .7375,face * .8625)
sc10 = Point(face * .7375,face * .620833)
sc12 = Point(face * .7375,face * .379167)
sc14 = Point(face * .7375,face * .1375)
sc1 = Point(face * .8625,face * .8625)
sc3 = Point(face * .8625,face * .620833)
sc5 = Point(face * .8625,face * .379167)
sc7 = Point(face * .8625,face * .1375)

sr5 = Point(face * .775, face * .8625)
sr6 = Point(face * .7, face * .620833)
sr7 = Point(face * .775, face * .379167)
sr8 = Point(face * .7, face * .1375)
sr1 = Point(face * .9, face * .8625)
sr2 = Point(face * .825, face * .620833)
sr3 = Point(face * .9, face * .379167)
sr4 = Point(face * .825, face * .1375)

S1 = Circle(sc1, r)
S3 = Circle(sc3, r)
S5 = Circle(sc5, r)
S7 = Circle(sc7, r)
S8 = Circle(sc8, r)
S10 = Circle(sc10, r)
S12 = Circle(sc12, r)
S14 = Circle(sc14, r)

S2 = Rectangle(sr1, sr2)
S4 = Rectangle(sr2, sr3)
S6 = Rectangle(sr3, sr4)
S9 = Rectangle(sr5, sr6)
S11 = Rectangle(sr6, sr7)
S13 = Rectangle(sr7, sr8)

#List of graphical elements structured to match the Sofdot control, seconds
secgeom = [([None], [S8, S9, S10, S11, S12, S13, S14], [S1, S2, S3, S4, S5, S6, S7])] 


#Set properties for second elements
#triple nested loops is messy but N is small, getting around sofdot control structure
for y in range(1,3):
    for z in range(7):
        for geoms in secgeom:
            geoms[y][z].setFill(tgc)
            geoms[y][z].setOutline(tgc)
            geoms[y][z].draw(win)

"""Bar Geometry"""
bc1 = Point(face * .1375,face * .5)
bc3 = Point(face * .5875,face * .5)

br1 = Point(face * .1375,face * .5375)
br2 = Point(face * .5875,face * .4625)

B1 = Circle(bc1, r)
B3 = Circle(bc3, r)

B2 = Rectangle(br1, br2)

bargeom = [B1, B2, B3]

for geomb in bargeom:
    geomb.setFill(tgc)
    geomb.setOutline(tgc)
    geomb.draw(win)


if __name__ == '__main__':
    main() 