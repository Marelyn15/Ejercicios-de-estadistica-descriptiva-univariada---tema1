from intervaltree import Interval
from collections import Counter
import Intervalos as Itvl
import boxplot as cj
import estadistica as stb #Estadistica basica
import estadistica2 as sdu #Estadistica descriptiva univariada
import tabla_frecuencia_valorres_estaticos as tfve

#--------------------------------- Ejercicios básicos de estadística --------------------------------------------------------------------------------
group5 = [283.6,269.4,262.2,261.1,246.7,245.5,239.2,233.7,230.3,227.9,226.4,225.5,224.1,223.6,222.3,221.4,217.8,217.2,216.9,211.6,211.4,208.5,204.9,202.7,202.4,200.5,198.5,182.4,111]

stb.estadisticas(group5)
#--------------------------------- Ejercicios básicos de estadística descriptiva univariada --------------------------------------------------------
group = [3,6,6,8,2,5,7,3,8,1,5,6,4,4,2,5,6,2,9,4,2,3,7,7,7]
percentil = 85

sdu.tabla_frecuencia(group,percentil)

#--------------------------------- tabla frecuencia valorres estaticos ----------------------------------------------------------------------------
xi = [0,1,2,3]
ni = [8,102,85,5]
tfve.tabla_frecuencia(ni,xi)
#--------------------------------- Ejercicios de intervalos desde una lista -------------------------------------------------------------------------
print("Ejercicios de intervalos desde una lista")
#Para sacar el valor maximo y minimo de una mejor manera
grupo = [60,66,77,70,66,68,57,70,66,52,75,65,69,71,58,66,67,74,61,63,69,80,59,66,70,67,78,75,64,71,81,62,64,69,68,72,83,56,65,74,67,54,65,65,69,61,67,73,57,62,67,68,63,67,71,68,76,61,62,63,76,61,67,67,64,72,64,73,79,58,67,71,68,59,69,70,66,62,63,66]

#OJO: Inicio del intervalo se disminuirá hacia el cero o cinco más cercano ejemplo 52, el inicio es 50
#OJO: Fin del intervalo se elevará hacia el cero o cinco mas cercano, ejemplo 83, el fin es 85 
print(f"El valor mas pequeño del grupo es {min(grupo)}. El valor más grande es {max(grupo)}")

#Crea los intervalos basado en el tamaño especificado en el ejercicio tomando en cuenta los valores inicial y final
def intervalos(inicio, fin, tamaño):
    intervalos = []
    while inicio < fin:
        intervalos.append(Interval(inicio, inicio + tamaño))
        inicio += tamaño
    return intervalos

saltos = intervalos(50,85,5)

# Función para mapear cada intervalo al número de frecuencia estática.
def mapeo_intervalos(grupo, saltos):
    mapeo = []
    for numero in grupo:
        for salto in saltos:
            # El intervalo [inicio, fin) incluye inicio pero excluye fin
            if salto.begin <= numero < salto.end: #Se toma la variable salto que se crea en el for.
                mapeo.append(salto)
                break
    return mapeo


mapeo = mapeo_intervalos(grupo,saltos)
FA = Counter(mapeo)
FA = dict(sorted(FA.items()))

datos_ord_intervalos = [] #Clave Individual
#Valores de la clave individual
for index, valor in enumerate(FA.values()):
    datos_ord_intervalos.insert(index,valor)
#print(datos_ord_intervalos)


Itvl.tabla_frecuencia_intervalos(saltos,datos_ord_intervalos)

#----------------------- Frecuencia estática en Intervalos ---------------------------------------------
print("Frecuencia estática en Intervalos")
intervals = intervalos(0,80,20)
#Cuando los datos son estáticos
datos_ord_intervalos = [45,10,5,2] #Ni o frecuencia

Itvl.tabla_frecuencia_intervalos(intervals,datos_ord_intervalos)
#----------------------- Caja y bigote -----------------------------------------------------------------

grupo = [283.6,269.4,262.2,261.1,246.7,245.5,239.2,233.7,230.3,227.9,226.4,225.5,224.1,223.6,222.3,221.4,217.8,217.2,216.9,211.6,211.4,208.5,204.9,202.7,202,200.5,198.5,182.4,111]
paises = [0.16,0.20,0.06,0.06,0.07,0.17,0.06,0.22]

cj.caja_bigotes(grupo, paises)