import Queue as Q
import sys
class ProcessA:
    def __init__(self,Name,ArrivalTime,Duration):
        self.name = Name
        self.arrivalTime = ArrivalTime
        self.duration = Duration

    def getName(self):
        return self.name

    def getArrivalTime(self):
        return self.arrivalTime

    def getDuration(self):
        return self.duration

    def __cmp__(self, other):
        return cmp(int(self.arrivalTime), int(other.arrivalTime))

    def printProcess(self):
        print self.name
        print self.arrivalTime
        print self.duration


class ProcessR:
    def __init__(self,Name ,ArrivalTime = 0,Duration=0):
        self.name = Name
        self.arrivalTime = int(ArrivalTime)
        self.duration = int(Duration)

    def getName(self):
        return self.name

    def getArrivalTime(self):
        return self.arrivalTime

    def getDuration(self):
        return self.duration

    def __cmp__(self, other):
        return cmp(int(self.duration), int(other.duration))

    def printProcess(self):
        print self.name
        print self.arrivalTime
        print self.duration


N = raw_input('How many processes you have : ')
print N
ls = []
i = 1
while(True):
    if(int(i) > int(N) ):
        break
    n = raw_input('Enter Name of process %d: ' %i)
    at = raw_input('Enter Arrival Time of process %d: ' %i)
    d = raw_input('Enter Duration of process %d: ' %i)
    obj = ProcessA(n, at, d)
    ls.append(obj)
    i += 1
print "Gantt Chart"
queueA = Q.PriorityQueue()
for x in ls:
    queueA.put(x)
var = queueA.get()
ob = ProcessR(var.name, var.arrivalTime, var.duration)
queueR = Q.PriorityQueue()
queueR.put(ob)
j = 0
while( not queueA.empty()):
    var = queueA.get()
    if(int(var.arrivalTime) == j):
        ob = ProcessR(var.name, var.arrivalTime, var.duration)
        queueR.put(ob)
    else:
        queueA.put(var)
        break
while not queueR.empty():
    Object = queueR.get()
    if(j == 0):
        i = 0
        print 0,
    else:
        i = 1
    dur = int(Object.duration)
    while(int(i) <= dur):
        while( not queueA.empty()):
            var = queueA.get()
            if(int(var.arrivalTime) == j):
                ob = ProcessR(var.name, var.arrivalTime, var.duration)
                queueR.put(ob)
            else:
                queueA.put(var)
                break
        if(not queueR.empty()):
            temp = queueR.get()
            queueR.put(temp)
            if(j == int(temp.arrivalTime) and  int(temp.duration < int(Object.duration))):
                queueR.put(Object)
                print j,
                i += 1
                j += 1
                break
        Object.duration -= 1
        if(int(i) == dur):
            print '_',j,
        else:
            print '_',
        i += 1
        j += 1

