import random
import datetime
import sys

def createMaze( wallRatio, rectLength, rectWidth):
	walkable = ' '
	bounds = 'b'
	obstacles = '%'
	notSearched = 'n'
	searched = 's'
	length = rectLength
	width = rectWidth
	obstacle_ratio = wallRatio
	maze = []
	obstacleList = []
	walkableList = []
	searchList = []

	for x in range(length):
		nextLine = []
		for y in range(width):
			nextLine.append(notSearched)
		maze.append(nextLine)

	for x in range(length):
		for y in range(width):
			if (x == 0 or y == 0 or x == length-1 or y == width-1):
				maze[x][y] = bounds

	startSelectedFlag = False
	allProcessedFlag = False
	startCoords = (0,0)

	while(not allProcessedFlag):
		while(not startSelectedFlag):
			startCoords = (random.randint(0,length-1),random.randint(0,width-1))
			if maze[startCoords[0]][startCoords[1]] == notSearched:
				startSelectedFlag = True
				searchList.append(startCoords)
				# walkableList.append(startCoords)

		while (len(searchList) > 0):
			# print("pathing")
			nextCoord = searchList.pop(0)
			if maze[nextCoord[0]][nextCoord[1]] == searched:
				continue
			maze[nextCoord[0]][nextCoord[1]] = searched
			if not (nextCoord in walkableList or nextCoord in obstacleList):
				walkableList.append(nextCoord)
			newCoordList = [
				(nextCoord[0] - 1,nextCoord[1]),
				(nextCoord[0] + 1,nextCoord[1]),
				(nextCoord[0],nextCoord[1] - 1),
				(nextCoord[0],nextCoord[1] + 1)
			]
			for newCoord in newCoordList:
				if newCoord[0] in range(1,length-1) and newCoord[1] in range(1,width-1):
					if not newCoord in obstacleList:
						if random.random() <= obstacle_ratio and (nextCoord in walkableList or nextCoord in obstacleList):
							obstacleList.append(newCoord)
						else:
							searchList.append(newCoord)
		allProcessedFlag = True
		for x in range(length):
			for y in range(width):
				# if maze[x][y] == notSearched and not ((x,y) in obstacleList or (x,y) in walkableList):
				if maze[x][y] == notSearched:
					# obstacleList.append((x,y))
					allProcessedFlag = False
					searchList.append((x,y))

	connectedList = []
	connectedList.append(walkableList[0])
	connectedGraphList = []
	disconnectedList = []

	for node in walkableList:
		disconnectedList.append(node)

	while not len(connectedGraphList) == len(walkableList):
		# print(len(connectedGraphList))
		# print(len(walkableList))
		connectedListAlteredFlag = True
		newConnectedNodeList = []
		while connectedListAlteredFlag:
			# print(connectedList)
			for node in connectedList:
				x,y = node
				neighborList = [
					(x - 1,y),
					(x + 1,y),
					(x,y - 1),
					(x,y + 1)
				]
				for checkNode in walkableList:
					if checkNode in connectedGraphList:
						if checkNode in disconnectedList:
							disconnectedList.remove(checkNode)
						continue
					if checkNode in neighborList:
						if not checkNode in newConnectedNodeList:
							newConnectedNodeList.append(checkNode)
						if checkNode in disconnectedList:
							disconnectedList.remove(checkNode)
					else:
						if not checkNode in disconnectedList:
							disconnectedList.append(checkNode)
				if not node in connectedGraphList:
					connectedGraphList.append(node)
			while len(connectedList) > 0:
				node = connectedList.pop()
				if not node in connectedGraphList:
					connectedGraphList.append(node)
			if len(newConnectedNodeList) > 0:
				connectedListAlteredFlag = True
			else:
				connectedListAlteredFlag = False
			for node in newConnectedNodeList:
				if not (node in connectedList or node in connectedGraphList):
					connectedList.append(node)
			newConnectedNodeList = []
		# print("deleting walls")
		# print(disconnectedList)
		if len(disconnectedList) > 0:
			for node in disconnectedList:
				x,y = node
				neighborList = [
					(x - 1,y),
					(x + 1,y),
					(x,y - 1),
					(x,y + 1)
				]
				
				removeObstacleNode = random.choice(neighborList)
				if removeObstacleNode[0] in range(1,length-1) and removeObstacleNode[1] in range(1,width-1):
						if removeObstacleNode in obstacleList:
							obstacleList.remove(removeObstacleNode)
							if not removeObstacleNode in walkableList:
								walkableList.append(removeObstacleNode)
		for node in connectedGraphList:
			connectedList.append(node)
		# print(len(connectedGraphList))
		# print(len(walkableList))

	for obstacleCoord in obstacleList:
		maze[obstacleCoord[0]][obstacleCoord[1]] = obstacles

	for walkCoord in walkableList:
		maze[walkCoord[0]][walkCoord[1]] = walkable

	for x in range(length):
		for y in range(width):
			if maze[x][y] == bounds:
				maze[x][y] = obstacles

	fileLines = []
	for line in maze:
		fileLines.append("".join(line)+"\n")

	lastLine = fileLines.pop().replace('\n',"")
	fileLines.append(lastLine)

	execTimeSuffix = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
	layoutCleanFile = open("RandomSparseMaze_"+str(length)+"_"+str(width)+"_"+execTimeSuffix,'w')
	layoutCleanFile.writelines(fileLines)
	layoutCleanFile.close()

def default(str):
    return str + ' [Default: %default]'

def readCommand( argv ):
	from optparse import OptionParser
	usageStr = """
	USAGE:      	python randomSparseMazeGen.py <options>
	EXAMPLES:   	(1) python randomSparseMazeGen.py
			- generates default 30x30 maxe with wall ratio = 30%
			(2) python randomSparseMazeGen.py -l 20 -h 10
			- generates default 20x10 maxe with wall ratio = 30%
"""
	parser = OptionParser(usageStr)

	parser.add_option('-r', '--wallRatio', dest='wallRatio', type='float',
                      help=default('Ratio of how many maze cells should be attepmted to turn to walls'), metavar='WALL_RATIO', default=0.3)
	parser.add_option('-l', '--length', dest='rectLength',
                      help=default('Length of rectangle maze to generate.'),
                      metavar='RECTANGLE_LENGTH', default=30)
	parser.add_option('-w', '--width', dest='rectWidth',
                      help=default('Width of rectangle maze to generate.'),
                      metavar='RECTANGLE_WIDTH', default=30)

	options, unidentified_options = parser.parse_args(argv)
	if len(unidentified_options) != 0:
		raise Exception('Unidentified options found : ' + str(unidentified_options))
	args = dict()
	args['wallRatio'] = float(options.wallRatio)
	args['rectLength'] = int(options.rectLength)
	args['rectWidth'] = int(options.rectWidth)
	return args


if __name__ == '__main__':
    args = readCommand( sys.argv[1:] ) # Get game components based on input
    createMaze( **args )