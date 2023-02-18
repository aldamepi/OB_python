#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 21:05:35 2023

@author: albertomengual


EJERCICIO 6-2 OPENBOOTCAMP PYTHON


Definición del programa

a. Crear clase llamada alumno con los atributos:
    - nombre
    - nota

b. Definir métodos:
    - inicializar atributos
    - imprimirlos
    - mostrar mensaje con la nota y si ha aprobado o no.


"""



class alumno:
    """ Esta clase define un alumno y sus metodos """
    
    def __init__(self):
        self.nombre = input("Introducir el nombre del alumno:\n")
        self.nota = float(input("Introducir la nota del alumno:\n"))
        
    def atributos(self):
        print(self.__dict__)
    
    def resultado(self):
        if self.nota >= 5:
            print("El alumno %s ha aprobado con la nota: %s" %(self.nombre, self.nota))
        else:
            print("El alumno %s ha suspendido con la nota: %s" %(self.nombre, self.nota))


a = alumno()
a.atributos()
a.resultado()

























































































