"""
Fundamentos de Programacion
Oscar Alejandro Gonzalez Huelgas
Modulo 3
"""

Monto = float(input("Monto de cobro: "))

if Monto >= 1000:
    print(Monto, "|", Monto * 0.1, "|", Monto * 0.9)
else:
    print("Total a pagar: ", Monto)

