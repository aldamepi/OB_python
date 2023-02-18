#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 15:20:49 2023

@author: albertomengual


EJERCICIO 4 OPENBOOTCAMP PYTHON

Escribe un programa que muestre los números del 1 al 100 en orden inverso


Voy a intentar complicarlo con iteradores y generadores + clases OMG

"""


# # ERROR
# print(range(100,0,-1))


# # Solución más simple
# for x in range(100,0,-1):
#     print(x, sep=("\n"))



# # Asignando el rango
# r = range(100,0,-1)
# # next(r) #-->TypeError: 'range' object is not an iterator
# for x in r:
#     print(x, sep=("\n"))


# # Asignando iterador
# r = iter(range(100,0,-1)) # <range_iterator at 0x7fda78cee4b0>
# # next(r)
# for x in r:
#     print(x, sep=("\n"))


# # Prueba iterador con strings
# s = "abc"
# it = iter(s) # <str_iterator at 0x7fda78f9e070>
# it
# next(it)



# # SOLUCION CON CLASES Y GENERADORES HAS-A 1
# class gen:
#     """ Esta clase crea un generador inverso """
    
#     def __init__(self, n):
#         self.entero = n
        
#     def gen_inv(self):
#         for x in range(self.entero,0,-1):
#             yield x

    
# class imprime:
#     """ Esta clase imprime un generador"""
    
#     def __init__(self,gen_obj):
#         # self.n = n
#         self.gen_obj = gen_obj
       
#     def imp_inv(self):
#         for x in self.gen_obj.gen_inv():
#             print(x)
 
# g = gen(100)
# i = imprime(g)
# i.imp_inv()




# SOLUCION CON CLASES Y GENERADORES HAS-A 2
class gen:
    """ Esta clase crea un generador inverso """
    
    def __init__(self, n):
        self.entero = n
        
    def gen_inv(self):
        for x in range(self.entero,0,-1):
            yield x

    
class imprime:
    """ Esta clase imprime un generador"""

    def __init__(self,n):
        self.n = n
    
    def imp_inv(self):
        g = gen(self.n)
        gi = g.gen_inv()
        for x in gi:
            print(x)
 

i = imprime(100)
i.imp_inv()






















































































