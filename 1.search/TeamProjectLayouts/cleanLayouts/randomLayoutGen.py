import os
import random
import string

fileList = os.listdir()

largeCounter = mediumCounter = smallCounter = 30

while (largeCounter + mediumCounter + smallCounter > 0):
    for file in fileList:
        placedGoalFlag = False
        placedStartFlag = False
        finalGoalIndex = None
        finalStartIndex = None
        appendStr = ''.join(random.choices(string.ascii_lowercase,k=5))
        find_ext = file.split('.')
        if len(find_ext) < 2:
            continue
        elif find_ext[1] != "lay":
            continue
        layoutFile = open(file,'r')
        lineList = layoutFile.readlines()
        while(not placedGoalFlag):
            pickLineIndex = random.randint(0,len(lineList))-1
            pickLine = list(lineList[pickLineIndex])
            pickCharIndex = random.randint(0,len(pickLine)-1)
            if pickLine[pickCharIndex] == " ":
                pickLine[pickCharIndex] = "."
                lineList[pickLineIndex] = ("".join(pickLine))
                finalGoalIndex = (pickCharIndex,pickLineIndex)
                placedGoalFlag = True
        while(not placedStartFlag):
            pickLineIndex = random.randint(0,len(lineList))-1
            pickLine = list(lineList[pickLineIndex])
            pickCharIndex = random.randint(0,len(pickLine)-1)
            if pickLine[pickCharIndex] == " ":
                pickLine[pickCharIndex] = "P"
                lineList[pickLineIndex] = ("".join(pickLine))
                finalStartIndex = (pickCharIndex,pickLineIndex)
                placedStartFlag = True
        manhattanDistanceStr = ""
        manhattanDistance = abs(finalGoalIndex[0] - finalStartIndex[0]) + abs(finalGoalIndex[1] - finalStartIndex[1])
        if manhattanDistance < 20:
            manhattanDistanceStr = "S_"
            if smallCounter > 0:
                if not os.path.exists("./randomLayouts/"+manhattanDistanceStr+find_ext[0]+appendStr+"."+find_ext[1]):
                    layoutCleanFile = open("./randomLayouts/"+manhattanDistanceStr+find_ext[0]+appendStr+"."+find_ext[1],'w')
                    layoutCleanFile.writelines(lineList)
                    layoutCleanFile.close()
                    smallCounter -=1
        elif manhattanDistance < 40:
            manhattanDistanceStr = "M_"
            if mediumCounter > 0:
                if not os.path.exists("./randomLayouts/"+manhattanDistanceStr+find_ext[0]+appendStr+"."+find_ext[1]):
                    layoutCleanFile = open("./randomLayouts/"+manhattanDistanceStr+find_ext[0]+appendStr+"."+find_ext[1],'w')
                    layoutCleanFile.writelines(lineList)
                    layoutCleanFile.close()
                    mediumCounter -=1
        else:
            manhattanDistanceStr = "L_"
            if largeCounter > 0:
                if not os.path.exists("./randomLayouts/"+manhattanDistanceStr+find_ext[0]+appendStr+"."+find_ext[1]):
                    layoutCleanFile = open("./randomLayouts/"+manhattanDistanceStr+find_ext[0]+appendStr+"."+find_ext[1],'w')
                    layoutCleanFile.writelines(lineList)
                    layoutCleanFile.close()
                    largeCounter -=1
        # while(not placedGoalFlag or not placedStartFlag):
        #     for x in range(len(lineList)):
        #         charList = list(lineList[x])
        #         if not placedGoalFlag:
        #             for i in range(len(charList)):
        #                 if random.randint(0,len(charList)-1)==i and random.randint(0,len(lineList)-1)==i:
        #                     if charList[i] == " ":
        #                         charList[i] = "."
        #                         placedGoalFlag = True
        #                         # print("placed dot")
        #                         # print(charList)
        #                         break
        #         if not placedStartFlag:
        #             for i in range(len(charList)):
        #                 if random.randint(0,len(charList)-1)==i and random.randint(0,len(lineList)-1)==i:
        #                     if charList[i] == " ":
        #                         charList[i] = "P"
        #                         placedStartFlag = True
        #                         # print("placed P")
        #                         # print(charList)
        #                         break
        #         lineList[x] = ("".join(charList))