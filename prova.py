# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:22:34 2019

@author: utente
"""
try:
# Non-existent module
#     import random as randomss
     from classes.Node import Node as node
     from classes.Graph import Graph as graph
     import dsep as dsep
     import back_door as bk
     import front_door
     import docalculus
     import plot
except ImportError:
    print('Module not found')

#formo una matrice d'adiacenza random
#Inserisco -1 nella posizione (x,y) se non vi è alcun nodo tra x e y
#matrixAdj=[]
#for i in range(6):
#    tmp=[]
#    
#    for j in range(6):
#        c=random.randint(1, 10)
#        if(i==j):
#            tmp.append(-1)
#        else:
#            p=c/(j+1)
#            if(p>(1.5)):
#                tmp.append(j)
#            else:
#                tmp.append(-1)
#                
#    matrixAdj.append(tmp)
    
X=node('x')
Y=node('y')
Z1=node('z1')
Z2=node('z2')
Z3=node('z3')
Z4=node('z4')
Z5=node('z5')
Z6=node('z6')

X.set_nodein([Z2, Z1])
Z2.set_nodein([Z3])
Z1.set_nodein([Z3, Z4])
Z5.set_nodein([Z4])
Z6.set_nodein([X])
Y.set_nodein([Z1, Z6, Z5])

X.set_nodeout([Z6])
Z2.set_nodeout([X])
Z3.set_nodeout([Z2, Z1])
Z1.set_nodeout([X,Y])
Z6.set_nodeout([Y])
Z4.set_nodeout([Z1,Z5])
Z5.set_nodeout([Y])

nodeList=[X ,Y ,Z1 ,Z2 ,Z3 ,Z4 ,Z5 ,Z6]
G=graph('G', nodeList)
#L=G.allPath(X, Y)
#plot.allPathPlot(G, X, Y)
#R=G.reachable(X, [Z1])
#L=G.descendant([Z3])
#K=G.backDoor(X, Y)
#K=G.findReachableNodes(X, [Z1, Z2])
#R=dsep.reachable(G, X, [Z1,Z2])
# K=bk.backdoor(G, Z5, [], Y)
# L=bk.backdoor2(G, Z6, Y)

# rl1=docalculus.rule1(G, X, Y, [Z1])
fk=front_door.frontdoor(G, X, [Z6], Y, PlotAll=True)
#for n in G.nodeList:
#    for m in n.nodeout:
#        a = G.reachable(n, [m])
#        if(len(a) > 0):
#            print("The causal effect of "+n.name+" on "+m.name+" is identifiable controlling for:\n")
#            print(a.name)
#G.checkPath(X, Y, [Z1, Z6])
#G.algorithmOne([Z1, Z6],[])
# =============================================================================
# 
# X=node('x')
# Y=node('y')
# U=node('u')
# S=node('s')
# 
# X.set_nodein([U])
# Y.set_nodein([S, U])
# U.set_nodein([])
# S.set_nodein([X])
# 
# X.set_nodeout([S])
# Y.set_nodeout([])
# U.set_nodeout([X, Y])
# S.set_nodeout([Y])
# 
# nodeList=[X ,Y ,U, S]
# G1=graph('G1', nodeList)
# 
# fk=front_door.frontdoor(G1, X, [S], Y)
# 
# =============================================================================

# C=node('c')
# Y=node('y')
# H=node('h')
# E=node('e')
# W=node('w')


# C.set_nodein([E])
# Y.set_nodein([C, H, W, E])
# H.set_nodein([W])
# E.set_nodein([])
# W.set_nodein([C])



# C.set_nodeout([Y, W])
# Y.set_nodeout([])
# H.set_nodeout([Y])
# E.set_nodeout([C, Y])
# W.set_nodeout([H, Y])

# nodelist=[C, E, H, W, Y]
#G=graph('G', nodeList)
#plot.plotGraph(G)



#d=docalculus.rule2(G, [] ,C, E, Y)

