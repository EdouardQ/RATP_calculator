# -*- coding: utf-8 -*-

############ Import & Path ############

import os
from collections import OrderedDict
path=os.chdir("./data/")

############ Fonctions fichiers ############
    
def listeMetroCsv(Fname):
    """
    Fonction qui lit un fichier .csv et qui en extrait le nom de la station,
    sa ligne et sa place sur cette dernière.
    """
    F = open(Fname)
    L1, L2, L3 = [], [], []
    for l in F.readlines()[1:]: # on exclue la première ligne
        ptdata = l.split(sep=';')
        i=0
        for ptd in ptdata :
            ptdata[i] = str(ptd)
            i+=1
        L1.append(ptdata)
    
    for var in L1:
        for i in range (0,3):
            L2.append(var[i])
        L3.append(L2)
        L2=[]
    
    F.close()
    return L3
    
def listeMetroCsvStation(Fname):
    """
    Fonction qui lit un fichier .csv et qui en extrait le nom des stations.
    """
    F = open(Fname)
    L1, L2, L3 = [], [], []
    for l in F.readlines()[1:]: # on exclue la première ligne
        ptdata = l.split(sep=';')
        i=0
        for ptd in ptdata :
            ptdata[i] = str(ptd)
            i+=1
        L1.append(ptdata)
    
    for var in L1:
            L2.append(var[1])
    
    F.close()
    return L2

def dictMetroCsv(l):
    """
    Fonction qui retourne un dictionnaire des stations triées par ligne.
    """
    registre=dict()
    temp=dict()
    l1,l2,l3,l3b,l4,l5,l6,l7,l7b,l8,l9,l10,l11,l12,l13,l14=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    
    for var in l:
        if var[0]=="M1":
            l1.append(var[1])
        if var[0]=="M2":
            l2.append(var[1])
        if var[0]=="M3":
            l3.append(var[1])
        if var[0]=="M3b":
            l3b.append(var[1])
        if var[0]=="M4":
            l4.append(var[1])
        if var[0]=="M5":
            l5.append(var[1])
        if var[0]=="M6":
            l6.append(var[1])
        if var[0]=="M7":
            l7.append(var[1])
        if var[0]=="M7b":
            l7b.append(var[1])
        if var[0]=="M8":
            l8.append(var[1])
        if var[0]=="M9":
            l9.append(var[1])
        if var[0]=="M10":
            l10.append(var[1])
        if var[0]=="M11":
            l11.append(var[1])
        if var[0]=="M12":
            l12.append(var[1])
        if var[0]=="M13":
            l13.append(var[1])
        if var[0]=="M14":
            l14.append(var[1])
    temp["M1"]=l1
    temp["M2"]=l2
    temp["M3"]=l3
    temp["M3b"]=l3b
    temp["M4"]=l4
    temp["M5"]=l5
    temp["M6"]=l6
    temp["M7"]=l7
    temp["M7b"]=l7b
    temp["M8"]=l8
    temp["M9"]=l9
    temp["M10"]=l10
    temp["M11"]=l11
    temp["M12"]=l12
    temp["M13"]=l13
    temp["M14"]=l14
    
    registre = OrderedDict(sorted(temp.items(), key=lambda t: t[0]))

    return registre      

#print(listeMetroCsv("liste stations.csv"))
#print(listeMetroCsvStation("liste stations exceptions-fourche2.csv"))        
#print(os.listdir(path))
#print(dictMetroCsv(listeMetroCsv("liste stations.csv")))