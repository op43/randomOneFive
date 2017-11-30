

import random
import time

##Part 3 Add the write to disk method
class randOneFive():
    
    def __init__(self):
        self.history = []
        
    #Generates a random number between 1 and 5 and inserts it into the history array  
    def generateRand(self):
        randSeed = random.randint(0, 99);
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
    
    #return an Array the shows the frequency each number appears in the history.
    #Return all 0's if there is no history
    def returnFrequency(self):
        frequency = []
        for i in range(1,6):
            frequencyString = ''
            if len(self.history) == 0:
                frequencyString = str(i) + ' is 0%'
            else:
                frequencyString = str(i) + ' is ' + str(self.history.count(i)/len(self.history) * 100) + '%'
            frequency.append(frequencyString)
        return frequency
        
    #writes the most recent random int in history plus the timestamp when this method was called
    #if no history exists, do nothing. If file exists, append to the next line
    def writeToDisk(self):
        file = open('disk.txt','a')
        if len(self.history) > 0:
            #python index -1 points to the last/recent object in the array
            recentRand = str(self.history[-1]) + '\t' + time.strftime("%a, %d %b %Y %H:%M:%S") + '\n'
            file.write(recentRand)
        file.close()   

