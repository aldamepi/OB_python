#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:29:51 2023

@author: albertomengual


EJERCICIO 5 OPENBOOTCAMP PYTHON


Escribe una función que pueda decirte si un año (numero entero) es bisiesto o no.


Voy a intentar hacerlo con clases


Requisitos de año bisiesto:
    Cualquier año divisible por 4 es un año bisiesto.
    Un año divisible por 100 sólo es bisiesto si es divisible por 400.
    Es decir, 1700, 1800,1900, 2100... no son bisiestos



"""




class mariano:
    """ Esta clase determina sí un año es bisiesto """
    
    def __init__(self, annus):
        self.annus = annus
        
    def check(self):
        x = self.annus
        
        if x%4 == 0:
            if x%100 == 0 and x%400 == 0:
                return True
            elif x%100 == 0:
                return False
            else:
                return True
        else:
            return False



a = 2024
# b = mariano(a)
# b.check()

print(mariano(a).check())


























































































