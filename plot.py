# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:03:00 2020

@author: mloca
"""
try:
# Non-existent module

     import matplotlib.pyplot as plt
     from classes.Graph import Graph as graph
     import networkx as nx
    
except ImportError:
    print('Module not found')


def plotGraph(G):
    Gplot= nx.DiGraph()
        
    edge=[]
    i=0
    label={}
    value=0
    for x in G.nodeList:
        label[x.name]=x.name
        Gplot.add_node(x.name)
        for y in x.nodeout:
            tupla=()
            tupla=(x.name, y.name)
            edge.append(tupla)
        i=i+1
    
    if not(G.pos==[]):
        position=G.pos
    else:
        position=nx.spring_layout(Gplot)
    #Gplot=nx.relabel_nodes(Gplot,mapping )
    Gplot.add_edges_from(edge)
    nx.draw_networkx_nodes(Gplot,
                           position,
                           nodelist=Gplot.nodes(),
                           node_color='b',
                           node_size=520,
                           alpha=0.8)
    nx.draw_networkx_labels(Gplot,position,label,font_size=12)
    nx.draw_networkx_edges(Gplot,position,width=1.0,alpha=0.5)
    #plt.savefig("simple_path.png") # save as png
    plt.title('Graph')
    plt.show()

def allPathPlot(G, X, Y):   
    validPath=[]
    validPath=G.allPath(X, Y)
    #Controllo che i percorsi non abbiano alcun collider  
    for p in validPath:
        Gtmp=graph('Gtmp', p)
        Gplot=nx.DiGraph()
        for x in p:
            Gplot.add_node(x.name, pos=G.pos[x.name])
        #plotGraph(Gtmp)
        i=0
        edge=[]
        while(i<(len(p)-1)):
            if(p[i] in p[i+1].nodeout):
                edge.append((p[i+1].name, p[i].name))
            elif(p[i+1] in p[i].nodeout):
                edge.append((p[i].name, p[i+1].name))
            i=i+1
        Gplot.add_edges_from(edge)
        
        pos=nx.get_node_attributes(Gplot,'pos')
        nx.draw(Gplot,pos, with_labels=True)
        #plt.savefig("simple_path.png") # save as png
        plt.show()
        
def plotRGBColor(G, R, Gr, Label, Title):
    '''
    

    Parameters
    ----------
    G : Graph
        Graph that we want to represent.
    R : List
        List of node that have particular trait (like are reachable or are part of directpath).
    Gr : List
        List of node of node observed
    Label : List
        List of label for red, blue and green node.

    Returns
    -------
    Plot a graph with three node color

    '''
    
    
    Gplot= nx.DiGraph()
    Red=[]
    for r in R:
        Red.append(r.name)
    Green=[]
    for g in Gr:
        Green.append(g.name)
         
    edge=[]
    i=0
    tmp=[]
    labels={}
    value=0
    
    for x in G.nodeList:        
        Gplot.add_node(x.name)
        tmp.append(x.name)
        labels[x.name]=x.name
        for y in x.nodeout:
            tupla=()
            tupla=(x.name, y.name)
            edge.append(tupla)
        i=i+1
    
    #Gplot=nx.relabel_nodes(Gplot,mapping )
        
    Blue=list(set(tmp)-set(Red))
    Blue=list(set(Blue)- set(Green))
    Red=list(set(Red)- set(Green))
    legend=[]
    pos=nx.spring_layout(Gplot) # positions for all nodes
    
    pos={'x':[0,0],
         'y':[2,0],
         'z1':[1,1],
         'z2':[0,1],
         'z3':[0,2],
         'z4':[2,2],
         'z5':[2,1], 
         'z6':[1,0]}
    
    Gplot.add_edges_from(edge)
    nx.draw_networkx_nodes(Gplot,pos, nodelist=Red,
                           node_color='r',
                           node_size=520,
                           alpha=0.8,
                           label=Label[0])
    nx.draw_networkx_nodes(Gplot,pos,
                           nodelist=Blue,
                           node_color='b',
                           node_size=520,
                           alpha=0.8,
                           label=Label[1])
    nx.draw_networkx_nodes(Gplot,pos,
                           nodelist=Green,
                           node_color='G',
                           node_size=520,
                           alpha=0.8,
                           label=Label[2])
    
    nx.draw_networkx_labels(Gplot,pos,labels,font_size=12)
    nx.draw_networkx_edges(Gplot,pos,width=1.0,alpha=0.5)
    plt.legend(numpoints = 1)
    plt.title(Title)
    plt.show()