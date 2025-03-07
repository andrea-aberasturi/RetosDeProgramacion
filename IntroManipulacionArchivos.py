#Leer y escribir archivos de textos
#Crear archivos de textos
#with open('My_New_File.txt','x') as file: #Con with el archivo automaticamente se cierra solo luego de ejecutado el código #Creo un archivo flag 'x' crea solo si el archivo no existe, de lo contrario genera un error
 #   file.write('This is an example\nIm been created of Python (:') # write para escribir algún texto dentro del archivo

#with open('My_New_File.txt','r') as file: #Flag 'R' abre el file en modo solo lectura
    #lineas = file.readlines() #Devuleve una lista con cada párrafo como elemento 
    #lineas = file.read() #Devuelve la cantidad de caracteres especificados, si no se especifica devuelve cada oración por separado
    #lineas = file.readline() #Devuelve la primera oración
    #print(lineas)
#with open('My_New_File.txt','w') as file: #Crea un nuevo archivo sin importar si el nombre es el mismo
#
import os #Importo modulo rutas path
directorio_actual = os.path.dirname(__file__)
ruta_relativa = os.path.join(directorio_actual, 'My_Tareas.txt')
#file = open(ruta_relativa, 'r')
# # file = open(ruta_relativa,'a') #Flag 'a' edita y agrega al final
# # file.write('This is a new line\n')
# # file.close()
# file = open(ruta_relativa, 'a')
# file.writelines(['\nThis is a new line with flag "a" ', 'And this also is the new line\n']) #Puedo pasar un iterable que lo inserta todo junto como cadena de texto
# print(file.writable())#metodo booleano true si es editable, false en caso contrario

#Crea un programa que registre tareas en un archivo
#Modificar ejercicio anterior solicitud de tareas en una lista, ahora en un file.txt

#Creo función agregar tareas
def add_tarea(tarea):
    with open(ruta_relativa, 'a+') as file:
        file.write(f'- {tarea}\n')

#Creo function eliminar tarea
def delete_tarea(tarea):
    with open(ruta_relativa, 'w+') as file:
        oraciones = file.readlines() #Divide el archivo en oraciones y devuelve una lista con cada oración como elemento
        tareas = []
        for line in oraciones:#Recorro cada elemento
            if line.strip(' -\n') != tarea.strip(' -\n'):
                tareas.append(line)
                print(tareas)
                add_tarea(tareas)
            else:
                print('La tarea no se encuentra en la lista')


#Creo una function para mostrar tareas por consola print
def view_tarea():
    with open(ruta_relativa,'r') as file:
        view = file.readlines()
        print(f'\n{view}')

            
        
def my_tarea():
    print('---------*Bienvenid@*----------\n------*Indique la opción a realizar*------\n')
    opciones = int(input('1) Agregar Tarea\n2) Eliminar Tarea\n3) Ver tareas pendientes\n4) Salir del programa\n'))
    match opciones:
        case 1:
            tarea = input('Ingrese la tarea a agendar:\n')
            add_tarea(tarea)
        case 2:
            print('Ingrese la tarea a eliminar:\n')
            tarea = input()
            delete_tarea(tarea)
        case 3:
            view_tarea()
        case 4:
            return
        case _:
            print('Opción invalida, ingrese una opción correcta por favor')
    my_tarea()

my_tarea()