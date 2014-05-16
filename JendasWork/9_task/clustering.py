#!/usr/bin/env python
from __future__ import division
from random     import sample
from math       import sqrt

# import matplotlib
# matplotlib.use('Agg')
import re
import matplotlib.pyplot as plt


def dist(A, B):
    return sqrt( (A[0]-B[0])**2 + (A[1]-B[1])**2 )


class Cluster(object):

    def __init__(self, centroid):
        self.centroid   = centroid
        self.points     = set()
        self.points_old = set()

    def updateCentroid(self):
        x = sum([ a[0] for a in self.points]) / len(self.points)
        y = sum([ b[1] for b in self.points]) / len(self.points)
        self.centroid = (x, y)

class Clustering(object):

    def __init__(self, data, k):

        self.data     = data
        self.k        = k
        self.clusters = []
        self.initClusters()

    def initClusters(self):
        for centroid in sample(self.data, self.k):
            self.clusters.append(Cluster(centroid))

    def performClustering(self):

        n = 0
        while True:
            self.copyOldPoints()
            self.assignPoints()
            self.updateCentroids()
            n += 1

            if not self.changed():
                self.plotResult()
                print "Clustering took %d iterations" % n
                return

    def assignPoints(self):

        for point in self.data:
            dists = [dist(point, c.centroid) for c in self.clusters]
            i     = dists.index(min(dists))
            self.clusters[i].points.add(point)


    def updateCentroids(self):
        for cluster in self.clusters:
            cluster.updateCentroid()


    def copyOldPoints(self):
        for cluster in self.clusters:
            cluster.points_old = cluster.points
            cluster.points     = set()


    def changed(self):

        for cluster in self.clusters:
            if cluster.points != cluster.points_old:
                return True
        return False


    def plotResult(self):

        clrs = ['r', 'g', 'b', 'k', 'c', 'm', 'y']
        fig  = plt.figure(figsize=(23.5, 23.5))

        for i, cluster in enumerate(self.clusters):
            x, y = zip(*cluster.points)
            plt.plot(x, y, clrs[i]+'o', markersize=10.)
            plt.plot([cluster.centroid[0]], 
                     [cluster.centroid[1]], 
                     clrs[i]+'h', 
                     markersize=20.)

        fig.savefig("img/clustering.png", dpi=80, bbox_inches='tight')





def loadData(path):

    data = []
    with open(path, 'r') as f:
        for row in f:
            pair = tuple([float(x) for x in re.findall("-?\d+\.\d+", row)])
            data.append(pair)
    return data


if __name__ == '__main__':
    
    Clustering(loadData("cluster_data.txt"), 7).performClustering()