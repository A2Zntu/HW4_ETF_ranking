import math
import statistics
import random
from scipy.stats import kurtosis
from scipy.stats import skew

n = 100

data = [1, 2, 3, 4, 5, float('nan')]

# usage : data ( List of number )
def ASKSR(data):
	lamda = 1 # absolute risk aversion
	rf = 0.1 # WTF is this?


	cleanedList = [x for x in data if str(x) != 'nan']

	Dvar = statistics.stdev(cleanedList) ** 0.5
	Dmean = statistics.mean(cleanedList)
	Dkur = kurtosis(cleanedList,nan_policy = 'raise')
	Dskew = skew(cleanedList,nan_policy = 'raise')

	# print(Dkur,Dskew)

	alpha = 3 * ( abs(3 * Dkur  - 4 * (Dskew**2) - 9)**0.5) / (Dvar**2 * ( 3 * Dkur  - 5 * (Dskew**2) - 9 ) )
	beta = 3 * Dskew / ( Dvar *( 3 * Dkur  - 5 * (Dskew**2) - 9 ) )
	nn = Dmean - 3 * Dvar * Dskew / (3 * Dkur  - 4 * (Dskew**2) - 9)
	delta = 3 * Dvar * ( abs(3 * Dkur  - 5 * (Dskew**2) - 9)**0.5) / (3 * Dkur  - 4 * (Dskew**2) - 9)

	# print(alpha)
	# print(beta)
	# print(nn)
	# print(delta)



	astar = 1/lamda * (beta + alpha * (nn - rf)/(delta**2 + (nn-rf)**2)**0.5)

	ASKSR = (2 * ( lamda * astar * (nn - rf) - delta * ((alpha**2 - beta**2)**0.5  - (alpha**2 - (beta - lamda * astar)**2)) ) ) ** 0.5

	# print(abs(ASKSR))
	return abs(ASKSR)

