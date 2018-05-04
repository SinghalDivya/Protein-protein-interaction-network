
# coding: utf-8
#import the required packages
import networkx as nx
import matplotlib.pyplot as plt
import math
import random
import pylab as pl
from networkx import *

#reading graph
hartford = nx.read_edgelist('Human-PPI.txt',create_using=nx.Graph(),nodetype=str)
N,K = hartford.order(), hartford.size()
avg_deg = float(K)/N
print ("Nodes: ", N)
print ("Edges: ", K)
print ("Average degree: ", avg_deg)

#calculation of clustering of each node
nx.clustering(hartford)

#to calculate degree
nx.degree(hartford)

# check if the data has been read properly or not.
nx.info(hartford) 

#To compute average clustering coefficient
nx . average_clustering ( hartford)

#To calcualte degree_distribution

T=nx.degree_histogram(hartford)
print(T)

if len(T) < 15:
 print ("Degree Fequency List:")
 print ("Degree : # of Nodes")
 
# print the degree and number of nodes that have that degree
for degree,number_of_nodes in enumerate(T):
   print ("%i : %i" % (degree,number_of_nodes))
else:
 print ("Degree Frequency List Too Long to Print")
 
# generate x,y values for degree dist. scatterplot
x_list = []
y_list = []
for degree,num_of_nodes in enumerate(T):
     if num_of_nodes > 0:
        x_list.append(degree)
        y_list.append(num_of_nodes)
 
# label the graph
pl.title('Degree Distribution\nGNP Graph')
pl.xlabel('Degree')
pl.ylabel('Frequency')
 
# plot degree distribution
pl.scatter(x_list,y_list)
pl.show()








