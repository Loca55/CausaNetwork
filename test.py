# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:22:34 2019

@author: mloca
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
#Define the node in the Graph

X=node('x')
Y=node('y')
Z1=node('z1')
Z2=node('z2')
Z3=node('z3')
Z4=node('z4')
Z5=node('z5')
Z6=node('z6')

#Define the node out for each node
nodeout={X:[Z6],
     Z2:[X],
     Z3:[Z2, Z1],
     Z1:[X, Y],
     Z4:[Z1, Z5],
     Z6:[Y],
     Z5:[Y], 
     Y:[]}
#Define, for each node, the position in the plot 
#For example the node x will be in (0,0) position
position={'x':[0,0],
         'y':[2,0],
         'z1':[1,1],
         'z2':[0,1],
         'z3':[0,2],
         'z4':[2,2],
         'z5':[2,1], 
         'z6':[1,0]}
#Draw up the list of node and define the graph
nodeList=[X ,Y ,Z1 ,Z2 ,Z3 ,Z4 ,Z5 ,Z6]
G=graph('G', nodeList, DAG=nodeout, pos=position)
#Plot the graph
plot.plotGraph(G)
#Plot all possible path between two node
plot.allPathPlot(G, X, Y)
#Define if between two variable there are backdoor path
BackDoor=bk.backdoor(G, X, [Z1, Z2], Y, Plot=True)
#Define if between two variable there are frontdoor path
FrontDoor=front_door.frontdoor(G, X, [Z6], Y, PlotAll=True)
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
#
# 
# =============================================================================

# C=node('c')
# Y=node('y')
# H=node('h')
# E=node('e')
# W=node('w')


# nodeout={C:[Y,W],
#          Y:[],
#          H:[Y],
#          E:[C,Y],
#          W:[H,Y]}

#nodeList=[C, Y, H, E, W]
#G=graph('G2', nodeList, DAG=nodeout)

