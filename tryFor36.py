from random import randint

def rollDice():
    a = randint(1,6)
    b = randint(1,6)
    return a + b

def setOfDiceRolls(times):
    rolls = 0
    results = []
    while rolls < times:
        results.append(rollDice())
        rolls += 1
    return results

def perfect36():
    count = 0
    perfectDist = False
    while not(perfectDist):
        testSet = setOfDiceRolls(36)
        count += 1
        if (testSet.count(8) == 5 and testSet.count(9) == 4 and testSet.count(10) == 3 and testSet.count(11) == 2 and testSet.count(12) == 1 and testSet.count(7) == 6 and testSet.count(6) == 5 and testSet.count(5) == 4 and testSet.count(4) == 3 and testSet.count(3) == 2 and testSet.count(2) == 1):
            perfectDist = True
    return count

def startFile():
    iteration = 0
    fout = open('/home/phil/perfect36output.txt', 'w')
    fout.write('id,times\n') 
    times = perfect36()
    line = str(1)+','+str(times)+'\n' #had to be all pro stringwise no commas
    print line
    fout.write(line)
    fout.close()


def appendResults(numberToDo):
    iteration = 0
    fout = open('/home/phil/perfect36output.txt', 'a+r')
    prevData = []
    for row in fout:
        prevData.append(row.strip().split(','))
    lastrow = prevData[-1]
    lastiteration = int(lastrow[0])
    endval = numberToDo + lastiteration
    print 'id,times'
    while lastiteration < endval:
        times = perfect36()
        lastiteration += 1
        line = str(lastiteration)+','+str(times)+'\n' #had to be all pro stringwise no commas
        print line
        fout.write(line)
    fout.close()


            


        
    
