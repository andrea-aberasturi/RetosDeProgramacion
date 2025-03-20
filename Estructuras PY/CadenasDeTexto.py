''' * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas'''
#Operaciones con strings
character = 'esto es una cadena de caracteres A\tL\tG\tU\tN\tA\tS PALABRAS EN MAYUSCULAS o que Comienzan Con Mayuscula'
print(character)
#Método capitalize hace que la primer palabra comience con mayuscula
first_word = character.capitalize()
#print(first_word)
#Método casefold hace que el string se pase a minusculas por completo
words_lower = character.casefold()
#print(words_lower)
#Método center recibe como argumento el ancho deseado del string, más el caracter de relleno (opcional) y rellena o corta para cubrir dicha longitud especificada con ese caracter
word_center = character.center(500, '-')
#print(word_center)
#Método count devuelve el número de veces que aparece la cadena o subcadena tomada por argumento, es case sensitive: distingue mayusculas de minusculas
word_count = character.count('e')
#print(word_count)
#Método encode devuelve bytes recibe como parametro el formato de codificación (si no se especifica utiliza el por defecto utf-8) y errorr para identificar posibles errores 
word_encode = character.encode(encoding="ascii",errors="namereplace")
#print(word_encode)
#Método endswith devulve True si el final coincide con la cadena o letra que recibe por parametro 
word_final = character.endswith('scula')
#print(word_final)
#Método expandtabs devuelve una copia del string con el espaciado indicado, si no se especifica devuelve el string igual que el original, el string debe tener caracteres de tabulación como \n o \t
word_expand = character.expandtabs(2)
#print(word_expand)
#Método find devuelve el indice del string pasado por parametro
word_find = character.find('AYUS')
#print(word_find)
#Método format devuelve un string segun los caracteres formateados especificos, desde la actualización de las f-string perdio utilidad
new_characters = 'Esto es una nueva CADENA DE TEXTO con elementos: {0} particulares: {1} '
word_formato = new_characters.format('primer elemento', 253)
#print(word_formato)
#Método format.map() similar al anterior solo que en vez de recibir como parametros elementos individuales se le debe asignar un diccionario como argumento
historia = 'Hola mi nombre es: {Name} y mi apellido es: {LastName}'
my_dict = {
    'Name': 'Andrea',
    'LastName': 'Smith'}
word_formato_map = historia.format_map(my_dict)
#print(word_formato_map)
#Método index devuelve el indice de la primera coincidencia sin importar si esta dentro de una palabra o es una palabra concreta
word_index = character.index('es')
#print(word_index)
#Método isalnum devuelve un booleano True si es número o False si no es número
word_number = character.isalnum()
#print(word_number)
#Método isalpha devuelve booleano, True si es strin alfabetico (solo letras sin espacios u otros caracteres) o False si no es string alfabetico
alfabeto = 'sdsfdsfdsdsfd.._'
word_string = alfabeto.isalpha()
#print(word_string)
#Método isascii() booleano devuelve True si el string cumple el formato ascii (letras, núm, alfabeto ingles, español, no chino o figuras)
word_ascii = character.isascii()
#print(word_ascii)
#Método identifier booleano devuelve True si el string cumple con las reglas de nomenclatura python para nombre de variables
word_identifier = character.isidentifier()
#print(word_identifier)
#Método booleano devuelve True si son todo minusculas o False si no
word_loweer = character.islower()
#print(word_loweer)
#Método isnumeric() booleano devuelve True si contiene solo int números o False
numeric_string = '125sadad'
word_numeric = numeric_string.isnumeric()
#print(word_numeric)
#Método isprintable() booleano devuelve True si cumple los requisitos para ser impreso por consola sin problemas de visualización o False si tiene caracteres conflictivos
word_print = numeric_string.isprintable()
#print(word_print)
#Método isspace() booleano devuelve True si el string es solo de espacios
word_space = character.isspace()
#print(word_space)
#Método booleano devuelve True si el string tiene formato title, es decir, comienza con mayuscula o False si tiene solo espacios o no cumple la condición
word_title = character.istitle()
#print(word_title)
#Método isupper booleano devuelve True si es todo en mayuscula o False caso contrario
mayuscula = 'MAYUSCULA'
word_upper = mayuscula.isupper()
#print(word_upper)
#Método join recibe como argumento un string y lo anexiona a la cadena en formato de separación devuelve el resultado
words = '   ¡OpaaA,,,,,,Tengo....VARIOS______Caracteres----!'
word_join = character.join(words)
#print(word_join)
#Método ljust()recibe como parametro longitud (obligatorio) y el caracter que se le quiera agregar segun esa longitud, por defaul es el espacio(opcional)
word_just = words.ljust(20,'!')
#print(word_just)
#Método lower, retorna una copia del string todo en minuscula
word_lowerrr = words.lower()
#print(word_lowerrr)
#Método lstrip () devuelve una copia del string sin espacios de más (adelante), también recibe opcional el/los caracter/es que se quiere/n eliminar (siempre que aparezcan al inicio unicamente)
word_lstrip = words.lstrip(' ¡')
#print(word_lstrip)
#Método maketrans() se utiliza en conjunto con el método translate(), recibe dos argumentos el primero: string a intercambiar y el segundo: por el strin que se quiere modificar
word_maketrans = str.maketrans('O', 'A')
new_word = words.translate(word_maketrans)
#print(new_word)
#Método partition devuelve una tupla con la divición en tres partes según el string especificado :
#Parte Anterior (Before): Es la parte de la cadena antes de la primera aparición de la subcadena especificada.
#Subcadena (Separator): Es la propia subcadena especificada.
#Parte Posterior (After): Es la parte de la cadena que sigue a la primera aparición de la #subcadena especificada
word_partition = words.partition(',')
#print(word_partition)
#Método
#words.removeprefix()

#DIFICULTAD EXTRA (opcional):
'''* Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas'''
def my_program():
    word_one = input('Indica una palabra:\n')
    word_two = input('Indica otra palabra:\n')
    if word_one == word_one[::-1]:
        print(f'La palabra {word_one} es palindroma!')
        if word_two == word_two[::-1]:
            print(f'La palabra {word_two} es palindroma!')
    else:
        print('Lo siento ninguna de las palabras ingresadas cumplen con la condición!')
my_program()