# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import *


##Part 2 change the function into a class and add more methods
class randOneFive():
    
    def __init__(self):
        self.history = []
        
    #Generates a random number between 1 and 5 and inserts it into the history array  
    def generateRand(self):
        randSeed = randint(0, 99);
        freqRate = [50,25,15,5,5]
        actualFreq = []
        for i in range(len(freqRate)):
            for j in range(freqRate[i]):
                actualFreq.append(i+1)
        self.addHistory(actualFreq[randSeed])
    
    #Add a number into the history array. If there are 100 items in the array, delete
    #the earliest one and then append the number
    def addHistory(self,num):
        if len(self.history) == 100:
            self.history.pop(0)
        self.history.append(num)
    
    #return an Array the shows the frequency each number appears in the history
    def returnFrequency(self):
        frequency = []
        for i in range(1,6):
            frequencyString = str(i) + ' is ' + str(self.history.count(i)/len(self.history)) + '%'
            frequency.append(frequencyString)
        return frequency
        


    