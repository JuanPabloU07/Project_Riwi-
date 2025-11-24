import math
import random
import datetime

# 1. conversor de temperatura
while True:
    try:
        fahrenheit = int(input("Ingrese una temperatura en grados Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5.0/9.0
        print(f"{fahrenheit}°f es igual a {celsius:.2f}°c")
    except ValueError: 
        print("Ingrese un numero valido")    
    finally:
        print("Fin del programa")
    print("-----------------------------------------")
        # 2. divisor 
    try:
        num = int(input("Introduce un número a dividir: "))
        print("El resultado es:", num / 2)
    except ValueError:
        print("Ingresa un número válido.")
    finally:
        print("Fin del programa")
    print("--------------------------------------------")
# 3. Uso combinado 
    print("Raíz:", math.sqrt(44))
    print("Aleatorio:", random.randint(1, 10))
    print("-------------------------------------")
# 4. fechas
    print("Fecha:", datetime.date.today())  
