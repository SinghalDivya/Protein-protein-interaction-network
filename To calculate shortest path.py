
# coding: utf-8

# In[2]:

import networkx as nx
prot_list2 = []
with open ("protein-list2.txt", 'r') as p1:
    for word in p1:
        line = word.strip().split()
        #print (line)
        prot_list2.append(line[0])
print (prot_list2)


# In[3]:

import networkx as nx
prot_list1 = []
with open ("protein-list1.txt", 'r') as p1:
    for word in p1:
        line = word.strip().split()
        #print (line)
        prot_list1.append(line[0])
print (prot_list1)


# In[4]:

hartford = nx.read_edgelist('Human-PPI.txt',create_using=nx.Graph(),nodetype=str)
N,K = hartford.order(), hartford.size()
avg_deg = float(K)/N
print ("Nodes: ", N)
print ("Edges: ", K)
print ("Average degree: ", avg_deg)


# In[9]:

prot_2=[]
for i in range(0,len(prot_list2)-1):
    if prot_list2[i] in hartford.nodes():
        if prot_list2[i+1] in hartford.nodes():
              prot_2.append(nx.shortest_path_length (hartford, prot_list2[i], prot_list2[i+1]))
print(prot_2)


# In[10]:

prot_1=[]
for i in range(0,len(prot_list1)-1):
    if prot_list1[i] in hartford.nodes():
        if prot_list1[i+1] in hartford.nodes():
            prot_1.append(nx.shortest_path_length (hartford, prot_list1[i], prot_list1[i+1]))
print(prot_1)


# In[13]:

import scipy
from scipy import stats


# In[30]:


L1=(len(prot_1))
L2=(len(prot_2))
for i in range(L2,L2+(L1-L2)):
    prot_2.append(0)

print (scipy.stats.wilcoxon(prot_1,prot_2,zero_method='wilcox'))





