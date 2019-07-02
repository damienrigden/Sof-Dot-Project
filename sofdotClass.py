#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:28:40 2019

@author: damienrigden
"""

class Sofdot(object):
    def __init__(self, x):
        """ Initializes a Sof-Dot number.
            Sof-Dot stands for "Switch on Five - Double on Ten"
            This is a system which uses dashes and dots
            to represent numbers in two digit increments
            read from bottom to top.
            
            Input can be a positive or negative, int or float number
            Output will always be a positive 'int' sofdot
            Non-supported object types will return the null character
            
            To view an object use <instance>.plot()"""
        
        try:
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

        except:
            print("Improper use detected, argument: '{}' of Type: '{}'".format(x, str(type(x))[8:-2]))
            print("Sofdot argument must be type 'int' or 'float'")
            self.split10 = [100]
            self.x = None
            
    
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
                    19:ninetyfive, 20:ninetyfive, 0:zero}

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
        if self.x == None:
            print('--Null Sofdot Detected--\n')
        
        return "Use plot() to view object. Use getcontrol() for control data."     
        
    def __repr__(self):
        return 'Sofdot(%r)' % self.x

    def __add__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')            
            
            return Sofdot(self.x + other.x)
        
        except:
            raise TypeError("unsupported operand type(s) for +: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
     
    def __sub__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')            
            
            return Sofdot(self.x - other.x)
        
        except:
            raise TypeError("unsupported operand type(s) for -: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
     
    def __mul__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')            
            
            return Sofdot(self.x * other.x)
        
        except:
            raise TypeError("unsupported operand type(s) for *: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
     
    def __truediv__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')            
            
            return Sofdot(self.x / other.x)
        
        except:
            raise TypeError("unsupported operand type(s) for /: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
     
    def __floordiv__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')            
            
            return Sofdot(self.x // other.x)
        
        except:
            raise TypeError("unsupported operand type(s) for //: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
             
    def __mod__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')            
            
            return Sofdot(self.x % other.x)
        
        except:
            raise TypeError("unsupported operand type(s) for %: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
             
    def __pow__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')
            
            return Sofdot(self.x ** other.x)
        
        except:
            raise TypeError("unsupported operand type(s) for ** or pow(): 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
     
    def __int__(self):
        if self.x == None:
            print('--Null Sofdot Detected--\n')
        
        return self.x       
        
    def __eq__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')
            
            return self.x == other.x
        
        except:
            raise TypeError("unsupported operand type(s) for ==: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
     
    def __ne__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')
            
            return self.x != other.x
        
        except:
            raise TypeError("unsupported operand type(s) for !=: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
       
    def __lt__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')            
            
            return self.x < other.x
        
        except:
            raise TypeError("unsupported operand type(s) for <: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
   
    def __le__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')            
            
            return self.x <= other.x
        
        except:
            raise TypeError("unsupported operand type(s) for <=: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
   
    def __ge__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')            
            
            return self.x >= other.x
        
        except:
            raise TypeError("unsupported operand type(s) for >=: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
   
    def __gt__(self, other):
        try:
            if self.x == None or other.x == None:
                print('--Null Sofdot Detected--\n')            
            
            return self.x > other.x
        
        except:
            raise TypeError("unsupported operand type(s) for >: 'Sofdot' and '{}'".format(str(type(other))[8:-2]))
           
#number = Sofdot(1234567890)
#null = Sofdot(None)
#
#number.plot()
#null.plot()