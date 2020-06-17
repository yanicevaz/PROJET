from Calcul_Fp import *

def dicho(FP,list):
    zga = -5
    zgb = 0
    epsilon = 0.0001
    zgmactuel = 0
    while True:
        acienzgm = zgmactuel
        zgmactuel = 0.5 * (zga+zgb)
        resultat,list = CalculPousseeArchimede(list,zgmactuel - acienzgm)
        phi = resultat - FP
        if abs(phi) < epsilon:
            return zga
        elif phi >= 0:
            zga = zgmactuel
        else:
            zgb = zgmactuel
