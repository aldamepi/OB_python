#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:29:51 2023

@author: albertomengual


Escribe un programa que pida al usuario su peso (en Kg) y estatura (en metros),
calcule el índice de masa corporal y lo alamacene en una variable, e imprima
la frase: "Tu índice de masa corporal es..."
El indice de masa corporal redondeado a dos decimales.

Voy a intentar hacerlo usando clases


"""


class indice_masa_corporal:
    """Esta clase sirve para calcular el índice de masa corporal"""
    
    imc = 0
    
    def calculo_imc(self):
        peso = float(input("Por favor introduzca su peso en Kg: \n"))
        estatura = float(input("Por favor intruduzca su estatura en metros: \n"))
        self.imc = peso/(estatura**2)
        
    def imprime_imc(self):
        print("Tu indice de mas corporal es", str(round(self.imc,2)), "Kg/m^2.")
        
        
i = indice_masa_corporal()

i.calculo_imc()

i.imprime_imc()





















































































