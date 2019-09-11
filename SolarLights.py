#Solar Lights

import csv
from pprint import pprint
import geopy.distance
from gurobipy import *

#maxRange = 1.36702 #miles == 2.2km: 8 central hubs needed w/ spoke model
maxRange = 1.24274 #miles = 2km: 10 central hubs needed w/ spoke model

def csvReader():
    with open('SLights.csv', 'rt') as fin:
        reader = csv.reader(fin)
        header = next(reader)
        uncleanList = [row for row in reader]
        cleanList = []
        for row in uncleanList:
            tempList = [row[0], float(row[1]), float(row[2]), row[3]]
            cleanList.append(tempList)
        return cleanList
csvList = csvReader()

numList = []
for i in range(len(csvList)):
    numList.append([i,(float(csvList[i][1]),float(csvList[i][2]))])


distCompList = []
for i in range(len(numList)):
    distList = []
    for j in range(len(numList)):
        distance = geopy.distance.distance(numList[i][1],numList[j][1]).miles
        distList.append(distance)
    distCompList.append(distList)

m = Model("Solar Lights")
m.setParam('OutputFlag', True)

x = m.addVars(len(numList), vtype = GRB.BINARY, name='bouys')

varDict = {}
for i in range(len(distCompList)):
    varDict[i] = distCompList[i]
    m.addConstr(x[i] >= 0, name = 'nonnegativity')

for i in range(len(varDict)):
    inList = []
    for j in range(len(varDict[i])):
        if varDict[i][j] <= maxRange:
            inList.append(j)
    m.addConstr(quicksum(x[i] for i in inList) >= 1, name = 'bouys')

m.setObjective(quicksum(x[i] for i in range(len(varDict))), GRB.MINIMIZE)

m.optimize()

status_code = {1:'LOADED',2:'OPTIMAL',3:'INFEASIBLE',4:'INF_OR_UNBD',5:'UNBOUNDED'}
status = m.status
print('The optimization status is {}'.format(status_code[status]))
if status == 2:
    print('Optimal solution:')
    finalList = []
    for v in m.getVars():
        #print('%s = %g' % (v.varName, v.x))
        if v.x == 1.0:
            finalList.append(csvList[int(v.varName[v.varName.find('[') + 1:v.varName.find(']')])])

    print('Number of solar lights needed:{}'.format(m.objVal))

pprint(finalList)
