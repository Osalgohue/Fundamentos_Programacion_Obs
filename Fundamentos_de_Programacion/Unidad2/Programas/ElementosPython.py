"""
Programa para estudiar los elementos de el lenguaje de programacion de Python
Mi nombre es Oscar Alejandro
"""

nombre = "ana"  # VAR tipo String
edad = 19  # VAR tipo Int
estatura = 1.65  # VAR tipo Float
es_estudiante = True  # VAR tipo Bool


print("Nombre:", nombre, type(nombre))
print("Edad:", edad, type(edad))
print("Estatura:", estatura, type(estatura))
print("Estudiante:", es_estudiante, type(es_estudiante))

PROMEDIO_MINIMO = 6

materia = input("Que materia cursas?")
calificacion = float(input("Que calificacion tienes?"))

suma = 8 + 2
resto = 10 % 3
potencia = 2**4
mayor_de_edad = edad >= 18
aprobado = calificacion >= PROMEDIO_MINIMO and es_estudiante

print("Suma:", suma, "| Resto:", resto, "| Potencia:", potencia)
print("Mayor de edad?, mayor_de_edad")
