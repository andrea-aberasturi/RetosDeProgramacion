'''/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */'''

class Persona:
    def __init__(self,name,age,profesion,estado):
        self.name = name
        self.age = age
        self.profesion = profesion
        self.estado = estado

    def saludar(self):
        print(f'Hola mi nombre es: {self.name} y soy {self.profesion} ¿Tú cómo te llamas? y A qué tededicas?')


class Mascota:
    def __init__(self, raza,age, tipo, sonido):
        self.raza = raza
        self.age = age
        self.tipo = tipo
        self.sonido = sonido

    def sonidos(self):
        print(f'El {self.tipo} hace: {self.sonido}')



mi_gato = Mascota('Siames',8, 'Gato','Miauu')
mi_gato.sonidos()
mi_perro = Mascota('Doberman',10,'Perro','Guaou')
mi_perro.sonidos()