# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

#temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
 #                 14.7, 19.6, 11.2, 18.4]


temp_dataloger = [9, 10, 13.9, 12, 12.1, 11.2, 13.5, 11.6,
                  10.7, 12.6, 11.2, 13.4]



# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
En este ejercicio se lo provee de una lista de temperaturas,
esa lista de temperaturas corresponde a los valores de temperaturas
tomados durante una temporada del año en Buenos Aires.
Usted deberá analizar dicha lista para deducir
en que temporada del año se realizó el muestreo de temperatura.
La variable con la lista de temperaturas se llama "temp_dataloger"
definida al comienzo del archivo

Debe recorrer la lista "temp_dataloger" y obtener los siguientes
resultados

1 - Obtener la máxima temperatura
2 - Obtener la mínima temperatura
3 - Obtener el promedio de las temperaturas

Los resultados se deberán almacenar en las variables
que ya hemos preparado para usted al comienzo del ejercicio

NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
el máximo y el mínimo utilizando los mismos métodos vistos
durante la clase (ejemplos_clase/ejemplo_5.py)
'''

print("Mi primer pasito en data analytics")
# Empezar aquí la resolución del ejercicio

temperatura_max = None      # Aquí debe ir almacenando la temp máxima
temperatura_min = None      # Aquí debe ir almacenando la temp mínima
temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

# Colocar el bucle aqui......
temperatura_max = temp_dataloger[0]
temperatura_min = temp_dataloger[0]

for i in temp_dataloger:

    if(i > temperatura_max):
        temperatura_max = i

    if(i < temperatura_min):
        temperatura_min = i

    temperatura_sumatoria += i


# Al finalizar el bucle compare si el valor que usted calculó para
# temperatura_max y temperatura_min coincide con el que podría calcular
# usando la función "max" y la función "min" de python
# función "max" --> https://www.w3schools.com/python/ref_func_max.asp
# función "min" --> https://www.w3schools.com/python/ref_func_min.asp

if(temperatura_max == max(temp_dataloger)):
    print('Se verifica que la temperatura {} es la maxima'.format(temperatura_max))

if(temperatura_min == min(temp_dataloger)):
    print('Se verifica que la temperatura {} es la minima'.format(temperatura_min))

# Al finalizar el bucle debe calcular el promedio como:
temperatura_len = len(temp_dataloger)
temperatura_promedio = round(temperatura_sumatoria / temperatura_len, 2)
print('La temperatura promedio es: {}'.format(temperatura_promedio))
# Corroboren los resultados de temperatura_sumatoria
# usando la función "sum"
# función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

if(temperatura_sumatoria == sum(temp_dataloger)):
    print('La sumatoria de temperaturas se ha verificado correctamente')

'''
Una vez que tengamos nuestros valores correctamente calculados debemos
determinar en que epoca del año nos encontramos en Buenos Aires utilizando
la estadística de años anteriores. Basados en el siguiente link realizamos
las siguientes aproximaciones:

verano -->      min = 19, max = 28
otoño -->       min = 11, max = 20
invierno -->    min = 8, max = 14
primavera -->   min = 10, max = 24

Referencia:
https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
'''

# En base a los rangos de temperatura de cada estación,
# ¿En qué época del año nos encontramos?
# Imprima el resultado en pantalla
# Debe utilizar temperatura_max y temperatura_min para definirlo
if(temperatura_min > 19 and temperatura_max < 28):
    print('La epoca del año es verano')

if(temperatura_min > 11 and temperatura_max < 20):
    print('La epoca del año es otoño')

if(temperatura_min > 8 and temperatura_max < 14):
    print('La epoca del año es invierno')

if(temperatura_min > 10 and temperatura_max < 24):
    print('La epoca del año es primavera')