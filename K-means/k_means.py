import random
import math
import matplotlib.pyplot as plt


def getDataset(filename):
	data = []
	with open(filename) as f:
		for line in f:
			coor = line.split("\t")
			coor[0] = float(coor[0].strip())
			coor[1] = float(coor[1].strip())
			data.append(coor)
	return data


def show(data):
	for item in data:
		print(item)


def getInitialPoints(data, K):
	return random.sample(data, K)


def distance(point1, point2):
	xcoor = abs(point1[0] - point2[0])
	ycoor = abs(point1[1] - point2[1])
	return math.sqrt(xcoor*xcoor + ycoor*ycoor)

def getMinimumIndex(item, initialPoints):
	min_ind = 0
	min_dis = 99999999
	for i in range(len(initialPoints)):
		if distance(item, initialPoints[i]) < min_dis:
			min_dis = distance(item, initialPoints[i])
			min_ind = i
	return min_ind



def putDataInBuckets(initialPoints, data, K):
	buckets = [[] for i in range(K)]
	for item in data:
		min_ind = getMinimumIndex(item, initialPoints)
		buckets[min_ind].append(item)
	return buckets



def getNewMeans(buckets):
	newMean = []
	for cluster in buckets:
		xsum = 0
		ysum = 0
		for item in cluster:
			xsum += item[0]
			ysum += item[1]
		xsum = xsum/len(cluster)
		ysum = ysum/len(cluster)
		newMean.append([xsum, ysum])
	return newMean


def KMeans(data, K):
	initialPoints = getInitialPoints(data, K)
	print("Initial Points: ", initialPoints)


	while(True):
		buckets = putDataInBuckets(initialPoints, data, K)
		newMean = getNewMeans(buckets)
		if(newMean == initialPoints):
			break

		initialPoints = newMean


	return buckets



def plotGraph(array, color):
	plt.scatter([k[0] for k in array], [k[1] for k in array], c= color, alpha=0.5)



def display(buckets):
	colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
	for i in range(len(buckets)):
		plotGraph(buckets[i], colors[i])
	plt.show()



if __name__ == "__main__":
	#data = getDataset("three_clusters.txt")
	data = getDataset("four_clusters.txt")
	K = 4
	buckets = KMeans(data, K)
	display(buckets)