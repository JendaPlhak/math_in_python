#!/usr/bin/env python
from __future__ import division
from random     import sample
from math       import sqrt

import matplotlib
matplotlib.use('Agg')
from random import random, choice, gauss
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

    def __init__(self, data, k, name="img/clustering.png", cores=None):

        self.cores    = cores
        self.name     = name
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

        clrs = ['g', 'b', 'k', 'c', 'm', 'y','r']
        fig  = plt.figure(figsize=(23.5, 23.5))

        for i, cluster in enumerate(self.clusters):
            x, y = zip(*cluster.points)
            plt.plot(x, y, clrs[i]+'o', markersize=10.)
            plt.plot([cluster.centroid[0]], 
                     [cluster.centroid[1]], 
                     clrs[i]+'h', 
                     markersize=20.)
        if self.cores:
            for core in self.cores:
                plt.plot([core[0]], 
                     [core[1]], 
                     'r*', 
                     markersize=30.)


        fig.savefig(self.name, dpi=80, bbox_inches='tight')


def dataGenerator(n_clust, n_points, size=500, rand_sig=True, sig_max = 30):

    if rand_sig:
        cluster_cores = {(random()*size, random()*size):random()*sig_max for _ in xrange(n_clust)}
    else:
        cluster_cores = {(random()*size, random()*size):sig_max for _ in xrange(n_clust)}

    points = []

    for _ in xrange(n_points):
        core  = choice(cluster_cores.keys())
        sigma = cluster_cores[core]
        x = gauss(0, sigma) + core[0]
        y = gauss(0, sigma) + core[1]
        points.append((x, y))

    return points, cluster_cores



def loadData(path):

    data = []
    with open(path, 'r') as f:
        for row in f:
            pair = tuple([float(x) for x in re.findall("-?\d+\.\d+", row)])
            data.append(pair)
    return data


if __name__ == '__main__':
    
    Clustering(loadData("cluster_data.txt"), 7).performClustering()

    points, cores = dataGenerator(7, 250, rand_sig=False)
    Clustering(points, 7, cores=cores, name="img/clustering_sigma30.png").performClustering()

    points, cores = dataGenerator(7, 250, rand_sig=False, sig_max = 100)
    Clustering(points, 7, cores=cores, name="img/clustering_sigma100.png").performClustering()

    points, cores = dataGenerator(7, 250, rand_sig=False, sig_max = 50)
    Clustering(points, 7, cores=cores,  name="img/clustering_sigma50random.png").performClustering()