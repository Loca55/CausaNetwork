# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:12:57 2020

@author: mloca
"""

try:
# Non-existent module
     from classes.Node import Node as node
     from classes.Graph import Graph as graph
     import back_door
     import dsep
     import plot

except ImportError:
    print('Module not found')
"""
Optional parameter:
    PlotAll=True/False;
    PlotDsep=True/False;
    PlotBackDoor=True/False;
"""
def frontdoor(G, X, Z, Y, **Optional_Parameter):
    PlotAll=False
    PlotDsep=False
    PlotBackDoor=False
    
    if (('PlotAll' in Optional_Parameter) 
        and(Optional_Parameter['PlotAll'])==True):
        PlotAll=True
        
    if (('PlotDsep' in Optional_Parameter) 
        and(Optional_Parameter['PlotDsep'])==True):
        PlotDsep=True
        
    if (('PlotBackDoor' in Optional_Parameter) 
        and(Optional_Parameter['PlotBackDoor'])==True):
        PlotBackDoor=True
    
    #Get all direct path between X and Y.
    direct_path=G.BFS(X, Y)
    if direct_path == []:
            return False

        
    #Z intercepts all directed paths from X to Y
    u=[]
    for p in direct_path:
        if(PlotAll):
            plot.plotRGBColor(G, p, Z, ["Direct Path", "Other", "Z"],
                              "Direct Path")
        flag=1
        for z in Z:
            if (z in p):
                flag=0
        if (flag):
           u.append(p) 
        
    if u:
            return False
        
    #There is no unblocked path from X to Z
    flag=True
    for z in Z:
        #R = back_door.backdoor(G, X, [], z)
        if (PlotBackDoor or PlotAll):
            R = back_door.backdoor(G, X, [], z, Plot=True)
            #plot.allPathPlot(G, X, Z)
        else:
             R = back_door.backdoor(G, X, [], z, Plot=False)
            #plot.plotRGBColor(G, R, [])
        #reachable = (z not in R)
        flag = flag and R
        
        
    if not(flag):
        return False
    
    #All back-door paths from Z to Y are blocked by X
    flag=True
    for z in Z:
        if (PlotBackDoor or PlotAll):
            bk=back_door.backdoor(G, z, [X], Y, Plot=True)
        else:
            bk=back_door.backdoor(G, z, [X], Y, Plot=False)
        flag= flag and bk
    
    if not(flag):
        return False
    
    return True
    