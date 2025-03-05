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
ruta_relativa = os.path.join(directorio_actual, 'My_New_File.txt')
# file = open(ruta_relativa,'a') #Flag 'a' edita y agrega al final
# file.write('This is a new line\n')
# file.close()
file = open(ruta_relativa, 'a')
file.writelines(['\nThis is a new line with flag "a" ', 'And this also is the new line\n']) #Puedo pasar un iterable que lo inserta todod junto como cadena de texto
print(file.writable())#metodo booleano true si es editable, false en caso contrario