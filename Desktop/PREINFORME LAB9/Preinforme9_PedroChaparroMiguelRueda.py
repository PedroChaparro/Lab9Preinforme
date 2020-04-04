#Leer las cinco notas obtenidas por un estudiantes y calcular su nota final
# n1 = 15%, n2 = 20%, n3 = 15%, n4 = 30%, n5 = 20%
#Si nota < 2.0 "No puede habilitar"
#Si nota < 3.0 "Reprobó"
#Si nota >= 3.0 "Aprobó"
#Si nota > 4.5 "Felicitaciones"

def cal_nota():

    nuevo = "Si"

    while nuevo == "Si":

        n1 = float(input("Ingrese la nota 1 obtenida por el estudiante: "))
        n2 = float(input("Ingrese la nota 2 obtenida por el estudiante: "))
        n3 = float(input("Ingrese la nota 3 obtenida por el estudiante: "))
        n4 = float(input("Ingrese la nota 4 obtenida por el estudiante: "))
        n5 = float(input("Ingrese la nota 5 obtenida por el estudiante: "))

        nota_final = (n1*0.15) + (n2*0.2) + (n3*0.15) + (n4*0.3) + (n5*0.2)
        print("La nota final del estudiante es: {}".format(nota_final))

        nuevo = input("¿Desea calcular un estudiante más? Escriba Si o No: ")
        nuevo = nuevo.title()

cal_nota()






