#Historias Locas a partir de input que da el user
# def history_crazy():
#     global name 
#     name = input('Indica un nombre para tu Historia ')
#     global place
#     place = input('Ahora indica un lugar ')
#     global hecho
#     hecho = input('Menciona un succeso principal ')

# history_crazy()
# desenlaces = input('Selecciona una de las opciones siguientes: \n*1: Final feliz \n*2: Final trágico \n*3: Final abierto\n')
# print('Creando history crazzy...')

# def history_principal():
#    print(f'TITLE: {name} \nThis History beginnin in {place} where the personaje principal faire: {hecho}')

# def desenlace(desenlaces):
#     match desenlaces:
#         case '1':
#             history_principal()
#             print('Fare fare away in this lejan oest, el etait une doncelle trés belle...')
#             print('La doncella tenia una madrastra malvada pero al final logre superaro')
#         case '2':
#             history_principal()
#             print('Fare fare away in this lejan oest, el etait une doncelle trés belle...')
#             print('La doncella comio la manzana envenenada y termino durmiendo por siempre')
#         case '3':
#             history_principal()
#             print('Fare fare away in this lejan oest, el etait une doncelle trés belle...')
#             print('Ella mordio la manzana pero luego...')
#         case _:
#             print('Please insert a option valid')

# desenlace(desenlaces)

# #Zodiac
# import sys
import math
import random

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
'''zodiac = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
n = int(input('Insert your year of born: '))
year = n - 1900
ind = year % 12
print(f'Yoy Chinese sign is: {zodiac[ind]}')
'''
#Adivina el número
# def juex(x):
#     num = random.randint(1,x)
#     prediccion = 0
#     while prediccion != num:
#         prediccion = int(input(f'Selecciona un número entre 1 y {x}: '))

#         if prediccion < num:
#             print('Número menor')
#         elif prediccion > num:
#             print('Número mayor')
#     print(f'Felicitaciones Adivinaste {num}')

# juex(10)


#Calculatrice fácile
# def calculatrcie():
#     operation = input('Choise a operator: add, rest, multiply or divided')
#     num1 = int(input('Insert a number '))
#     num2 = int(input('Insert other number '))
#     resultado = 0
#     match operation:
#         case 'add':
#             resultado = num1 +num2
#         case 'rest':
#             resultado = num1 - num2
#         case 'multiply':
#             resultado =  num1 * num2
#         case 'divided':
#             resultado = num1/num2
#     print(resultado)
#     return resultado


# calculatrcie()

# Crear  una agenda donde se pueda buscar, agregar, eliminar o editar contactos
agenda = dict() #Creo un diccionario para almacenar contactos, par clave:valor

def my_agenda():
    print('*-----------------------------------------*')
    print('*-------Bienvenid@ a su agenda 2.0--------* \nSeleccione una de las opciones a continuación:')
    accion =  int(input('1- Agregar contacto \n2- Buscar contacto \n3- Eliminar contacto \n4- Editar contacto\n5- Salir de la agenda\n'))#Doy opciones al user
    match accion:
        case 1:
            nombre = input('Ingrese el nombre del nuevo contacto ')
            telefono = int(input('Ahora ingrese el número de telefono: '))
            if nombre in agenda:
                print('Este contacto ya existe')
            else:
                agenda.update({nombre : telefono})
                #agenda[nombre] = telefono
            print('Agregando contacto a su agenda...')
            my_agenda()
            #return agenda
        case 2:
            nombre = input('Ingrese el nombre del contacto ha buscar: ')
            if nombre not in agenda:
                print('El contacto no existe en la agenda')
                my_agenda()
            else:
                print(agenda[nombre])
                my_agenda()
            #return agenda
        case 3:
            nombre = input('Ingrese el nombre del contacto ha eliminar: ')
            if nombre not in agenda:
                print('El contacto no existe')
            else:
                print('Eliminando contacto...')
                del agenda[nombre]
                print('Contacto eliminado con exito!')
                my_agenda()
            #return agenda
        case 4:
            nombre = input('Ingrese el nombre del contacto ha actualizar: ')
            telefono = int(input('Ingrese nuevo telefono: '))
            if nombre not in agenda:
                print('El contacto no existe')
                my_agenda()
            else:
                print('Actualizando contacto')
                agenda[nombre] = telefono
                my_agenda()
            #return agenda
        case 5:
            print('Saliendo de la agenda...')
            return
        case _:
            print('Opción no valida, por favor ingresa una opción valida')
            my_agenda()
    return agenda

my_agenda()
# print(dir(dict))