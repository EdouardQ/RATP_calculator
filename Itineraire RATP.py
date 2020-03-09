# -*- coding: utf-8 -*-

########## Import ###########

from LibMetroIti import *
from tkinter import *

########### MAIN ############

programme = Tk()
programme.title("Itinéraires RATP")
programme.geometry("1000x300")

############################

L=listeMetroCsv("liste stations.csv")

lignes = []
for varLd in dictMetroCsv(L):
    lignes.append(varLd)
    
############################

filename = PhotoImage(file = ".\\logo-ratp.png")
Label(programme, image=filename).place(x=0, y=0, relwidth=1, relheight=1)

############################

varCalc = StringVar(programme)
varCalc.set("")

def Calc(*arg):
    varCalc.set(itineraire(varSd.get(),varLd.get(),varSa.get(),varLa.get(),timeH.get()+timeM.get()*0.01666))

############################

varSd = StringVar(programme)
varSd.set("Choississez la station")

varSa = StringVar(programme)
varSa.set("Choississez la station")

def AffichageDepart(*arg):
   w1 = OptionMenu(programme, varSd, *dictMetroCsv(L)[varLd.get()], command=Calc)
   w1.grid(column=1, row=3)

def AffichageArrive(*arg):
   w3 = OptionMenu(programme, varSa, *dictMetroCsv(L)[varLa.get()], command=Calc)
   w3.grid(column=1, row=5)
        
############################ 
   
varLd = StringVar(programme)
varLd.set("Choississez la ligne")

varLa = StringVar(programme)
varLa.set("Choississez la ligne")

w = OptionMenu(programme, varLd, *lignes, command=AffichageDepart)
w.grid(column=1, row=2)

w2 = OptionMenu(programme, varLa, *lignes, command=AffichageArrive)
w2.grid(column=1, row=4)

############################

heures, minutes = [], []

for n in range(0,60):
    if n<24:
        heures.append(n)
    if n%5==0:
        minutes.append(n)

############################

timeH = IntVar(programme)
timeM = IntVar(programme)


w4 = OptionMenu(programme, timeH, *heures, command=Calc)
w4.grid(column=3, row=2)

w5 = OptionMenu(programme, timeM, *minutes, command=Calc)
w5.grid(column=4, row=2)

############################

Label(programme, text="Itinéraire du réseau de métro RATP").grid(column=1, row=1)
Label(programme, text="\t|\tHeure de départ").grid(column=3, row=1)
Label(programme, textvariable=varCalc).grid(column=5, row=1)
            
programme.mainloop()