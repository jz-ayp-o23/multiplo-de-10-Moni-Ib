"""
Determinar si un número dado es múltiplo de 10
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
CONSTANTE = 10

# Entradas
entrada = int(input("Introduzca un número: "))

# Proceso
if entrada % CONSTANTE == 0:
    salida = (f"El número {entrada} sí es múltiplo de {CONSTANTE}")
else:
    salida = (f"El número {entrada} no es múltiplo de {CONSTANTE}")

# Salidas
print(salida)
