import random
import numpy as np
import pandas as pd
import funciones


class tablero:
    """
    Clase tablero 
    Atributos:
        tamaño (tupla): tamaño del tablero  
        barcos (dict): los barcos empleados en el juego  
    """
    
    tamaño = (10,10)
    barcos = barcos = {
    'barco1_1' : {
        'cantidad' : 1,
        'vidas' : 1},
    'barco1_2' : {
        'cantidad' : 1,
        'vidas' : 1},
    'barco1_3' : {
        'cantidad' : 1,
        'vidas' : 1},
    'barco1_4' : {
        'cantidad' : 1,
        'vidas' : 1},
    'barco2_1' : {
        'cantidad' : 1,
        'vidas' : 2},
    'barco2_2' : {
        'cantidad' : 1,
        'vidas' : 2},
    'barco2_3' : {
        'cantidad' : 1,
        'vidas' : 2},
    'barco3_1' : {
        'cantidad' : 1,
        'vidas' : 3},
    'barco3_2' : {
        'cantidad' : 1,
        'vidas' : 3},
    'barco4_1' : {
        'cantidad' : 1,
        'vidas' : 4}}
    


    def __init__(self):

        """
        Args:
            barcos (dict): coloca los barcos
            
        """
        tablero = pd.DataFrame(np.full((10,10), ' '))
        barco1_1 = colocar_barco(barcos['barco1_1']['vidas']-1)
        barco1_2 = colocar_barco(barcos['barco1_2']['vidas']-1)
        barco1_3 = colocar_barco(barcos['barco1_3']['vidas']-1)
        barco1_4 = colocar_barco(barcos['barco1_4']['vidas']-1)

        barco2_1 = colocar_barco(barcos['barco2_1']['vidas']-1)
        barco2_2 = colocar_barco(barcos['barco2_2']['vidas']-1)
        barco2_3 = colocar_barco(barcos['barco2_3']['vidas']-1)

        barco3_1 = colocar_barco(barcos['barco3_1']['vidas']-1)
        barco3_2 = colocar_barco(barcos['barco3_2']['vidas']-1)

        barco4_1 = colocar_barco(barcos['barco4_1']['vidas']-1)
                

        
        

