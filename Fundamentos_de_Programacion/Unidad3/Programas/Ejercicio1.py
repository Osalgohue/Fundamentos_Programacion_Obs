"""
Fundamentos de Programacion
Oscar Alejandro Gonzalez Huelgas
Modulo 3
"""

valides = False
calificacion = float(input("Escribe tu calificacion: "))

while valides != True:
    if (calificacion <= 0) | (calificacion > 10):
        print("calificacion invalida \n")
        calificacion = float(input("Escribe tu calificacion: "))
    else:
        valides = True

if calificacion >= 9:
    print("Exelente")
elif calificacion > 8:
    print("Buen Trabajo")
elif calificacion > 5:
    print("Aprobaste")
else:
    print("Reprobado")
