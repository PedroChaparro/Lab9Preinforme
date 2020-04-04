#Un algoritmo que dadas las coordenadas x1, y1, x2, y2 en el plano cartesiano
#calcule la distancia euclidiana entre ellos (considere todos los valores positivos)

import math

def calcular_distancia(x1,y1,x2,y2):

    d_euclidiana = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d_euclidiana

x1 = float(input("Ingrese la coordenada en X del primer punto: "))
y1 = float(input("Ingrese la coordenada en Y del primer punto: "))

x2 = float(input("Ingrese la coordenada en X del segundo punto: "))
y2 = float(input("Ingrese la coordenada en Y del segundo punto: "))

distancia = calcular_distancia(x1,y1,x2,y2)

print("La distancia entre los puntos con coordenadas X1={}, Y1={}, X2= {} y Y2={} es: {}".format(x1,y1,x2,y2,distancia))





