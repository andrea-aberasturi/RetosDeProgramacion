'''* EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.'''
#Funciones sin parametros y sin return
def myFunction():
    print('Hello world')
myFunction()
#Funciones sin parametros con return
def myFunctionReturn():
    return 'Bonjour Monde'
#print(myFunctionReturn())
#Function con parametros y sin return
def myFunctionParam(num1,num2):
    print(f'My firstnumber is: {num1} and my second number is: {num2}')
#myFunctionParam(5,7)
#Function con param y return
def myFunctionParamReturn(charact):
        return charact.split()
#print(myFunctionParamReturn('Soy una cadena de texto'))
'''DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.'''
def functions(param1,param2):
       num = 0
       for i in range(1,101):
            if i % 3 == 0 and i % 5 == 0:
                print(f'{str(param1+param2)}')
            elif i % 3 == 0:
                 print(f'{param1}')
            elif i % 5 == 0:
                 print(f'{param2}')
            else:
                 num +=1
                 print(i)
            print(f'Cantidad de veces que no hay coincidencia {num}')
            return num
#functions('Fizz','Buzz')

def my_arguments(**arg):
     for i, x in arg.items():
          print(f'Hola {i} {x}')

my_arguments(
     Name= 'Andrea',
     Age= 29,
     Langues = 'French'
     )