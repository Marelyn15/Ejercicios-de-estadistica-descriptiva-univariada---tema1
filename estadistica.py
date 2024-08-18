import statistics as st
import math

def estadisticas(grupo):
    print("Ejercicios básicos de estadística")
    #----------Funciones estadisticas ---------------------------..
    media = round(st.mean(grupo),2) 
    mediana = round(st.median(grupo),2)
    tamanio = len(grupo)
    orden = sorted(grupo)

    #--------------Funciones hechas -------------------------------
    def media_acotada_dos_lados(lista, porcentaje):
        lista = sorted(lista)
        porcentaje = porcentaje / 100
        digitos_en_lista = len(lista)
        numeros_quitar = digitos_en_lista * porcentaje
        i = 0
        while i < numeros_quitar:
            del lista[0]
            del lista[-1]
            i = i + 1
        return(lista)
    
    def media_acotada(lista, porcentaje):
        lista = sorted(lista)
        porcentaje = porcentaje / 100
        digitos_en_lista = len(lista)
        numeros_quitar = digitos_en_lista * porcentaje
        i = 0
        while i < numeros_quitar:
            del lista[0]
            i = i + 1
        return(lista)
    
    def varianza(lista):
        largo = tamanio - 1
        all_values = []
        for i in lista:
            element = (i - media) ** 2
            all_values.append(element)
        all_values = sum(all_values)
        resultado = 1 / largo * (all_values)
        return resultado
    
    def estandar(lista):
        largo = tamanio - 1
        all_values = []
        for i in lista:
            element = (i - media) ** 2
            all_values.append(element)
        all_values = sum(all_values)
        resultado = 1 / largo * (all_values)
        return round(math.sqrt(resultado),2)



    #-----------------------resultados-----------------------------------------------------------------
    calculo_varianza = round(varianza(grupo),2)
    desviancion_estandar = estandar(grupo)
    media_ya_acotada_dos_lados = round(st.mean(media_acotada_dos_lados(grupo, 10)),2)
    media_ya_acotada = round(st.mean(media_acotada(grupo, 10)),2)


    #---------------------resultado final--------------------------------------------------------------
    print(f"Estos son los resultados del {grupo}: organizados dan como resultado: {orden}, la cantidad de numeros es: {tamanio} la media es: {media}, la mediana es: {mediana}, la media acortada es a dos lados:  {media_ya_acotada_dos_lados}, la media acortada es: {media_ya_acotada}, la varianza es {calculo_varianza}, y la desviación estándar es {desviancion_estandar}")
    
