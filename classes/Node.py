# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:29:24 2020

@author: utente
"""

class Node:
    #definisco la classe node nel seguente modo:
    #nome del nodo (name)
    #nodi in entrata(node in)
    #nodi in uscita(node out)
    #in caso di grafo non orientato i nodi in entrata coincideranno con i nodi 
    #in uscita
    def __init__(self, name):
        self.name=name
        self.nodein=[]
        self.nodeout=[]
    
    def set_nodein(self, nodein):
        self.nodein=nodein
        
    def set_nodeout(self, nodeout):
        self.nodeout=nodeout
        
    def categorize(self):
        if (len(self.nodein)>1):
            for adj in self.nodein:
                for adj2 in self.nodein:
                    if(adj.name != adj2.name):
                        print(adj.name+"-->" + self.name+"<--"+adj2.name)
        
        if (len(self.nodeout)>1):
            for adj in self.nodeout:
                for adj2 in self.nodeout:
                    if(adj.name != adj2.name):
                        print(adj.name+"<--" + self.name+"-->"+adj2.name)
                        
        adjList=[]
        for adj in self.nodein:
            adjList.append(adj)
            nodeout=list(set(self.nodeout)- set(adjList))
            for adj2 in nodeout:
                if(adj.name != adj2.name):
                    print(adj.name+"-->" + self.name+"-->"+adj2.name)
    
   
   
        
            