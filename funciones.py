import numpy as np
import pandas as pd
import random



def espacio_barco(c1,c2,orientacion,eslora):
    if orientacion == 'h':
        espacio_barco = tablero.loc[c1-1:c1+1, c2-1:c2-1+eslora+2] 
    if orientacion == 'v':
        espacio_barco = tablero.loc[c1-1:c1+eslora+1,c2-1:c2+1]
    return espacio_barco



def colocar_barco(eslora):
    lista_barcos = []
    sigo = True
    while sigo:
        sigo = False
        c1 = np.random.randint(0,10)
        c2 = np.random.randint(0,10)
        orientacion = np.random.choice(['h', 'v'])

        if orientacion == 'h' and ((c2+eslora)<10):
            
            if np.any(espacio_barco(c1,c2,orientacion,eslora) == 'O'):
                sigo = True
            else:
                self.tablero.loc[c1, c2:c2+eslora] = 'O'
                barco = [(c1+eslora,c2),(c1,c2)]
                lista_barcos.append(barco)

        elif orientacion == 'v' and ((c1+eslora)<10):
            
            if np.any(espacio_barco(c1,c2,orientacion,eslora) == 'O'):
                sigo = True
            else: 
                self.tablero.loc[c1:c1+eslora, c2] = 'O'
                barco = [(c1,c2),(c1+eslora,c2)]
                lista_barcos.append(barco)
 
        else:
            sigo = True
    return lista_barcos