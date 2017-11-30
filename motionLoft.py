# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import *



def randOneFive(): 
	randSeed = randint(0, 99);
	freqRate = [50,25,15,5,5]
	actualFreq = []
	for i in range(len(freqRate)):
		for j in range(freqRate[i]):
			actualFreq.append(i+1)
	print(actualFreq[randSeed])


   


