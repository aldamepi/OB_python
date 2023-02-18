#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:02:27 2023

@author: albertomengual


EJERCICIO 6-1 OPENBOOTCAMP PYTHON 


a. Crea la clase vehiculo con los siguientes atributos:
    - color
    - ruedas
    - puertas
    
b. Crea la clase coche que heredará de vehiculo con los siguientes atributos:
    - velocidad
    - cilindrada

c. Crea un objeto de la clase coche y muestralo por consola


"""




class vehiculo:
    """ Esta clase define un vehiculo generico. Es una clase base. """
    
    color = None
    ruedas = 4
    puertas = 5
    

class coche(vehiculo):
    """ Esta clase define un coche. Hereda de vehiculo """
    
    velocidad = 120
    cilindrada = 0
    

# Crear objeto
c = coche()
c.color = "Negro"
c.velocidad = 180
c.cilindrada = 1.6

# print(c.__dict__)


# Visualizar atributos
for attr in dir(c):
    if not attr.startswith("_"):
        print("c.%s = %r" % (attr, getattr(c, attr)))










































































