'''Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.'''
def my_IMC():
    peso = int(input('Indica tu peso en kilogramos por favor:\n'))
    estatura = float(input('Ahora indica tu estatura en metros por favor:\n'))
    imc = round(peso / (estatura * estatura),2)
    
    print(f'Tu indice de masa corporal es: {imc}')

#my_IMC()
''' Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.'''
def my_INVERSION():
    monto = int(input('Ingrese el monto a invertir:\n'))
    renta = int(input('Ahora ingrese la renta anual:\n'))
    plazo = int(input('Indique el plazo de dicha inversión:\n'))
    capital_estimado = monto * renta *plazo
    print(f'El estimado de capital para esa fecha es: {capital_estimado}') 

#my_INVERSION()

# #Crear un programa de notas, donde el usuario pueda: Agregar, Eliminar, Editar o Ver las notas.
# #Paso 1 definir la estructura de las notas
# nota = {
#     'titulo': 'Mi primer nota',
#     'contenido': 'Este es el contenido de la nota'
# }
# #Paso 2 crear las funcionalidades

# Ejercicio de diccionarios
# Escribe un programa que cree un diccionario con las claves 'nombre', 'edad' y 'ciudad', y luego imprima un mensaje que contenga esa información de la siguiente forma: "Mi nombre es [nombre], tengo [edad] años y vivo en [ciudad]."
# Pistas:
# Usa el método .get() para acceder a los valores en el diccionario.
def metodo_get():
    my_dict = dict()
    name = input('Indique su nombre:\n')
    age = input('Indique su edad:\n')
    city = input('Indique su ciudad de residencia:\n')
    my_dict['name'] = name
    my_dict['age'] = age
    my_dict['city'] = city
    print(f'Mi nombre es {my_dict.get('name')} y tengo {my_dict.get('age')} además vivo en {my_dict.get('city')}')

# #metodo_get()
# Ejercicio de manejo de excepciones
# Escribe un programa que pida al usuario ingresar un número y lo divida entre otro número. Si el segundo número es 0, el programa debe mostrar un mensaje de error y pedir que ingrese un número válido.
# Pistas:
# Usa un bloque try-except para manejar la excepción de división por cero.
def my_calculator():
    divisor = int(input('Indique un número:\n'))
    dividendo = int(input('Indique otro número:\n'))
    try:
        dividendo !=0 and divisor !=0
        resultado = divisor / dividendo
        print(resultado)
    except:
        print('Imposible dividir entre cero, indique un número válido por favor')
        my_calculator()

#my_calculator()

# Ejercicio de manipulación de cadenas
# Escribe un programa que reciba una cadena de texto del usuario y luego imprima esa cadena al revés.
# Pistas:
# Usa el slicing [::-1] para invertir la cadena.
def my_reverse_string():
    text = input('Ingrese un texto\n')
    reverse = text[::-1]
    print(reverse)

#my_reverse_string()

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

#Modificación del  programa ut supra, manejo de errores try catch
import math, random #Importo modulo para utilizar métodos matemáticos
from random import randint #Importo modulo randint

def my_juex():
    print('---------------------------------------------------------------------------------')
    print('                              Bienvenido      ')
    print('Este es un programa donde debes adivinar el número seleccionado por computadora')
    print('--------------------------------------------------------------------------------')
    try:
        rango = int(input('Selecciona el rango deseado por favor: \n'))
        num = random.randint(1,rango)
    except:
        print('Ingrese un número entero por favor')
        return my_juex()
    predicción = 0
    print('Muy bien! estamos generando el número aleatorio')
    print('|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_')
    print('Listo! ')
    while predicción != num:
        try:
            predicción = int(input(f'Ahora intenta adivinar el número, ingresa un entero desde 1 a :{rango}\n'))
            if predicción < num:
                print('El número es muy pequeño! prueba otra vez! (:')
            elif predicción > num:
                print('El número es muy grande, prueba otra vez!')
        except:
            print('Ingrese un número entero por favor!')
    print(f'Felicitaciones adivinaste el número! {num}')

#my_juex()

#Ejercicios compresión de listas
'''Ejercicio 1: Crear una lista de cuadrados
Instrucción: Crea una lista de los primeros 10 números enteros (del 0 al 9) al cuadrado usando comprensión de listas.'''
lista_cuadrados = [num*num for num in range(0,10)]
#print(lista_cuadrados)

'''Ejercicio 2: Filtrar números pares
Instrucción: Dada una lista de números, usa comprensión de listas para filtrar solo los números pares.'''
valores = [1,6,5,78,30,3,99,105,15478,2036547,10,7]
pares = [num for num in valores if num % 2 == 0]
#print(pares)

'''Ejercicio 3: Transformar cadenas a mayúsculas
Instrucción: Dada una lista de cadenas, utiliza comprensión de listas para convertir todas las cadenas a mayúsculas.'''
strings = ['Hola', 'Soy','Una','Lista','de','strings']
mayuscula = [word.upper() for word in strings]
#print(mayuscula)

'''Ejercicio 4: Crear una lista de tuplas
Instrucción: Dada una lista de números, utiliza comprensión de listas para crear una lista de tuplas donde el primer elemento sea el número y el segundo el cuadrado de ese número.'''
numeritos = [54,87,6,32,10,0,78,9998,10247]
numerito_al_cuadrado = []
recorrido = [(num,num**2) for num in numeritos]
#print(recorrido)

'''Ejercicio 5: Filtrar palabras largas
Instrucción: Dada una lista de palabras, usa comprensión de listas para filtrar las que tengan más de 4 caracteres.'''
words_list = ['Soy','Una','Lista','De','Palabras']
filtro_words = [word for word in words_list if len(word) > 4]
#print(filtro_words)

'''Ejercicio 6: Multiplicar elementos de dos listas
Instrucción: Dadas dos listas de números, usa comprensión de listas para crear una nueva lista que contenga el producto de los elementos con el mismo índice de ambas listas.'''
list_num_one = [12,555,98,5,96,6,3,47]
list_num_two = [654,8,9,6,5265,78,20,3,52]
new_list = [x*y for x,y in zip(list_num_one,list_num_two)]
#print(new_list)

'''Ejercicio 7: Extraer números de una cadena
Instrucción: Dada una lista de cadenas, usa comprensión de listas para extraer solo aquellos que contienen números.'''
word_list = ['Hola1','125','es','856','cadena']
solo_num = [string for string in word_list if any(caracter.isdigit() for caracter in string)]
#print(solo_num)

'''Ejercicio 8: Generar una lista de listas
Instrucción: Usa comprensión de listas para crear una lista de listas que contenga los primeros 3 múltiplos de cada número en una lista de números.'''
numbers_list = [12,25,54,9,30,7,85,12]
multiplos_list = [[num * i for i in range(1,4)] for num in numbers_list]
print(multiplos_list)