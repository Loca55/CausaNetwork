# CausalDataScience

This repo contain a three-year thesis work. We can find an implementation of algorithm for d-separation, back-door and front-door. do-calculus algorithm isn't complete.
The aim of this work is provide who approaching to *causal networks*  with a tool that could help to figure out what are the nodes d-separeted, the back-door or front-door path between two nodes.

A test implementation can be found below. 

```Python

from classes.Node import Node as node
from classes.Graph import Graph as graph
import dsep as dsep
import back_door as bk
import front_door
import plot

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
```
