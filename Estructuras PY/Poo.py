# '''/*
#  * EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#  * utilizando su función.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.
#  */'''

# import datetime as dt

# #Iniciando clase
# class Persona:
#     def __init__(self,name: str,age: int,profesion: str,estado: str) -> None: #Inicialización de atributos
#         self.name = name
#         self.age = age
#         self.profesion = profesion
#         self.estado = estado

#     def saludar(self): #Métodos
#         print(f'Hola mi nombre es: {self.name} y soy {self.profesion} ¿Tú cómo te llamas? y A qué te dedicas?')
    
#     def cumpleaños(self):
#         birthday = dt.datetime.now().year - self.age
#         print(f'Mi nacimiento fue en el año {birthday}')

# #Iniciando clase
# class Mascota:
#     def __init__(self, raza,age, tipo, sonido):
#         self.raza = raza
#         self.age = age
#         self.tipo = tipo
#         self.sonido = sonido

#     def sonidos(self):
#         print(f'El {self.tipo} hace: {self.sonido}')


# #Instanciando clase
# mi_gato = Mascota('Siames',8, 'Gato','Miauu')
# mi_gato.sonidos()
# mi_perro = Mascota('Doberman',10,'Perro','Guaou')
# mi_perro.sonidos()

# camila = Persona('Maria',33,'Abogada','Casada')
# #camila.saludar()
# camila.cumpleaños()


'''Ejercicios prácticos de clases en Python:
1. Ejercicio básico: Crear una clase Coche
Define una clase llamada Coche que tenga los siguientes atributos:
marca
modelo
año
color
Y los siguientes métodos:
Un método informar() que imprima todos los detalles del coche (marca, modelo, año y color).
Un método encender() que imprima "El coche está encendido".
Objetivo: Practicar la definición básica de clases y métodos en Python.'''
# #Iniciando clase coche
# class Coche:
#     #Inicializando atributos
#     def __init__(self,marca,modelo,año,color):
#         self.marca = marca
#         self.modelo = modelo
#         self.año = año
#         self.color = color
#         #Definiendo métodos
#     def informar(self):
#             print(f'La marca es {self.marca}, el modelo es {self.modelo}, el año de fabricación es: {self.año} y el color es {self.color}')

#     def encender(self):
#             print('El coche está encendido...\nBrumm Brummm Brumm')

# #Instanciando clase coche
# my_coche = Coche('Escarabajo','W',1850,'Red')
# #my_coche.informar()
# #my_coche.encender()

'''Ejercicio intermedio: Clase Persona
Crea una clase Persona que contenga los atributos:
nombre
edad
email
Además, incluye un método:
saludar() que imprima algo como: "¡Hola! Mi nombre es [nombre] y tengo [edad] años."
Extensión: Puedes agregar un método cumpleaños() que incremente la edad de la persona en 1.'''
# #Iniciando class
# class Person:
#     #Atributos
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email
#     #Métodos
#     def salutation(self):
#         print(f'Bonjour J´mappelle {self.name} et J´ai {self.age} ans')
    
#     def cumpleaños(self):
#         new_age = self.age +1
#         print(new_age)
    
# Juan = Person('Juan',58, 'Juan@yahoo.com')
# Juan.salutation()
# Juan.cumpleaños()

'''Ejercicio avanzado: Clase Banco
Crea una clase CuentaBancaria que permita a los usuarios:
Depositar dinero.
Retirar dinero.
Consultar el saldo.
Cada cuenta debe tener un número de cuenta único, y un método informar() que imprima los detalles de la cuenta (número de cuenta y saldo).
Extensión: Añadir un método de transferencia entre cuentas.'''
class Banco:
    def __init__(self,cuenta,saldo):
        self.cuenta = cuenta
        self.saldo = saldo

    def informar(self):
        print(f'El número de cuenta consultada es: {self.cuenta} y el saldo correspondiente es: {self.saldo}')