#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:28:40 2019

@author: damienrigden
"""

class sofdot(object):
    def __init__(self, x):
        """ Initializes a Sof-Dot number.
            Sof-Dot stands for "Switch on Five - Double on Ten"
            This is a system which uses dashes and dots
            to represent numbers in two digit increments
            read from bottom to top.
            
            Input can be a positive or negative, int or float number
            Output will always be a positive 'int' sofdot
            To view an object use <instance>.plot()"""
            
        self.x = abs(int(x))
        numstr = str(self.x)
        split10 = []
        
        if len(numstr) % 2 == 0:
            for y in range(0,len(numstr),2):
                s = ''
                s += numstr[y]
                s += numstr[y+1]
                split10.append(s)
            for z in range(len(split10)):
                split10[z] = int(split10[z])
        
        else:
            split10.append(numstr[0])
            for y in range(1,len(numstr),2):
                s = ''
                s += numstr[y]
                s += numstr[y+1]
                split10.append(s)
            for z in range(len(split10)):
                split10[z] = int(split10[z])
        split10.reverse()
        self.split10 = split10
    
    @staticmethod
    def __getsofdot(number):
        """Input: A single two digit number
            Output:Returns a tuple of three lists which represent
            a binary version of a two digit segment of a sofdot number
            two lists represent the number, one list is a delimeter bar
            this function is only used within the objet class"""
        dots = number % 5
        fives = number // 5
        switchflag = False
        tenflag = False

        zero =        [0,0,0,0,0,0,0]
        five =        [1,1,1,0,0,0,0]
        fifteen =     [1,1,1,0,1,0,0]
        twentyfive =  [1,1,1,0,1,0,1]
        thirtyfive =  [1,0,1,1,1,0,0]
        fortyfive =   [1,0,1,1,1,0,1]
        fiftyfive =   [1,0,1,0,1,1,1]
        sixtyfive =   [1,1,1,1,1,0,0]
        seventyfive = [1,1,1,1,1,0,1]
        eightyfive =  [1,0,1,1,1,1,1]
        ninetyfive =  [1,1,1,0,1,1,1]
        fivedict = {1:five, 2:five, 3:fifteen, 4:fifteen, 5:twentyfive, 6:twentyfive, \
                    7:thirtyfive, 8:thirtyfive, 9:fortyfive, 10:fortyfive, \
                    11:fiftyfive, 12:fiftyfive, 13:sixtyfive, 14:sixtyfive, \
                    15:seventyfive, 16:seventyfive, 17:eightyfive, 18:eightyfive, \
                    19:ninetyfive, 0:zero}

        onedot =   [1,0,0,0,0,0,0]
        twodot =   [1,0,1,0,0,0,0]
        threedot = [1,0,1,0,1,0,0]
        fourdot =  [1,0,1,0,1,0,1]
        dotdict = {1:onedot, 2:twodot, 3:threedot, 4:fourdot, 0:zero}
  
        bar = [2,2,2,2,2,2,2]
        
        if fives % 2 == 0:
            switchflag = True
        
        if dots == 0:
            tenflag = True
        
        if switchflag and tenflag:
            return (bar, fivedict[fives], fivedict[fives])
        
        elif switchflag:
            return (bar, fivedict[fives], dotdict[dots])
        
        else:
            return (bar, dotdict[dots], fivedict[fives])
    
    @staticmethod
    def __turntostring(dotlist):
        """Input: A single binary sofdot list
            Output: A single line string of dots and dashes.
            This function is only used within the object class"""
        string = ''
        for item in dotlist:
            if item == 1:
                string += '▄'
            elif item == 0:
                string += ' '
            else:
                string += '_'
        return string
    
    def plot(self):
        """Input: A sofdot object
            Output:Plots a visual representation of a sofdot number"""
        for number in self.split10:
            sofdot = []
            sofdot = self.__getsofdot(number)
            for row in sofdot:
                print(self.__turntostring(row))
                
    def getcontrol(self):
        """Input: a sofdot object
            Output:Returns a complete list of binary data for a sofdot
            number. (This could be used to control an external program/hardware
            which would use sofdot numbers)"""
        control = []
        for number in self.split10:
            sofdot = self.__getsofdot(number)
            control.append(sofdot)
        return control
    
    def __str__(self):
        return "Use plot() to view object. Use getcontrol() for control data"     
        
    def __repr__(self):
        return 'sofdot(%r)' % self.x

    def __add__(self, other):
        return sofdot(self.x + other.x)
    
    def __sub__(self, other):
        return sofdot(self.x - other.x)
    
    def __mul__(self, other):
        return sofdot(self.x * other.x)
    
    def __truediv__(self, other):
        """Due to the nature of these numbers this is also a floor div"""
        return sofdot(self.x / other.x)
    
    def __floordiv__(self, other):
        return sofdot(self.x // other.x)
    
    def __mod__(self, other):
        return sofdot(self.x % other.x)
    
    def __pow__(self, other):
        return sofdot(self.x ** other.x)

    def __int__(self):
        return self.x
    
    def __eq__(self, other):
        if self.x == other.x:
            return True
        else:
            return False
        
    def __ne__(self, other):
        if self.x != other.x:
            return True
        else:
            return False
        
    def __lt__(self, other):
        if self.x < other.x:
            return True
        else:
            return False
    
    def __le__(self, other):
        if self.x <= other.x:
            return True
        else:
            return False
    
    def __ge__(self, other):
        if self.x >= other.x:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.x > other.x:
            return True
        else:
            return False

number = sofdot(1234567890)

number.plot()




        
        
        
            