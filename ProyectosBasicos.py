#Historias Locas a partor de input que da el user
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
def juex(x):
    num = random.randint(1,x)
    prediccion = 0
    while prediccion != num:
        prediccion = int(input(f'Selecciona un número entre 1 y {x}: '))

        if prediccion < num:
            print('Número menor')
        elif prediccion > num:
            print('Número mayor')
    print(f'Felicitaciones Adivinaste {num}')

juex(10)