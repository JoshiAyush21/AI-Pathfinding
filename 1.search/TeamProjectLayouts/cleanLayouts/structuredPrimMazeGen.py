import random
import datetime
import sys

def createMaze( connectChance, rectLength, rectWidth):
	obstacle = '%'
	walkable = ' '
	bounds = 'b'
	notSearched = 'n'
	length = rectLength
	width = rectWidth
	passageConnectionChance = connectChance
	maze = []
	obstacleList = []

	for x in range(length):
		nextLine = []
		for y in range(width):
			nextLine.append(notSearched)
		maze.append(nextLine)

	for x in range(length):
		for y in range(width):
			if (x == 0 or y == 0 or x == length-1 or y == width-1):
				maze[x][y] = bounds

	# print("maze init")
	# for line in maze:
	# 	print("".join(line))

	startSelectedFlag = False

	while not startSelectedFlag:
		startCoords = (random.randint(1,length-2),random.randint(1,width-2))
		start_x, start_y = startCoords

		if maze[start_x][start_y] == notSearched:
			maze[start_x][start_y] = walkable
			startSelectedFlag = True

	neighborList = [
					(start_x - 1,start_y),
					(start_x + 1,start_y),
					(start_x,start_y - 1),
					(start_x,start_y + 1)
				]

	for node in neighborList:
		x, y = node
		if maze[x][y] == notSearched:
			maze[x][y] = obstacle
			obstacleList.append(node)

	# print("maze state")
	# for line in maze:
	# 	print("".join(line))

	while(obstacleList):
		# print("building")
		# print(obstacleList)
		randomObstacle = random.choice(obstacleList)
		# print(randomObstacle)
		obstacleList.remove(randomObstacle)
		rx, ry = randomObstacle
		neighborList = [
			(rx - 1,ry),
			(rx + 1,ry),
			(rx,ry - 1),
			(rx,ry + 1)
		]
		neighborWalkableCount = 0
		for node in neighborList:
			x, y = node
			if maze[x][y] == walkable:
				neighborWalkableCount += 1
		if random.random() <= passageConnectionChance:
			maze[rx][ry] = walkable
			for node in neighborList:
				x, y = node
				if maze[x][y] == notSearched:
					maze[x][y] = obstacle
					obstacleList.append(node)
		elif neighborWalkableCount < 2:
			# print("candidateFound")
			if maze[rx-1][ry] == walkable and (maze[rx+1][ry] == notSearched or maze[rx+1][ry] == bounds):
				maze[rx][ry] = walkable
				for node in neighborList:
					x, y = node
					if maze[x][y] == notSearched:
						maze[x][y] = obstacle
						obstacleList.append(node)
			elif maze[rx+1][ry] == walkable and (maze[rx-1][ry] == notSearched or maze[rx-1][ry] == bounds):
				maze[rx][ry] = walkable
				for node in neighborList:
					x, y = node
					if maze[x][y] == notSearched:
						maze[x][y] = obstacle
						obstacleList.append(node)
			elif maze[rx][ry-1] == walkable and (maze[rx][ry+1] == notSearched or maze[rx][ry+1] == bounds):
				maze[rx][ry] = walkable
				for node in neighborList:
					x, y = node
					if maze[x][y] == notSearched:
						maze[x][y] = obstacle
						obstacleList.append(node)
			elif maze[rx][ry+1] == walkable and (maze[rx][ry-1] == notSearched or maze[rx][ry-1] == bounds):
				maze[rx][ry] = walkable
				for node in neighborList:
					x, y = node
					if maze[x][y] == notSearched:
						maze[x][y] = obstacle
						obstacleList.append(node)
		# print("maze state")
		# for line in maze:
		# 	print("".join(line))

	for x in range(0, length):
		for y in range(0, width):
			if (maze[x][y] == notSearched):
				maze[x][y] = obstacle

	for x in range(length):
		for y in range(width):
			if maze[x][y] == bounds:
				maze[x][y] = obstacle

	fileLines = []
	for line in maze:
		fileLines.append("".join(line)+"\n")

	lastLine = fileLines.pop().replace('\n',"")
	fileLines.append(lastLine)

	execTimeSuffix = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
	layoutCleanFile = open("StructuredPrimMaze_"+str(length)+"_"+str(width)+"_"+execTimeSuffix,'w')
	layoutCleanFile.writelines(fileLines)
	layoutCleanFile.close()

def default(str):
    return str + ' [Default: %default]'

def readCommand( argv ):
	from optparse import OptionParser
	usageStr = """
	USAGE:      	python structuredPrimMazeGen.py <options>
	EXAMPLES:   	(1) python structuredPrimMazeGen.py
			- generates default 30x30 maxe with connection chance = 20%
			(2) python structuredPrimMazeGen.py -l 20 -h 10
			- generates default 20x10 maxe with connection chance = 20%
"""
	parser = OptionParser(usageStr)

	parser.add_option('-c', '--connectChance', dest='connectChance', type='float',
                      help=default('Ratio of how often to connect nearby passages'), metavar='CONNECT_CHANCE', default=0.2)
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
	args['connectChance'] = float(options.connectChance)
	args['rectLength'] = int(options.rectLength)
	args['rectWidth'] = int(options.rectWidth)
	return args


if __name__ == '__main__':
    args = readCommand( sys.argv[1:] ) # Get game components based on input
    createMaze( **args )