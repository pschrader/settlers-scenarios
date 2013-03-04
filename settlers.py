from random import randint

#
#function definitions
#
def rollDice():
    """Roll dice takes no parameters, simulates the roll of two
    dice and returns an integer with the result"""
    a = randint(1,6)
    b = randint(1,6)
    return a + b

def diceRollDist(times):
    rolls = 0
    results = []
    while rolls < times:
        results.append(rollDice())
        rolls += 1
    print 'result \t times \t pct \t in36'
    print '------ \t ----- \t --- \t ----'
    for i in range (2,13):
        timesRolled = results.count(i)
        pctRolled = round((float(timesRolled)/float(times)) * 100,2)
        outOfThirtySix = round((float(timesRolled) * 36.0) / float(times),0)
        print i, '\t', timesRolled, '\t', pctRolled, '\t', outOfThirtySix
        
        
        

def addResource(resourceToAdd, amount, handToUpdate):
    """add Resource takes three parameters, a string indicating
    the resource to add, an integer indicating the amount
    of the resource to add, and a dictionary representing the
    hand to which the resource should be added.  Thus if you
    wanted to add 2 ore to your hand you would write:
    addResource('ore', 2, myHand)"""
    handToUpdate[resourceToAdd] += amount

def removeResource(resourceToRemove, amount, handToUpdate):
    """subtract Resource takes three parameters, a string indicating
    the resource to remove, an integer indicating the amount
    of the resource to remove, and a dictionary representing the
    hand to which the resource should be removed.  Thus if you
    wanted to remove 2 ore from your hand you would write:
    removeResource('ore', 2, myHand)"""
    handToUpdate[resourceToSubtract] -= amount

def printHand(hand):
    """printHand prints the contents of a dictionary representing
    a hand"""
    for item in hand:
        print item, ':', hand[item]

def updateHandByRoll(diceResult, payoutList, handToUpdate):
    """updateHandByRoll takes the result of a dice roll, checks a list
    containing the payoffs a player receives and a dictionary representing
    their hand.  The function checks each payout in the list and if the
    dice result matches the payout amount (stored in position 0 in each payout
    sub list) then it uses the add resource function to add the corresponding
    number of resources to the hand"""    
    #print 'Rolling:'
    #print '\t dice result: ', diceResult
    for payout in payoutList:
        i = payoutList.index(payout)
        if payoutList[i][0] == diceResult:
            addResource(payoutList[i][1],payoutList[i][2], handToUpdate)
            #print '\t payout var', payout
            #print '\t adding ', payoutList[i][2], ' ', payoutList[i][1]
            #print '\t hand now = ', handToUpdate
    #print '\t leaving updateHandByRoll'
    return handToUpdate

def repeatRoll(times, handToUpdate):
    """repeat Roll runs multiple iterations of the updateHandByRoll function"""
    rolls = 0
    while rolls < times:
        handToUpdate = updateHandByRoll(rollDice(), resourcePayouts, handToUpdate)
        rolls += 1
    return handToUpdate

def canBuildSettlement(handToTest):
    """canBuildSettlement takes a dictionary representing a hand and checks to see if
    it contains the resource mix needed to build a settlement.  it returns either true or
    false"""
    if (handToTest['brick']>=1 and handToTest['sheep']>=1 and handToTest['wheat']>=1 and handToTest['wood']>=1):
        #print 'can build a settlement'
        #print handToTest
        return True
    else:
        #print "can't build a settlement"
        return False

def tryForASettlement(testHand, resourcePayouts):
    """tryForASettlement takes a dictionary representing a hand and, if it cannot build a
    settlement with it, runs the updateHandByRoll function until it can.  it returns an integer
    representing the number of times it had to roll before it could build a settlement"""
    counter = 0
    while not(canBuildSettlement(testHand)):
        updateHandByRoll(rollDice(), resourcePayouts, testHand)
        #print 'after', counter, ' rolls:'
        counter += 1
    #resetHand(testHand)
    return counter

def resetHand(hand):
    """resetHand takes a dictionary representing a hand and sets all the resource values
    within in to zero"""
    for resource in hand:
        hand[resource] = 0

def runSimulations(gameSimulations,resourcePayouts,playHand):
    """runSimulations takes an integer indicating the number of simulations to run,
    a list of resourcePayouts, and a dictionary representing a hand.  It runs the number of
    simulations, checking to see how many rolls it took to be able to build a settlement.
    It uses the tryForASettlement function.  It returns a list of paired integers showing the
    scenario and the number of dice rolls it took in that scenario"""
    scenario = 0
    scenarioResults = []
    originalHand = dict(playHand)
    while scenario < gameSimulations:
        times = tryForASettlement(playHand, resourcePayouts)
        #print 'in scenario:', scenario,' it took',times
        scenarioResults.append([scenario,times])
        scenario += 1
        playHand = dict(originalHand)

    #print scenarioResults
    #print '======================'
    #print 'Output:'
    #print 'scenario \t rolls'
    #print '-------- \t -----'
    #for result in scenarioResults:
        #print result[0] + 1, '\t', result[1]
    return scenarioResults

def summarizeScenarios(scenarioResults, simulations):
    """summarizeScenarios takes a list of senenario results produced by runSimulations
    and creates summarized output.  Right now it also takes an integer indicating the
    number of simulations that were run but I should fix that.  It isn't necessary because I
    could just check the lenght of the list"""
    times = []
    for result in scenarioResults:
        times.append(result[1])
    #print max(times)
    print 'rolls \t times \t pct \t bynowpct'
    print '----- \t ----- \t --- \t -------'
    i = 0
    byNowPct = 0.00
    while i <= max(times):
        instanceCount = times.count(i)
        pctInstance = float(instanceCount)/float(simulations)*100
        byNowPct += pctInstance
        print i, '\t', instanceCount, '\t', pctInstance, '\t', byNowPct
        i += 1

        
    
#ACTION

#set starting variables
resourcePayouts = []
resourcePayouts.append([5, 'wheat', 1])
resourcePayouts.append([6, 'brick', 1])
resourcePayouts.append([10, 'sheep', 1])
resourcePayouts.append([2, 'wheat', 1])
resourcePayouts.append([3, 'ore', 1])
resourcePayouts.append([5, 'wood', 1])

playHand = {'brick' : 0, 'ore' : 1, 'sheep' : 0, 'wheat' : 1, 'wood' : 1}

print 'starting the action'
print '\t resourcePayouts: ', resourcePayouts

simulations = 10
resultSet = runSimulations(simulations,resourcePayouts,playHand)
summarizeScenarios(resultSet,simulations)
