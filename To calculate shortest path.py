#////////////////////////////////////////////////////////////////////////////////////////////////////
#/// \file To calculate shortest path.py
#/// \brief A python program built to calculate the shortest path lengths between every pair of 
#///        proteins.
#///
#//  Author: Divya Singhal
#////////////////////////////////////////////////////////////////////////////////////////////////////

# coding: utf-8
#Import required packages
import networkx as nx
import scipy
from scipy import stats

#load the data
#load list_1 of proteins
prot_list2 = []
with open ("protein-list2.txt", 'r') as p1:
    for word in p1:
        line = word.strip().split()
        #print (line)
        prot_list2.append(line[0])
print (prot_list2)

#load list_2 of proteins
prot_list1 = []
with open ("protein-list1.txt", 'r') as p1:
    for word in p1:
        line = word.strip().split()
        #print (line)
        prot_list1.append(line[0])
print (prot_list1)

#compute the number of nodes and degree for given buman protein list.
hartford = nx.read_edgelist('Human-PPI.txt',create_using=nx.Graph(),nodetype=str)
N,K = hartford.order(), hartford.size()
avg_deg = float(K)/N
print ("Nodes: ", N)
print ("Edges: ", K)
print ("Average degree: ", avg_deg)

# To compute shortest path between each nodes of protein list_2
prot_2=[]
for i in range(0,len(prot_list2)-1):
    if prot_list2[i] in hartford.nodes():
        if prot_list2[i+1] in hartford.nodes():
              prot_2.append(nx.shortest_path_length (hartford, prot_list2[i], prot_list2[i+1]))
print(prot_2)

# To compute shortest path between each nodes of protein list_1
prot_1=[]
for i in range(0,len(prot_list1)-1):
    if prot_list1[i] in hartford.nodes():
        if prot_list1[i+1] in hartford.nodes():
            prot_1.append(nx.shortest_path_length (hartford, prot_list1[i], prot_list1[i+1]))
print(prot_1)

#To carry out the wilcox test to compare the path lengths between two proteins.

L1=(len(prot_1))
L2=(len(prot_2))
for i in range(L2,L2+(L1-L2)):
    prot_2.append(0)
    
# print the final output of wilcox test.
print (scipy.stats.wilcoxon(prot_1,prot_2,zero_method='wilcox'))





