'''* EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.'''
#Ejemplos operadores Python
#Asignación
num1 = 7
num2 = 9
#Aritméticos
suma = num1 + num2
resta = num2 - num1
division = num1 / num2
multiplicacion = num2 * num1
resto = num1 % num2
#Lógicos
if num2 and num1 !=0:
    print('Num valid')
elif num1 or num2 <5:
    print('Alguno de los números es menor a cinco')
else:
    print('error')
#Comparación, también se puede agregar <=(menor o igual que) >=(mayor o igual que) o != (distinto que)
def mayor_que(num1,num2):
    if num1 > num2:
        print(f'El {num1} es mayor que {num2}')
    elif num1 == num2:
        print('Ambos números son iguales')
    elif num1 < num2:
        print(f'El número {num1} es menor que el número {num2}')
#Identidad is, not is
lambda_function = lambda num1, num2 : num1*num2 if num2 is num1 else num1/num2
#Pertenencia in, not in
frutis = ['Banana', 'Frutilla', 'Manzana']
contiene_Frutila = 'Frutilla' in frutis #Si está devuelve true de lo contrario sería false
no_contiene_Manzana = 'Manzana' not in frutis # Si está devuelve false, contrario true
print(contiene_Frutila, no_contiene_Manzana)
#Estructuras de control
#Condicionales if, elif, else
cars = ['Wolst', 'Ferrari','Lamborgini']
if 'Ferrari' in cars:
    print(cars)
else:
    print('Does´t not exists')
#Iteradores for in, while
#for
names = ['Pablo', 'Milagros','Micaela','Guillermo', 'Losno']
for name in names:
    print(f'Mi compañere se llama: {name}')
#while
count = 0
range = 5
while count < range:
    count += 1
    print(count)
#excepciones
def numbers(x,y):
    try:
        result = x//y
        print(result)
    except:
        print('Imposible divided by zero')
numbers(10,2)
#Plus
'''DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.'''
for i in range(10, 56):
    if i %2 == 0 and i !=16 and i %3 != 0 :
      print(i)
