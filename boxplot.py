import statistics as st
import numpy as np

def caja_bigotes(grupo):
    #Ejercicios de boxplot

    print("Ejercicios de caja y bigotes")

    grupo = sorted(grupo)
    tamanio = len(grupo)
    print("El grupo es: ", grupo ,"y su tamaño es: ", tamanio)

    Q2 = st.median(grupo)
    indice = 0
    for i in grupo:
        indice = indice + 1
        if i == Q2:
            break

    indice = indice
    print(f"La mediana del grupo es {Q2} y su indice es {indice}")
    #media: 
    media = sum(grupo)/tamanio
    print(f"Esta es la media {media}")
    moda = st.mode(grupo)
    print(f"Esta es la media {moda}")


    grupo2  = []
    for i in grupo:
        if i < Q2:
            grupo2.append(i) 

    print(grupo2)
    Q1 = st.median(grupo2)
    print(f"La mediana del grupo2 es {Q1}")

    grupo3  = []
    for i in grupo:
            if i > Q2:
                grupo3.append(i) 

    print(grupo3)
    Q3 = st.median(grupo3)
    print(f"La mediana del grupo3 es {Q3}")

    valor_minimo = min(grupo)
    valor_maximo = max(grupo)

    print(f"El valor minimo del grupo completo es: {valor_minimo} y el valor maximo es {valor_maximo}")

    #Verificando si hay valores atípicos: 
    RI = Q3 - Q1 #Rango Intercuartilico
    BS = Q3 + 1.5 * RI #Barrera superior
    BI = Q1 - 1.5 * RI #Barrera inferior

    print(f"Se consideran valores atípicos los numeros que sea menor o igual a {BI} o mayor o igual a {BS}")

    Valores_BS = []
    Valores_BI = []
    for i in grupo:
         if i >= BS:
              Valores_BS.append(i)

    for i in grupo:
         if i <= BI:
              Valores_BI.append(i)

    calculo_varianza = np.var(grupo)
    desviancion_estandar = np.sqrt(calculo_varianza)

    print(f"La varianza es: {calculo_varianza} y la desviación estándar es: {desviancion_estandar}")

    #Coeficiente de variación: 

    Vp =  (desviancion_estandar / media) * 100

    print(f"El coeficiente de variacion es {Vp}")

    #Asimetria
    As = round((Q1 + Q3 - ( 2 * Q2))/Q3-Q1,2)

    if As < 0:
         print(f"El valor de la asimetría basada en cuantiles es: {As}, y es una asimetría es negativa")
    elif As > 0:
        print(f"El valor de la asimetría basada en cuantiles es: {As}, y es una asimetría es positiva")
    else:
         print(f"El coeficiente de asimetria basada en cuantiles es simétrico {As}")

    #Asimetria de pearson
    Ap = (media - moda)/desviancion_estandar
    print(f"El coeficiente de asimetría de pearson es {Ap}")