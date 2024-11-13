## Variables ## 

# Inter 
a = 1
b = 2
print(a + b)

#String
name = 'Luis'
last_name = 'Garcia'
print(name + ' ' + last_name)

#Float
float_variable = 1.1
print(type(float_variable))

#List
list_variable = [1, 2, 3]
print(list_variable)

#Tuple
tuple_variable = (1, 2, 3)
print(tuple_variable)

#Dictionary
dict_variable = {'name': 'Luis', 'last_name': 'Garcia'}
print(dict_variable)

#Boolean 
bool_variable = True
print(bool_variable)


## Funciones del sistema ##

# Convierte un numero a string
number_variable = 1  
converter_variable = str(number_variable)
print(type(converter_variable))

#ver el lenght de una variable
print(len(converter_variable))

#Recibiendo parametros 
print('Last name length: ' + str(len(last_name)))

#Variables en una sola linea 
name, last_name, age = 'Luis', 'Garcia', 25
print('Me llamo ' + name + ' ' + last_name + ' y tengo ' + str(age) + ' de edad')

#Inputs 
name = input('What is your name? ') 
age = input('What is your age? ')

print('My name is ' + name + ' and I am ' + age + ' years old')

#¿Forzar un tipo de variable? entre comillas, lo hacemos para el visual de nosotros y darnos cuenta que tipo estamos usando, pero el tipado no es estricto
address : str = 'Calle 1' 