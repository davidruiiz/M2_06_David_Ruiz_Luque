#1) Realiza una función que devuelva el área de un círculo a partir de un radio. La función se llamará area_circulo().
#  El radio se pedirá al usuario por teclado:

import math

def area_circulo():
    radio = float(input("Introduce el valor del radio:\n"))
    area = (radio**2) * math.pi
    return 'El área de un circulo de radio {} es de {} unidades cuadradas.'.format(radio, area)

print(area_circulo())

#2) Realiza una función llamada lee_numero() que solicite y lea por teclado un numero. Utilizar esta función para pedirle al usuario 3 números. 
# Luego pasarle estos 3 números a una función que se llame mayor() que tenga 3 parámetros y que devuelva el número mayor de los 3:

def lee_numero():
    numero=float(input("Introduce un número cualquiera:\n "))
    return numero

num1=lee_numero()
num2=lee_numero()
num3=lee_numero()

def mayor(a,b,c):
    if a<b<c:
        return '{} es el mayor de los tres números introducidos.'.format(c)
    elif a>b>c:
        return '{} es el mayor de los tres números introducidos.'.format(a)
    else:
        return '{} es el mayor de los tres números introducidos.'.format(b)

print(mayor(num1,num2,num3))

#3) Realizar una función llamada imc(). Esta función nos proporcionará el estado nutricional de una persona.
#  Esto es; la clasificación de su índice de masa corporal (IMC), según la tabla proporcionada.
#  La función recibirá el peso (en kilos) y la talla de una persona (en metros con dos decimales), datos a partir de los cuales se puede calcular el IMC cómo:

def imc():
    alura=float(input('Introduce la altura en metros:\n'))
    peso=float(input('Introduce el peso en Kg:\n'))
    
    



