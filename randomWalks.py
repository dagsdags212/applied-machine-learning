import random

class Location(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def move(self, deltaX, deltaY):
		''' deltaX and deltaY are floats '''
		return Location(self.x + deltaX, self.y + deltaY)

	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
	
	def distFrom(self, other):
		xDist = self.x - other.getX()
		yDist = self.y - other.getY()
		return (xDist**2 + yDist**2) ** 0.5
	
	def __str__(self):
		return "<" + str(self.x) + "," + str(self.y) + ">"


class Drunk(object):
	def __init__(self, name = None):
		""" Assume name is a str """
		self.name = name
		
	def __str__(self):
		if self != None:
			return self.name
		return 'Anonymous'


class UsualDrunk(Drunk):
	def takeStep(self):
		stepChoices = [(0,1), (0,-1), (1,0), (-1,0)]
		return random.choice(stepChoices)


class MasochistDrunk(Drunk):
	def takeStep(self):
		stepChoices = [(0.0,1.1), (0.0,-0.9), (1.0,0.0), (-1.0,0.0)]
		return random.choice(stepChoices)


class Field(object):
	def __init__(self):
        # Key => Drunk object, value => Location object
		self.drunks = {}
		
	def addDrunk(self, drunk, loc):
		if drunk in self.drunks:
			raise ValueError('Duplicate drunk')
		else:
			self.drunks[drunk] = loc
			
	def getLoc(self, drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')
		return self.drunks[drunk]
	
	def moveDrunk(self, drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')
		xDist, yDist = drunk.takeStep()
		# use move method of Location to get new Location
		self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)

def walk(f, d, numSteps):
	""" Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0 
	Moves d numSteps times; returns the distance between the final location and the location at the start of the walk. """
	start = f.getLoc(d)
	for s in range(numSteps):
		f.moveDrunk(d)
	return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
	""" Assumes numSteps an int >= 0, numTrials an int > 0, dClass a subclass of Drunk.
	Simulates numTrials walks of numSteps steps each. Returns a list of the final distances for each trial """
	Homer = dClass()
	origin = Location(0, 0)
	distances = []
	for t in range(numTrials):
		f = Field()
		f.addDrunk(Homer, origin)
		distances.append(round(walk(f, Homer, numTrials), 1))
	return distances

def drunkTest(walkLengths, numTrials, dClass):
	""" Assumes walkLengths a sequence of ints >= 0, numTrials an int > 0, dClass a subclass of Drunk.
	For each number of steps in walkLengths, runs simWaks with numTrials and prints results """
	for numSteps in walkLengths:
		distances = simWalks(numSteps, numTrials, dClass)
		print(dClass.__name__, 'random walk of', numSteps, 'steps')
		print('Mean =', round(sum(distances)/len(distances)), 4)
		print('Max =', max(distances), 'Min =', min(distances))

# drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
# drunkTest((0, 1, 2), 100, UsualDrunk)
drunkTest((1000, 10000), 100, MasochistDrunk)

# Plotting results (an example)
import pylab

xVals = [1,2,3,4]
yVals1 = [1,2,3,4]
pylab.plot(xVals, yVals1, 'b-', label = 'first')
yVals2 = [1,7,3,5]
pylab.plot(xVals, yVals2, 'r--', label = 'second')
pylab.legend()

# Random walks with wormholes
class OddField(Field):
	def __init__(self, numHoles = 1000, xRange = 100, yRange = 100):
		Field.__init__(self)
		self.wormholes = {}
		for w in range(numHoles):
			x = random.randint(-xRange, xRange)
			y = random.randint(-yRange, yRange)
			newX = random.randint(-xRange, xRange)
			newY = random.randint(-yRange, yRange)
			newLoc = Location(newX, newY)
			self.wormholes[(x, y)] = newLoc
	
	def moveDrunk(self, drunk):
		Field.moveDrunk(self, drunk)
		x = self.drunks[drunk].getX()
		y = self.drunks[drunk].getY()
		if (x, y) in self.wormbholes:
			self.drunks[drunk] = self.wormhole[(x, y)]