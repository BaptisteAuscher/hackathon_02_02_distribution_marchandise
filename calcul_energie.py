
import numpy as np
import osmnx as ox
graphe1 = [[2.339874, 48.845587], [2.339191, 48.84431], [2.338983, 48.843925], [2.338668, 48.843363], [2.3382, 48.842505], [2.337756, 48.841755], [2.337467, 48.841247], [2.337256, 48.840875], [2.336833, 48.840525], [2.336725, 48.840429], [2.33667, 48.840368], [2.336618, 48.840296], [2.336599, 48.840254], [2.33659, 48.840219], [2.336582, 48.84018], [2.336576, 48.840137], [2.336576, 48.840066], [2.336554, 48.839769], [2.336657, 48.839671], [2.33666, 48.839333], [2.336634, 48.838883], [2.33662, 48.83862], [2.336478, 48.838523], [2.336382, 48.838455], [2.336305, 48.838394], [2.335676, 48.837758], [2.335587, 48.837667], [2.33543, 48.837511], [2.334876, 48.836939], [2.33464, 48.836704], [2.334476, 48.836536], [2.334315, 48.836373], [2.33417, 48.836228], [2.334056, 48.836117], [2.333502, 48.835546], [2.333243, 48.835247], [2.333061, 48.835037], [2.332998, 48.834961], [2.332886, 48.834828], [2.332765, 48.8347], [2.332617, 48.834545], [2.33252, 48.834532], [2.332448, 48.834511], [2.332403, 48.834485], [2.332353, 48.834443], [2.332307, 48.834391], [2.332287, 48.834323], [2.33229, 48.834275], [2.332312, 48.834233], [2.332355, 48.83419], [2.332507, 48.834221], [2.33256, 48.83424], [2.332617, 48.834267], [2.332674, 48.834299], [2.332716, 48.834336], [2.332768, 48.834413], [2.332747, 48.834461], [2.332718, 48.834494], [2.332676, 48.834523], [2.332617, 48.834545], [2.332765, 48.8347], [2.332886, 48.834828], [2.332998, 48.834961], [2.333061, 48.835037], [2.333243, 48.835247], [2.333502, 48.835546], [2.334056, 48.836117], [2.33417, 48.836228], [2.334315, 48.836373], [2.334476, 48.836536], [2.33464, 48.836704], [2.334876, 48.836939], [2.33543, 48.837511], [2.335587, 48.837667], [2.335703, 48.837625], [2.33652, 48.837324]]
graphe = [[]]
#Nous avons fait le choix d'établir notre propore modèle pour calcuelr les perrtes énergétiques lors du déplacement du camion.
#Nous commençons par définir l'acceleration du camion et sa masse initiale. Un point imporant de notre modèle est l'hypothèse
# de constance de l'accélération.

a=6
m0 = 18000

#Nous modélisons le fait qu'a chaque livraisons, le camion perd de la masse (il décharge sa marchandise, il consomme du carburant, ...)

m=[]
for i in len(graphe):
    m[i]=m0-i*50

# On commence par la perte d'énergie par frottements fluides avec l'air. O  suppose une vitesse fiable donc un modèle de frottement 
# selon un loi de Stocks ( linéaire par raport à la vitesse). Pour trouver la vitesse, on utilise la vitesse moyenne des vehicule dans la 
# zone concernée ( vitesse extraite de la base de donée fournie).


def energie_aero(graphe):
    E=[]
    v=[]
    for i in len(graphe): 
        v[i]= (graphe[i][0])/(graphe[i][1])
        E[i]= 0.5*1.25*0.69*(v[i])**2*0.33*graphe[i][0]
    return (np.array(E))

#Maintenant, on calcul l'énergie dissipée par frottement solide avec le sol

def energie_frotsol(graphe):
    E=[]
    for i in len(graphe):
         return(3*m[i]*9.8*graphe[i][0])
    return (np.array(E))

# Enfin, on calcul l'énergie nécessaire pour accélérer le cmaion. On se place dans un cas simple : on considère une distance nécéssaire pour accélérer
# selon la formule : l_acc = v_moy * v_finale / a   où a est l'accélération que l'on a pris à 0,6g supposée constante en cas d'accélération, 
# et on a prit v_moy = 15 km/h et v_finale = 30 km/h.
# On se place ensuite dans le cas d'une variation classique d'énergie cinétique


def energie_acceleration(graphe):
    E=[]
    l_acc = 30*15/a
    for i in len(graphe): 
        if graphe[i][0] <= 2*l_acc:
            vf=(30*graphe[i][0])/2*l_acc
            E[i]=0.5*m[i]*vf**2
        else :
            E[i]=0.5*m[i]*30**2
    return (np.array(E))

#Il nous reste mainetant qu'a sommer les différentes contributions énergétiques

def energie_totale(graphe): 
   
    E_tot=0.30*(energie_aero(graphe)+energie_frotsol(graphe)+energie_acceleration(graphe))
    res=0
    for i in range (len(E_tot)): 
        res+=E_tot[i]
    return (res)




