#1) Realiza una función que devuelva el área de un círculo a partir de un radio. La función se llamará area_circulo().
#  El radio se pedirá al usuario por teclado:

import math

def area_circulo():
    radio = float(input("Introduce el valor del radio:\n"))
    area = (radio**2) * math.pi
    return 'El área de un circulo de radio {} es de {} unidades cuadradas.'.format(radio, area)

print(area_circulo())


