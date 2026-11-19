import math  # Importa funciones de la libreria "math"

radio = float(input("Radio del circulo: "))

area = math.pi * math.pow(radio, 2)
perimetro = 2 * math.pi * radio

print("Area:", round(area, 2))
print("Perimetro: ", round(perimetro, 2))
print("Raiz cuadrada del radio: ", round(math.sqrt(radio), 2))
print("Techo del area: ", math.ceil(area))
print(" ")

print("Truncate radio: ", math.trunc(radio))
print("Tanjente radio: ", math.tan(radio))

"""
Toda funcion de la libreria math se llama usando:
    math.Nombre_Funcion(variables, si_se_nesesitan)

Las funciones usadas en este codigo son:
    math.pow(x, y)  potencia de x en y
    math.pi         solo es el numero "pi"
    math.sqrt(x, y) Raiz cuadrada de x en y
    math.ceil(x)    Redondea numero a int mas cercano
"""
