import numpy as np
from scipy import stats 
import os
import csv

alpha=0.05

dataStoragePath = "./TeamProjectData/"

dataFilesList = os.listdir(dataStoragePath)

compareMain = "mm"
compareToList = ["mm0","astar","ucs","bfs","dfs"]

# compareSet = []

# for compareTo in compareToList:
#     compareSet.append((compareMain,compareTo))

currentCompareFileList = [i for i in dataFilesList if compareMain + "_" in i]
# print(currentCompareFileList)
for compareFile in currentCompareFileList:
    compareParameterSlice = len(compareMain) + 1
    compareParameter = compareFile[compareParameterSlice:]
    # print(compareParameter)
    for compareTo in compareToList:
        pTestData1 = []
        pTestData2 = []
        compareToFile = compareTo + "_" + compareParameter
        if compareToFile in dataFilesList:
            # print("Found")
            print("comparing : " + compareMain + " To : " + compareTo + " on Parameter : " + compareParameter.split("_")[0])
            compareMainData = []
            with open(dataStoragePath + compareFile) as compareMainFileOpener:
                compareMainRows = csv.reader(compareMainFileOpener)
                for row in compareMainRows:
                    compareMainData = row
                    break
                if "Time" in compareFile:
                    pTestData1 = [float(x) for x in compareMainData]
                else:
                    pTestData1 = [int(x) for x in compareMainData]
            compareToData = []
            with open(dataStoragePath + compareToFile) as compareToFileOpener:
                compareToRows = csv.reader(compareToFileOpener)
                for row in compareToRows:
                    compareToData = row
                    break
                if "Time" in compareFile:
                    pTestData2 = [float(x) for x in compareToData]
                else:
                    pTestData2 = [int(x) for x in compareToData]
            mean1, mean2 = np.mean(pTestData1), np.mean(pTestData2)
            n = len(pTestData1)
            # sum squared difference between observations
            d1 = sum([(pTestData1[i]-pTestData2[i])**2 for i in range(n)])
            # sum difference between observations
            d2 = sum([pTestData1[i]-pTestData2[i] for i in range(n)])
            std_dev = np.sqrt((d1 - (d2**2 / n)) / (n - 1))
            # standard error of the difference between the means
            se = std_dev / np.sqrt(n)
            t_stat = (mean1 - mean2) / se
            df = n - 1
            # calculate the critical value
            critical =stats.t.ppf(1.0 - alpha, df)
            p = (1.0 - stats.t.cdf(abs(t_stat), df)) * 2.0
            # print(t_stat,critical,p)
            print(compareMain + " Mean :",mean1)
            print(compareTo + " Mean :",mean2)
            print("p Value =",p)
        else:
            raise Exception("Corresponding data missing : " + compareToFile)
