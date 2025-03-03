'''
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.'''
#Estructuras...
#Listas [] ordenadas, modificables, admite repetidos
lista = [1,3,5,'Andrea','Montevideo',5,5]
#Insertar elementos
lista.append('Amour') #Agrega elemento al final por defecto, de a uno a la vez
lista.insert(0,{'Salutation': 'Bienvenue','Question': 'Ca va?'}) #Agrega al final o según indice especificado, varios a la vez en forma de diccionario u otra lista
#Contar elementos
cantidadItem = lista.count(5) #Devuelve cantidad de veces que aparece el elemento
#Encontrar Indice
indice = lista.index(3) #Devuelve valor del indice donde se encuentra el elemento
#Eliminar elementos
deleteLastItem = lista.pop(2) #elimina último elemento por defecto o según indice especifico, devuelve el elemento eliminado
#lista.remove()
#Ordena elementos
newList = [10,20,55,78,5,1.3,1,7] #creo una lista nueva
newList.sort() #Para que funcione ok deben ser los mismos tipos de datos iterables (int,string)
#Ordenar al reves
listaDeux = ['A','B','C','D','E']
listaDeux.reverse()
#Actualizar elementos
lista[0] = 'Bonjour' #Asignando directamente el valor indicando indice a modificar

'''print(lista)
print(cantidadItem)
print(indice)
print(deleteLastItem)
print(newList)
print(listaDeux)'''

#Diccionarios {key:valor} par clave : valor, no repetidos, ordenados, modificables
my_Dict = {'Salutation':'Bonjour','Questions':'Cooment allez vus?', 'Depart': 'Á plus tard'}
#Actualizar
my_Dict['Salutation'] = 'Salut' #Asignando directamente mediante key
#Eliminar
my_Dict.pop('Salutation') #Delete el par clave : valor mediante key, devuelve error si la key no existe
my_Dict.popitem() #Elimina de forma aleatoria
#Mostrar los items 
newKey = my_Dict.items()

'''print(my_Dict)
print(newKey)'''

#Tuplas () no modificables, iterables, ordenadas, no repetidos
my_Tupla = (5,'Andre', 'Montevideo')
#Acceder
indice = my_Tupla[2]
#Metodos
contar = my_Tupla.count(5) #Identifica numero de veces que aparece el elemento
'''print(my_Tupla.index(5))#Devuleve el indice dele lemento indicado
print(my_Tupla)
print(indice)
print(contar)'''

#Set o conjuntos {} no ordenados, modificables, no repetidos
my_set = {29,'Montevideo',333, True, 29}
for x in my_set:
    print(x)
#Agregar elementos
my_set.add('Bonjour')
#Eliminar elementos
my_set.pop() #elimina elemento aleatorio ya que no tiene un orden establecido
'''print(my_set)'''

#Dificultad extra
my_contacts = {}
#def insert_contact(contact):