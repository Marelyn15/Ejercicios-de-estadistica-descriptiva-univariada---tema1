from collections import Counter
import math
import numpy as np

def tabla_frecuencia(grupo,percentil):
    print("Ejercicios básicos de estadística descriptiva univariada")
    

    #frecuencia absoluta

    # Convierte en diccionario los elementos sin repetición 
    # su valor es el número de veces que se repite
    FA = Counter(grupo)
    #Organizando el diccionario
    FA = dict(sorted(FA.items()))
    print("Esto es la frecuencia absoluta (FA)", FA)

    #Un listado de las marcas de clase
    CI = [] #Clave Individual
    #Valores de la clave individual
    for index, valor in enumerate(FA.keys()):
        CI.insert(index,valor)
    
    #Frecuencia absoluta acumulada
    nuevo_valor = 0
    FAA = []
    for index, valor in enumerate(FA.values()):  #La frecuencia de repetición de las marcas de clase
        nuevo_valor = valor + nuevo_valor
        FAA.insert(index,nuevo_valor)

    FAA = dict(zip(CI,FAA))
    print(f"Frecuencia Absoluta acumulada (FAA) {FAA}")
    total_numeros = max(FAA)


    #frecuencia relativa
    # Desde el diccionario de frecuencia absoluta se toma el numero y su frecuencia 
    # Esto a su vez se divide entre el largo del grupo del inicio
    # Cuando se tiene el resultado se entra en una entrada de diccionario (osea el num)
    FR = {num: round(freq / len(grupo),2) for num, freq in FA.items()} # Numero : frecuencia relativa
    print(f"Esto es la frecuencia relativa (FR) {FR}")

    #Frecuencia relativa acumulada:
    nuevo_valor = 0
    FRA = []
    for index, valor in enumerate(FR.values()):
        nuevo_valor = valor + nuevo_valor
        FRA.insert(index,round(nuevo_valor,2))
    FRA = dict(zip(CI, FRA))
    print(f"Esto es frecuencia relativa acumulada (FRA) {FRA}")

    #Un listado solo de las frecuencias
    VI = [] #Clave Individual
    #Valores de la clave individual
    for index, valor in enumerate(FA.values()):
        VI.insert(index,valor)
    ni = VI
    VI = sum(VI)

    #Intervalo del percentil
    pxn = (VI * percentil) / 100
    print(f"El percentil a {percentil} % es {pxn} que sería más cercano al {math.ceil(pxn)} de la frecuencia absoluta")

    #Xi Ni multiplicacion marca clase y frecuencia
    Xi_Ni = []
    for index, valor in enumerate(CI):
        mult = valor * ni[index]
        Xi_Ni.insert(index,mult)

    print('Puntos medios por frecuencia (Xi ni)', Xi_Ni)

    total_Xi_Ni = sum(Xi_Ni)

    print('Total del Xi ni', total_Xi_Ni)

    #Xi Ni multiplicacion marca clase y frecuencia
    Xi_Ni_2 = []
    for index, valor in enumerate(CI):
        mult = (valor**2) * ni[index]
        Xi_Ni_2.insert(index,mult)

    print('Puntos medios por frecuencia (Xi^ ni)', Xi_Ni_2)

    total_Xi_Ni_2 = sum(Xi_Ni_2)

    print('Total del Xi ni ^ 2', total_Xi_Ni_2)

    Media_Xi_Ni = total_Xi_Ni/total_numeros

    print(f"Esta es la media: {Media_Xi_Ni}")

    #Variacion y desviación estándar: 

    calculo_varianza = round((total_Xi_Ni_2/VI) - (Media_Xi_Ni ** 2),2)
    desviancion_estandar = round(np.sqrt(calculo_varianza),3)

    print(f"La varianza es: {calculo_varianza} y la desviación estándar es: {desviancion_estandar}")

