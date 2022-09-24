# Libreria #3 Salto a lo cuantico:

_En esta libreria encontraremos una serie de funciones que nos permiten realizar operaciones para determinar estados cuanticos, así mismo para obtener la gráfica de las probabilidades:_
1. Calcular la cantidad de "clicks" de las canicas.
2. Calcular la propabilidad de estado con una matriz de números reales.
3. Calcular la propabilidad de estado con una matriz de números complejos.
4. Gráfica de probabilidad.

### Pre-requisitos
_Para poder correr nuestra libreria necesitaremos un iDLE cualquiera de python._\
_Para poder obtener un resultado exitoso debemos tener la libreria de matplotlib y qiskit instalados en python, de lo contrario no podremos ejecutar satisfactoriamente nuestras funciones._ \
_A continuación, vamos a observar las funciones auxiliares que nos permitiran realizar calculos de manera más sencilla:_
```
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
```
### Ejemplos
_A continuación encontraremos el ejemplo de la función donde se oberva la probabilidad de que una canica se encuentre en uno u otro estado dependiendo la cantidad de "clicks":_
```
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
```
_¿Cómo podemos verificar estos resultados?_\
_Para poder verificar estos resultados debemos transponer nuestra matriz y verificar si la misma es estocastica:_
```
for i in range(len(matriz_transpuesta)):
        if sum(matriz_transpuesta[i]) != 1:
            estocastica = False
            break
        else:
            estocastica = True
```
_En caso de que nuestra verificación sea True (```estocastica = True```), vamos a crear una lista con elementos de tipo ```float``` que hace el llamado a la función de clicks.
```
    if estocastica == True:
        res = list(map(float, clicks(matriz, estado, 1)))
        return res
```
### Pruebas en codigo
_Al finalizar cada función encontraremos su respectiva prueba con comentario (```#matriz = [[1/3,0,0],[1/3,0,1],[1/3,1,0]]
#estado = [1,0,0]
#print(multiplesRendijas(matriz, estado))```), para poder probar cada una debemos quitar sus respectivos comentarios.

## ¿Como lo construimos?
* [Pycharm](https://www.jetbrains.com/es-es/pycharm/) -_El iDLE usado_

## Autor
* **Oscar Lesmes** - *Libreria completa* - [GitHub](https://github.com/villanuevand)

