# -*- coding: utf-8 -*-
"""
Created on Tue Sept 20 11:50:20 2022
@author: Oscar Lesmes
"""
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

##FUNCIONES AUXILIARES##
def accionMatrizVector(matriz, vector):
    vector_resultante = []
    for i in range(len(vector)):
        vector_resultante.append(0)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            vector_resultante[i] += matriz[i][j]*vector[j]
    return vector_resultante

def accionMatrizVectorCompleja(matriz,vector):
    res = []
    for i in range(len(matriz)):
        x = matriz[i]
        for j in range(len(x)):
            y = (multiplicacionComplejos(mattriz[i],vector))
        res.append(y)
    return res

def sumaComplejos(numero1, numero2):
    res = ()
    sumaReal = numero1[0] + numero2[0]
    sumaImaginaria = numero1[1] + numero2[1]
    res = (sumaReal, sumaImaginaria)
    return (res)

def multiplicacionComplejos(numero1, numero2):
    res = ()
    res = ((numero1[0]*numero2[0])-(numero1[1]*numero2[1]), (numero1[0]*numero2[1])+(numero2[0]*numero1[1]))
    return (res)

def traspuestaMatriz(matriz):
    objeto = " "
    for i in range(len(matriz)):
        for k in range(i,len(matriz)):
            objeto = matriz[k][i]
            matriz[k][i] = matriz[i][k]
            matriz[i][k] = objeto
    return matriz

def moduloComplejo(vector):
    suma = []
    modulo = [(0,0)]
    for i in range(len(vector)):
        if type(vector[i]) == tuple:
            suma.append(multiplicacionComplejos(vector[i],vector[i]))
    for j in range(len(suma)):
        if suma[j] == tuple:
            modulo[0] = sumaComplejos(modulo[0], suma[j])
    return modulo

def divisionComplejos(numero1, numero2):
    res = ()
    denominador = (numero2[0]**2) + (numero2[1]**2)
    numeradorReal = (numero1[0]*numero2[0]) + (numero1[1]*numero2[1])
    numeradorImaginario = (numero2[0]*numero1[1]) - (numero1[0]*numero2[1])
    res = (round((numeradorReal/denominador), 3), round((numeradorImaginario/denominador), 3))
    return (res)

def normalizarVector(vector):
    modulo = moduloComplejo(vector)
    res = []
    for k in range(len(vec)):
        if vec[k]==tuple:
            resp.append(divisionComplejos(vec[k],modulo[0]))
        elif vec[k]==int:
            resp.append(divisionComplejos((k,0),modulo[0]))
    return res
####################################

#Funcion 1
def clicks(matriz, estado, cantidadClicks):
    for i in range(cantidadClicks):
        estado_nuevo = accionMatrizVector(matriz, estado)
    return estado_nuevo

#matriz= [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
#vector= [6,2,1,5,3,10]
#cantidadClicks = 1
#print(clicks(matriz,vector,cantidadClicks))

#Funcion 2
def multiplesRendijas(matriz, estado):
    matriz_transpuesta = traspuestaMatriz(matriz)
    print(matriz_transpuesta)
    for i in range(len(matriz_transpuesta)):
        if sum(matriz_transpuesta[i]) != 1:
            estocastica = False
            break
        else:
            estocastica = True
    if estocastica == True:
        res = list(map(float, clicks(matriz, estado, 1)))
        return res

#matriz = [[1/3,0,0],[1/3,0,1],[1/3,1,0]]
#estado = [1,0,0]
#print(multiplesRendijas(matriz, estado))

#Funcion 3
def clicksCuantico(matriz, estado, cantidadClicks):
    for i in range(cantidadClicks):
        estado_nuevo = accionMatrizComplejaVectorComplejo(matriz, estado)
    return estado_nuevo

def multiplesRendijasCuantico(matriz,estado,clicks):
    matriz_transpuesta = traspuestaMatriz(matriz)
    for i in range(len(matriz)):
        if sum(matriz_transpuesta[i])!=1:
            return False
    for j in range(int(clicks)):
        vectorResultante = accmatvec(matriz, estado)
    return vectorResultante

#matriz = [[(0,1),(0,0)],[(0,0),(0,1)]]
#vector = [(0,1),(0,0)]
#print(multiplesRendijasCuantico(matriz,vector))

#Funcion 4
def graficar(vectorEstado):
    counts = {}
    vectorNormal = []
    if sum(vectorEstado) == 1:
        for i in range(1, len(vectorEstado) + 1):
            x = str(i)
            counts[x] = vectorEstado[i-1]
    elif sum(vectorNormal) > 1 or sum(vectorNormal)<1:
        vectorNormal = normalizarVector(vectorEstado)
        for i in range(1, len(vectorNormal) + 1):
            x = str(i)
            counts[x] = vec[i-1]
    plot_histogram(counts)
    plt.show()
    return

