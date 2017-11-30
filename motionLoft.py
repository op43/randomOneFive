

import random
import datetime
import queue
import threading


##Part 4 Change the writer function to be a single thread which writes from a queue

class randOneFive():
    
    def __init__(self):
        self.history = []
        self.randQueue = queue.Queue(maxsize = 0)
        
    #Generates a random number between 1 and 5 and inserts it into the history array 
    #Also insert a tuple of the number and the timestamp it was created
    def generateRand(self):
        randSeed = random.randint(0, 99);
        freqRate = [50,25,15,5,5]
        actualFreq = []
        for i in range(len(freqRate)):
            for j in range(freqRate[i]):
                actualFreq.append(i+1)
        self.addHistory(actualFreq[randSeed])
        self.randQueue.put((actualFreq[randSeed], str(datetime.datetime.now())))
    
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
        
    #worker function to write the most recent queue value into disk
    def writeToDisk(self):
        while True:
            randTuple = self.randQueue.get()
            if randTuple is None:
                break
            file = open('disk.txt','a')
            recentRand = str(randTuple[0]) + '\t' + str(randTuple[1]) + '\n'
            file.write(recentRand)
            file.close()   
            self.randQueue.task_done()
    
    #writer is a single thread that looks at writeToDisk for values in the queue
    #which it then writes the number and the timestamp into the queue
    def writer(self):
        newThread = threading.Thread(target=self.writeToDisk)
        newThread.start()
        self.randQueue.join()
        


x = randOneFive()

x.writer()    


#generate 5 threads running the generateRand()
for i in range(5):
    worker = threading.Thread(target=x.generateRand())
    worker.setDaemon(True)
    worker.start()

