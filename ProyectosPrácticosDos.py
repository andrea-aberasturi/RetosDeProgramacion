# Conversor de TEMPERATURA
# Descripción: Haz un programa que convierta temperaturas entre Celsius, Fahrenheit y Kelvin.
# Objetivo: Practicar la manipulación de números flotantes y las conversiones.
# Conceptos clave: Funciones, conversiones de unidades, manejo de entradas.

def my_converter():
    print('Bienvenid@ a su conversor online\nPor favor indique unidad metrica inicial:')
    unidad_metrica_inicial = int(input('*1* Celsius\n*2* Fahrenheit\n*3 *Kelvin\n'))
    print('Perfecto ahore ingrese a cuál unidad metrica desea convertir')
    unidad_metrica_convertir = int(input('*1* Celsius\n*2* Fahrenheit\n*3* Kelvin\n'))
    print('Genial! ahora indique la temperatura')
    temperatura = int(input())
    conversion = 0
    match unidad_metrica_inicial:
        case 1:
            if unidad_metrica_inicial == unidad_metrica_convertir:
                print('Las unidades metricas son las mismas!')
            elif unidad_metrica_convertir == 2:
                conversion = (temperatura * 1.8) + 32
            else:
                conversion = temperatura + 273.15
        case 2:
            if unidad_metrica_inicial == unidad_metrica_convertir:
                print('Las unidades metricas son las mismas!')
            elif unidad_metrica_convertir == 1:
                conversion = (temperatura - 32)* 1.8
            else:
                conversion = (temperatura + 459.67) * 0.55
        case 3:
            if unidad_metrica_inicial == unidad_metrica_convertir:
                print('Las unidades metricas son las mismas!')
            elif unidad_metrica_convertir == 1:
                conversion = temperatura - 273.15
            else:
                conversion = (temperatura * 1.8) - 459.67 
    print(f' La temperatura convertida es: {conversion}')


my_converter()