# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:18:54 2020

@author: utente
"""
try:
# Non-existent module
     import Node as Node
     import copy
     import itertools
     import matplotlib.pyplot as plt
     #import networkx as nx
except ImportError:
    print('Module not found')

class Graph:
    import networkx as nx
    
    def __init__(self, name, n):
        self.name=name
        self.nodeList=n

    def descendant(self, X):
        nodeToExplore=X
        descendant=[]
        while(len(nodeToExplore)!=0):
            Y=nodeToExplore.pop(0)
            for desc in Y.nodeout:
                if (desc not in descendant):
                    descendant.append(desc)
                    nodeToExplore.append(desc)                
        return descendant
        
    def ancestor(self, Z):
        ancestor=[]
        nodeToExplore=Z[:]
        while (len(nodeToExplore)!=0):
            L=nodeToExplore.pop(0)
            tmp=[]
            for parent in L.nodein:
                if (parent not in Z):
                    tmp.append(parent)
                    if (parent not in ancestor):
                        ancestor.append(parent)
            nodeToExplore=list (set(nodeToExplore)| set(tmp))   
        return ancestor
            
    def BFS(self,start,end):
        q=[]
        
        temp_path = [start]
        q.append(temp_path)
        result=[]
        while(len(q)!=0):
            tmp_path = q.pop(0)
            last_node = tmp_path[len(tmp_path)-1]
            #print (tmp_path)
            if (last_node == end):
                result.append(tmp_path)
                #print ("VALID_PATH : ",tmp_path)
            for link_node in last_node.nodeout:
                if link_node not in tmp_path:
                    #new_path = []
                    new_path = tmp_path + [link_node]
                    q.append(new_path)
        return result   
    
    def allPath(self,start,end):
        q=[]
        
        temp_path = [start]
        q.append(temp_path)
        path=[]
        while(len(q)!=0):
            tmp_path = q.pop(0)
            last_node = tmp_path[len(tmp_path)-1]
            #print (tmp_path)
            if (last_node == end):
                path.append(tmp_path)
                #print ("VALID_PATH : ",tmp_path)
            for link_node in list(set(last_node.nodeout)|set(last_node.nodein)):
                if link_node not in tmp_path:
                    #new_path = []
                    new_path = tmp_path + [link_node]
                    q.append(new_path)
          
        validPath=[]
        for p in path:
            if(len(p)>2):
                i=1
                flag=True
                while(i<(len(p)-1) and flag):
                    flag=not(self.checkCollider(p[i-1], p[i], p[i+1]))
                    i=i+1
                if(flag):
                    validPath.append(p)
            else:
                validPath.append(p)
        return validPath
              
    #def allValidPath(self, start, end)
    
    def checkCollider(self,A, B, C):
        if ((B in A.nodeout) and (B in C.nodeout)):
            return True
        return False

        
#    def algorithmOne(self, J, F):
#        S=Node('s')
#        H=self.nodeList
#        for j in J:
#            S.nodeout.append(j)
#            j.nodein.append(S)
#        self.nodeList.append(S)
#        matrixtmp=[]
#        #si potrebbe fare che le riga e la colonna 0 siano i nomi dei nodi
#        for i in range(len(self.nodeList)):
#            tmp=[]
#            for j in range(len(self.nodeList)):
#                tmp.append(0)
#            matrixtmp.append(tmp)
#            
#        #costruisco la matrice d'adiacenza
#        matrixAdj=[]
#        i=0
#        for x in self.nodeList:
#            j=0
#            tmp=[]
#            for y in self.nodeList:
#                if (y in x.nodeout):
#                    tmp.append(j)
#                j=j+1
#            i=i+1
#            matrixAdj.append(tmp)
#        i=0
#        s_position=len(matrixtmp)-1
#        for x in self.nodeList:
#            print(x.name)
#            if (x in J):
#                matrixtmp[i][s_position]=1
#                matrixtmp[s_position][i]=1
#            i=i+1
#        #cerco di fare la parte 3 dell'algoritmo
#        len_matrix=len(matrixtmp)
#         for i in range(len_matrix):
#             for j in range(len_matrix):                    
#                 if (matrixtmp[i][j]==1):
#                     for k in matrixAdj