# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:32:05 2020

@author: mloca
"""
try:
# Non-existent module
#     from classes.Node import Node as node
     import plot
     import copy
except ImportError:
    print('Module not found')




def reachable(G, X, Z, **OptionalPlot):
    """
    G => rete causale
    X => nodo sorgente
    Z => lista di nodi condizionanti
    """
    A = reachablePhaseOne(G, X, Z)
    R = reachablePhaseTwo(G, X, Z, A)
    
    if (('Plot' in OptionalPlot) 
        and(OptionalPlot['Plot'])==True):
        plot.plotRGBColor(G, R, Z, ["Reachable", "Not reachable", "Observed"],
                          "Reachable Graph of "+ X.name)
    
    return R
    
    
def reachablePhaseOne(G, X, Z):
    """
    G => rete causale
    X => nodo sorgente
    Z => lista di nodi condizionanti
    """
    
    # Fase 1: inserire tutti gli antenati di Z in A
    
    L = copy.deepcopy(Z)	# nodi da visitare
    A = []					# antenati di Z
    ZTmp=[]
    for z in Z:
        ZTmp.append(z.name)
    
    while ( len(L) != 0 ):
        #Selezioniamo un nodo Y da L
        Y = L.pop(0)
        if (Y not in A):
            #Unisco la lista dei nodi da visitare con i genitori di Y
            L = list(set(L)|set(Y.nodein))
        #Y è evidentemente un antenato
        
        if (Y.name in ZTmp):
            A=list(set(A)|set(Z))
        else:
            A=list(set(A)|set([Y]))
        
    return A
    
def reachablePhaseTwo(G, X, Z, A):
    """
    G => rete causale
    X => nodo sorgente
    Z => lista di nodi condizionanti
    A => antenati di Z
    """
    
    #Fase 2: attraversa percorsi attivi a partire da X
    #Direzione: 
    #   0 indica l'attraversamento in direzione foglia-radice
    #   1 indica l'attraversamento in direzione radice-foglia
    
    L = [(X, 0)]	# (nodo, direzione) da visitare
    V = []          # (nodo, direzione) già visitati
    R = []          # nodi raggiungibile da percorsi attivi
    while (len(L) != 0):
        #Selezioniamo un nodo Y e la sua direzione d da L
        (Y, d) = L.pop(0)
        if ((Y, d) not in V):
            if(Y not in Z):
            # Y è raggiungibile
                R = list(set(R) | set([Y]))
            V = list(set(V) | set([(Y, d)]))	# Segniamo (Y,d) come visitati
            # Percorso attraverso Y è attivo se Y non è in Z
            if ((d==0) and (Y not in Z)):
                for y in Y.nodein:
                    #I genitori di Y saranno visitati dal basso
                    L = list(set(L) | set([(y,0)]))	
                for y in Y.nodeout:
                    #I figli di Y saranno visitati dall'alto
                    L = list(set(L) | set([(y,1)]))
            # Scendi attraverso Y  
            elif (d==1):
                if Y not in Z:
					# Percorsi discendenti verso i figli di Y sono attivi
                    for y in Y.nodeout:
                        # I figli di Y saranno visitati dall'alto
                        L = list(set(L) | set([(y,1)]))
                if Y in A:	
                    # I percorsi della v-structure sono attivi
                    for y in Y.nodein:
                        #I genitori di Y saranno visitati dal basso
                        L = list(set(L) | set([(y,1)]))	
    return R

    