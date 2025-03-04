# Conversor de TEMPERATURA
# Descripción: Haz un programa que convierta temperaturas entre Celsius, Fahrenheit y Kelvin.
# Objetivo: Practicar la manipulación de números flotantes y las conversiones.
# Conceptos clave: Funciones, conversiones de unidades, manejo de entradas.

# def kelvin(temperatura):
#     conversion = temperatura + 237.15
#     return conversion

# def my_converter():
#     print('Bienvenid@ a su conversor online\nPor favor indique unidad metrica inicial:')
#     unidad_metrica_inicial = int(input('*1* Celsius\n*2* Fahrenheit\n*3 *Kelvin\n'))
#     print('Perfecto ahore ingrese a cuál unidad metrica desea convertir')
#     unidad_metrica_convertir = int(input('*1* Celsius\n*2* Fahrenheit\n*3* Kelvin\n'))
#     print('Genial! ahora indique la temperatura')
#     temperatura = int(input())
#     conversion = 0
#     match unidad_metrica_inicial:
#         case 1:
#             if unidad_metrica_inicial == unidad_metrica_convertir:
#                 print('Las unidades metricas son las mismas!')
#             elif unidad_metrica_convertir == 2:
#                 conversion = (temperatura * 1.8) + 32
#             else:
#                 conversion = kelvin(temperatura)
#         case 2:
#             if unidad_metrica_inicial == unidad_metrica_convertir:
#                 print('Las unidades metricas son las mismas!')
#             elif unidad_metrica_convertir == 1:
#                 conversion = (temperatura - 32)* 1.8
#             else:
#                 conversion = (temperatura + 459.67) * 0.55
#         case 3:
#             if unidad_metrica_inicial == unidad_metrica_convertir:
#                 print('Las unidades metricas son las mismas!')
#             elif unidad_metrica_convertir == 1:
#                 conversion = temperatura - 273.15
#             else:
#                 conversion = (temperatura * 1.8) - 459.67 
#     print(f' La temperatura convertida es: {conversion}')


#my_converter()

# Generador de Contraseñas Aleatorias
# Descripción: Crea un programa que genere contraseñas seguras y aleatorias.
# Objetivo: Aprender a usar la librería random para generar caracteres aleatorios.
# Conceptos clave: Librerías, cadenas de texto, ciclos, manejo de entradas.

# import random #Importo modulo para utilizar método random
# import string #Modulo para utilizar método digits, letters
# def password_random():
#     num = random.random() #número tipo flotante random del 0 al 1
#     numero = random.randint(1,100) #Número entero aleatorio entre dos parametros dados
#     #seleccion = random.choice()#Selecciona un elemento aleatorio de un iterable que se le pasa
#     numeroDos = random.randint(1,80)
#     text = string.ascii_letters #abecedario completo
#     multiply = string.digits #números del 0 al 9 formato string?
#     for x in range(numero):
#         print(''.join(
#             random.SystemRandom().choice(text + multiply)
#             for i in range(numeroDos)
#         ))
    

# password_random()


# Contador de Palabras
# Descripción: Crea un programa que cuente la cantidad de palabras que contiene un texto introducido por el usuario.
# Objetivo: Practicar el manejo de cadenas de texto.
# Conceptos clave: Métodos de cadenas, bucles, diccionarios (si quieres contar cuántas veces aparece cada palabra).

def counter_world(text): #Recibe como argumento el texto en cuestión
    worlds = text.split() #Devuelve una list con cada palabra como elemento ''
    counter = {} #Creo un set/conjunto para guardar el númeor de palabras
    for world in worlds:
        if world in counter:
            counter[world] += 1
        else:
            counter[world] = 1
    return counter

#print(counter_world('Hello, World! Hello, World! Hello, World!'))

#Crear un programa que busque una determinada palabra dada, dentro de un texto especifico
def search_world(world,text):
    split = text.split()
    lista = set()
    count = {}
    for x in split:
        if world.lower() in x.lower():
            lista.add(x)
            #count[x] += 1
    return lista, count

print(search_world('Amor','Amor, amor, cariño, prosperidad, paz, alegria, exito'))

def buscar_palabra(archivo, palabra):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
            for numero, linea in enumerate(lineas, start=1):
                if palabra in linea:
                    print(f"Línea {numero}: {linea.strip()}")
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
archivo = 'ejemplo.txt'
palabra = 'Python'
buscar_palabra(archivo, palabra)


#Empresa solicita calcular días de vacaciones correspondientes a cada empleo según los siguientes parametros:
# Existen tres departamentos en la empresa
#Comercial  año de servicio = 10 días, 2 a 6 años 20 días, más años 30 días key 3
# Logística   1 año de servicio = 7 días. 2 a 6 años = 15 días, más años 22 días key 2
# Atención al cliente 1 año de servicio = 6 días 2 a 6 años = 14 días más 20 días key 1
#Requerimientos indispensables: el sistema debe solicitar el nombre, clave del departamento y antiguedad
#El sistema debe devolver mediante consola el nombre del trabajador y días de vacaciones.

# def vacances():
#     print('---------*Welcome*---------\n------*Rappi enterprise holdings*-----\n')
#     name = input('Insert employee name please:\n')
#     department = int(input('Insert department please:\n1)Customer\n2)Logistics\n3)Management\n'))
#     year = int(input('Insert antiquity please:\n'))
#     match department:
#         case 1:
#             if year == 1:
#                 print(f'The employee: {name} have 6 days of vacations')
#             elif year in range(2,7):
#                 print(f'The employee {name} have 14 days of vacations')
#             elif year >= 7:
#                 print(f'The employee {name} have 20 days of vacations')
#             else:
#                 print(f'The employee {name} not have vacations, sorry')
#         case 2:
#             if year == 1:
#                 print(f'The employee {name} have 7 days of vacations')
#             elif year in range(2,7):
#                 print(f'The employee {name} have 15 days of vacations')
#             elif year >= 7:
#                 print(f'The employee {name} have 22 days of vacations')
#             else:
#                 print(f'The employee {name} not have days of vacations')
#         case 3:
#             if year == 1:
#                 print(f'The employee {name} have 10 days of vacations')
#             elif year in range(2,7):
#                 print(f'The employee {name} have 20 days of vacations')
#             elif year >= 7:
#                 print(f'The employee {name} have 30 days of vacations')
#             else:
#                 print(f'The employee {name} not have vacations, sorry')
#         case _:
#             print('Insert an option valid please!')
#             vacances()    

# vacances()