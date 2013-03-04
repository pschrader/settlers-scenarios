possibilities = []
counter = 0
# need to add a min roads variable
for settlements in range (1,6):
    for cities in range (1,5):
        for victorypointcards in range (0,6):
                for longestroad in range (0,2):
                    for largestarmy in range (0,2):
                        points = settlements + (cities * 2) + victorypointcards + (longestroad * 2) + (largestarmy * 2)
                        if ((points == 10 or points == 11) and victorypointcards < 2):
                            appendDict = {}
                            counter += 1
                            totalcards = (settlements * 4) + (cities * 5) + (victorypointcards * 3) + (largestarmy * 9) + (longestroad * 10)
                            appendDict['settlements'] = settlements
                            appendDict['cities'] = cities
                            appendDict['victorypointcards'] = victorypointcards
                            appendDict['longestroad'] = longestroad
                            appendDict['largestarmy'] = largestarmy
                            appendDict['points'] = points
                            appendDict['totalcards'] = totalcards
                            possibilities.append(appendDict)

possibilities.sort(key=lambda x: x['totalcards'])
print 'Settlements \t Cities \t VictoryPointCards \t LongestRoad \t LargestArmy \t Points \t TotalCards'
for item in possibilities:
    print item['settlements'],item['cities'],item['victorypointcards'],item['longestroad'],item['largestarmy'],item['points'],item['totalcards']
