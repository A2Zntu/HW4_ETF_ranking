import math
import statistics
import pandas as pd
import random
from scipy.stats import kurtosis
from scipy.stats import skew
import csv

n = 100


# usage : 
# 	data ( List of number )
# 	rfArray ( List of number )
def ASKSR(data,rfArray):
	

	lamda = 1 # absolute risk aversion, doesn't matter in this case
	rfArray = [x for x in rfArray if str(x) != 'nan']

	rf = sum(rfArray)


	cleanedList = [x for x in data if str(x) != 'nan']


	Dvar = statistics.stdev(cleanedList) ** 0.5
	Dmean = statistics.mean(cleanedList)
	Dkur = kurtosis(cleanedList,nan_policy = 'raise')
	Dskew = skew(cleanedList,nan_policy = 'raise')


	alpha = 3 * ( abs(3 * Dkur  - 4 * (Dskew**2) - 9)**0.5) / (Dvar**2 * ( 3 * Dkur  - 5 * (Dskew**2) - 9 ) )
	beta = 3 * Dskew / ( Dvar *( 3 * Dkur  - 5 * (Dskew**2) - 9 ) )
	nn = Dmean - 3 * Dvar * Dskew / (3 * Dkur  - 4 * (Dskew**2) - 9)
	delta = 3 * Dvar * ( abs(3 * Dkur  - 5 * (Dskew**2) - 9)**0.5) / (3 * Dkur  - 4 * (Dskew**2) - 9)


	astar = 1/lamda * (beta + alpha * (nn - rf)/(delta**2 + (nn-rf)**2)**0.5)

	ASKSR = (2 * ( lamda * astar * (nn - rf) - delta * ((alpha**2 - beta**2)**0.5  - (alpha**2 - (beta - lamda * astar)**2)) ) ) ** 0.5

	return abs(ASKSR)



if __name__ == '__main__':

	A = {}
	d = pd.read_csv('../data/output_weekly_with_rf.csv')
	rf = d["Rf"].tolist()
	# print(rf)
	for key in d:
		if key == "Date":
			pass
		else:
			A[key] = ASKSR(d[key].tolist(),rf)

	sorted_x = sorted(A.items(), key=lambda kv: kv[1])
	sorted_x.reverse()
	indexr = 1
	print("|Rank|Name|ASKSR-Value|")
	print("| ------------- | ------------- |------------- | ")
	for i in sorted_x:
		if i[0] != "Rf":
			print("| {}  | {}  | {}  |".format(indexr,i[0],i[1]))
			indexr += 1