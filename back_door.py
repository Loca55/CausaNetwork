# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:37:40 2020

@author: utente
"""
try:
# Non-existent module
     from classes.Node import Node as node
     from classes.Graph import Graph as graph
     import dsep 
     import itertools
     import plot
except ImportError:
    print('Module not found')

#definisco la funzione back_door(x,y,z,G)
#G=(V,E) è un grafo identificata da una matrice d'adiacenza
#z identifica l'insieme di nodi condizionanti
#y identifica il nodo effetto
#x identifica il nodo causa
#x,y,z(appartengono)G
#la funzione verifica se esiste un percorso non bloccato tra x e y
#un percorso si definisce bloccato se si verifica una delle seguenti condizioni:
#   1)il percorso contiente una catena o una fork e il nodo centrale della
#   catena o della fork fa parte di z
#   2) il percorso contiente un collider e il nodo centrale del collider non fa
#   parte di 
#ritorna 1 se il percorso non è bloccato 
#ritorna 0 se il percorso è bloccato
def backdoor(G, X, Z, Y, **OptionalPlot):
    PlotBackDoor=False
    if (('Plot' in OptionalPlot) 
        and(OptionalPlot['Plot'])==True):
        PlotBackDoor=True
        plot.allPathPlot(G, X, Y)
        
    D = G.descendant([X])
    tmp=X.nodeout
    for m in tmp:
        m.nodein=list(set(m.nodein) - set([X]))
    X.nodeout=[]
    
    if (PlotBackDoor): 
        R=dsep.reachable(G, X, Z, Plot=True)
    else:
        R=dsep.reachable(G, X, Z, Plot=False)
        
    reachable=(Y not in R)
    X.nodeout=tmp
    for m in tmp:
        m.nodein=list(set(m.nodein)|set([X]))

    desc=True
    for z in Z:
        if z in D:
            desc=False
    
    if (PlotBackDoor):
        direct=G.BFS(X,Y)
        for d in direct:  
            R=list(set(R)|set(d))
        plot.plotRGBColor(G,R , Z)
    
    result= reachable and desc
    return result

def backdoor2(G, X, Y):
        L=[]
        L1=[]
        for i in range(len(G.nodeList)):
            for subset in itertools.combinations(G.nodeList, i):
                subset=list(subset)
                M=[]
                for y in subset:
                    M.append(y.name)
                if (X not in subset):
                    R=backdoor(G, X, subset, Y)
                    # R=(Y not in R)
                    flag=True
                    J=G.descendant([X])
                    for j in J:
                        if (j in subset):
                            flag=False                     
                    if (R and flag):
                        L.append(subset)
                        L1.append(M)
        return L1
        