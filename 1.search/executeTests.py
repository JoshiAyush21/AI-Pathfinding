import subprocess
import os
# import string
import csv
import datetime

trialLayoutPath = "./TeamProjectLayouts/cleanLayouts/randomLayouts/"
dataStoragePath = "./TeamProjectData/"
if not os.path.exists(dataStoragePath):
    os.mkdir(dataStoragePath)
fileList = os.listdir(trialLayoutPath)
execTimeSuffix = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

algoritmList = [
    "astar,heuristic=manhattanHeuristic",
    "mm",
    "mm0",
    "bfs",
    "dfs",
    "ucs"
]

for algo in algoritmList:
    smallCostList = []
    smallTimeList = []
    smallNodeList = []
    mediumCostList = []
    mediumTimeList = []
    mediumNodeList = []
    largeCostList = []
    largeTimeList = []
    largeNodeList = []
    # for x in range(len(fileList)):
    #     fileList[x] = fileList[x].split(".")[0]
    # print(fileList)
    # print(subprocess.run("dir /b",shell=True,capture_output=True).stdout.decode("utf-8").split())
    #CompletedProcess(args='python .\\pacman.py -l .//TeamProjectLayouts//cleanLayouts//randomLayouts//S_trickySearch_cleantrnen.lay -q -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic', returncode=0, stdout=b"('cost', 20)\r\n('runtime ms', 0.0)\r\n('nodes expanded', 32)\r\n", stderr=b'')
    for file in fileList:
        outStr = subprocess.run(
            "python pacman.py -l " + trialLayoutPath + file + " -q -p SearchAgent -a fn=" + algo, shell=True, capture_output=True
        ).stdout.decode("utf-8").splitlines()
        cost = int(outStr[0].split().pop().replace(")",""))
        time = float(outStr[1].split().pop().replace(")",""))
        node = int(outStr[2].split().pop().replace(")",""))
        if file.split('_')[0] == "S":
            smallCostList.append(cost)
            smallTimeList.append(time)
            smallNodeList.append(node)
        elif file.split('_')[0] == "M":
            mediumCostList.append(cost)
            mediumTimeList.append(time)
            mediumNodeList.append(node)
        elif file.split('_')[0] == "L":
            largeCostList.append(cost)
            largeTimeList.append(time)
            largeNodeList.append(node)
    #python .\pacman.py -l bigMaze -q -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

    algoName = algo.split(",")[0]

    smallCostFile = open(dataStoragePath + algoName + "_smallCost_" + execTimeSuffix + ".csv",'w')
    smallTimeFile = open(dataStoragePath + algoName + "_smallTime_" + execTimeSuffix + ".csv",'w')
    smallNodeFile = open(dataStoragePath + algoName + "_smallNode_" + execTimeSuffix + ".csv",'w')
    mediumCostFile = open(dataStoragePath + algoName + "_mediumCost_" + execTimeSuffix + ".csv",'w')
    mediumTimeFile = open(dataStoragePath + algoName + "_mediumTime_" + execTimeSuffix + ".csv",'w')
    mediumNodeFile = open(dataStoragePath + algoName + "_mediumNode_" + execTimeSuffix + ".csv",'w')
    largeCostFile = open(dataStoragePath + algoName +"_largeCost_" + execTimeSuffix + ".csv",'w')
    largeTimeFile = open(dataStoragePath + algoName +"_largeTime_" + execTimeSuffix + ".csv",'w')
    largeNodeFile = open(dataStoragePath + algoName +"_largeNode_" + execTimeSuffix + ".csv",'w')  

    writer = csv.writer(smallCostFile)
    writer.writerow(smallCostList)
    smallCostFile.close()

    writer = csv.writer(smallTimeFile)
    writer.writerow(smallTimeList)
    smallTimeFile.close()

    writer = csv.writer(smallNodeFile)
    writer.writerow(smallNodeList)
    smallNodeFile.close()

    writer = csv.writer(mediumCostFile)
    writer.writerow(mediumCostList)
    mediumCostFile.close()

    writer = csv.writer(mediumTimeFile)
    writer.writerow(mediumTimeList)
    mediumTimeFile.close()

    writer = csv.writer(mediumNodeFile)
    writer.writerow(mediumNodeList)
    mediumNodeFile.close()

    writer = csv.writer(largeCostFile)
    writer.writerow(largeCostList)
    largeCostFile.close()

    writer = csv.writer(largeTimeFile)
    writer.writerow(largeTimeList)
    largeTimeFile.close()

    writer = csv.writer(largeNodeFile)
    writer.writerow(largeNodeList)
    largeNodeFile.close()