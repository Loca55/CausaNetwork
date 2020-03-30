# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:12:48 2020

@author: mloca
"""
try:
# Non-existent module
     from classes.Node import Node as node
     from classes.Graph import Graph as graph
     import dsep 
     import itertools
     import copy
except ImportError:
    print('Module not found')

def rule1 (G, X, Z, W, Y):
    result = []
    tmp = X.nodein
    X.nodein = []
    for j in tmp:
        j.nodeout = list(set(j.nodeout) - set([X]))

    subset=list(set(W)|set([X]))
    R=dsep.reachable(G, Z, subset)
    if(Y not in R):
        result.append(R)
        
    for j in tmp:
        j.nodeout = list(set(j.nodeout)|set([X]))
        
    X.nodein = tmp
    return result

def rule2(G, X, Z, W, Y):
    result=[]
    tmpX=X.nodein
    X.nodein=[]
    for x in tmpX:
        x.nodeout = list(set(j.nodeout) - set([X]))
        
    tmpZ=Z.nodeout
    Z.nodeout=[]
    for z in tmpZ:
        z.nodeout = list(set(z.nodeout) - set([Z]))
        
    subset=list(set(W)|set([X]))
    R=dsep.reachable(G, Z, subset)
    if(Y not in R):
        result.append(R)
        
def rule2(G, X, Z, W, Y):
    result=[]
    if not(X==[]):
        tmpX=X.nodein
        X.nodein=[]
        for x in tmpX:
            x.nodeout = list(set(x.nodeout) - set([X]))
        
    tmpZ=Z.nodeout
    Z.nodeout=[]
    for z in tmpZ:
        z.nodeout = list(set(z.nodeout) - set([Z]))
        
    subset=list(set(W)|set([X]))
    R=dsep.reachable(G, Z, subset)
    if(Y not in R):
        result.append(R)
        
def rule3(G, X, Z, W, Y):
    G1=copy.deepcopy(G)
    result=[]
    ancestor=[]
    Wname=[]
    subset=[]
    
    for w in W:
        Wname.append(w.name)
    
    for j in G1.nodelist:
        if(j.name==X.name):
            subset=list(set(subset)|set([X]))
            for i in j.nodein:
                i.nodeout = list(set(i.nodeout) - set([j]))
            j.nodein=[]
    
    for j in G1.nodelist:
        if(j.name in Wname):
            subset=list(set(subset)|set([j]))
            ancW=G1.ancestor(j)
            ancestor=list(set(ancestor)|set(ancW))
            
    nodeZ=list(set(G1.nodelist)- set(ancestor))
    
    for z in nodeZ:
        for i in z.nodein:
                i.nodeout = list(set(i.nodeout) - set([z]))
        z.nodein=[]
        
    R=dsep.reachable(G, Z, subset)
    if(Y not in R):
        result.append(R)
        