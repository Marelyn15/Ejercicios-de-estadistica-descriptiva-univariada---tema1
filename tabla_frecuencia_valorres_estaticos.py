from collections import Counter
import numpy as np

def tabla_frecuencia(ni,xi):
    print("tabla frecuencia valorres estaticos")
    total_ni = sum(ni)
    mitad = total_ni/2

    #frecuencia absoluta
    #Organizando
    FA = dict(zip(xi, ni))
    print(f"Esto es la frecuencia absoluta (FA): {FA}")

    #Frecuencia absoluta acumulada
    nuevo_valor = 0
    FAA = []
    for index, valor in enumerate(FA.values()): 
        nuevo_valor = valor + nuevo_valor
        FAA.insert(index,nuevo_valor)
    print(f"Frecuencia Absoluta acumulada (FAA) {FAA}")

    
    #Xi Ni multiplicacion marca clase y frecuencia
    Xi_Ni = []
    for index, valor in enumerate(xi):
        mult = valor * ni[index]
        Xi_Ni.insert(index,mult)
    total_Xi_Ni = sum(Xi_Ni)

    print(f'Puntos medios por frecuencia (Xi ni): {Xi_Ni} y el total es: {total_Xi_Ni}')

    #Xi Ni multiplicacion marca clase y frecuencia
    Xi_Ni_2 = []
    for index, valor in enumerate(xi):
        mult = (valor**2) * ni[index]
        Xi_Ni_2.insert(index,mult)
    total_Xi_Ni_2 = sum(Xi_Ni_2)

    print('Puntos medios por frecuencia (Xi^2 ni)', Xi_Ni_2, 'y el total es:', total_Xi_Ni_2)

    FR = {num: round(freq / len(xi),2) for num, freq in FA.items()} # Numero : frecuencia relativa
    print(f"Esto es la frecuencia relativa (FR) {FR}")
    
    #Frecuencia relativa acumulada:
    nuevo_valor = 0
    FRA = []
    for index, valor in enumerate(FR.values()):
        nuevo_valor = valor + nuevo_valor
        FRA.insert(index,round(nuevo_valor,2))
    FRA = dict(zip(xi, FRA))
    print(f"Esto es frecuencia relativa acumulada (FRA) {FRA}")

    def encontrar_numero_cercano(numero, lista):
        numero_cercano = lista[0]
        indice_cercano = 0
        diferencia_minima = abs(numero - numero_cercano) 

        for i in range(1,len(lista)):
            diferencia_actual = abs(numero - lista[i])
            if diferencia_actual < diferencia_minima:
                numero_cercano = lista[i]
                indice_cercano = i
                diferencia_minima = diferencia_actual
        return numero_cercano, indice_cercano

    numero_cercano, indice = encontrar_numero_cercano(mitad, ni)
   

    def encontrar_el_valor_mas_frecuente(ni):
        vmf = max(ni)
        for index, numero  in enumerate(ni):
            if numero == vmf: 
                return index
            
    mas_frecuente = encontrar_el_valor_mas_frecuente(ni)

    print(f"El indice del valor más frecuente es: {mas_frecuente}")

    Media_Xi_Ni = total_Xi_Ni/total_ni
    mo = xi[mas_frecuente] #se podria sacar de otra forma
    me = xi[indice] #El numero del medio
    print(f"La media es {Media_Xi_Ni}, la moda es: {mo} y la mediana es: {me}")

    #Variacion y desviación estándar: 

    calculo_varianza = round((total_Xi_Ni_2/total_ni) - (Media_Xi_Ni ** 2),2)
    desviancion_estandar = round(np.sqrt(calculo_varianza),3)

    print(f"La varianza es: {calculo_varianza} y la desviación estándar es: {desviancion_estandar}")

    #Coeficiente de variación: 
    Vp =  round((desviancion_estandar / Media_Xi_Ni),2)

    print(f"El coeficiente de variacion es {Vp}%")

    #Asimetria de pearson

    Ap = (Media_Xi_Ni - mo)/desviancion_estandar
    print(f"El coeficiente de asimetría de pearson es {Ap}")

    Ap = round(3 * ((Media_Xi_Ni - me)/desviancion_estandar),2)
    print(f"El coeficiente de asimetría de pearson es {Ap}")
