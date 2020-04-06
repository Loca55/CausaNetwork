# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:29:24 2020

@author: mloca
"""

class Node:
    #definisco la classe node nel seguente modo:
    #nome del nodo (name)
    #nodi in entrata(node in)
    #nodi in uscita(node out)
    
    def __init__(self, name):
        self.name=name
        self.nodein=[]
        self.nodeout=[]
    
    def set_nodein(self, nodein):
        self.nodein=nodein
        
    def set_nodeout(self, nodeout):
        self.nodeout=nodeout
        
    
    
   
   
        
            