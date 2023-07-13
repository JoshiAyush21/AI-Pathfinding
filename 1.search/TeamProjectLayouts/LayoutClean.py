import os

fileList = os.listdir()

for file in fileList:
    find_ext = file.split('.')
    if len(find_ext) < 2:
        continue
    elif find_ext[1] != "lay":
        continue
    layoutFile = open(file,'r')
    layoutCleanFile = open("./cleanLayouts/"+find_ext[0]+"_clean."+find_ext[1],'w')
    lineList = layoutFile.readlines()
    writeLineList = []
    for line in lineList:
        writeLineList.append(line.replace("P"," ").replace("G"," ").replace("."," ").replace("o"," "))
    layoutCleanFile.writelines(writeLineList)
    layoutFile.close()
    layoutCleanFile.close()




