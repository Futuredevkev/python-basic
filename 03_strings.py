## Strings ## 

my_string = 'Hello World'
my_other_string = "Hello World2"


print(my_string + ' ' + my_other_string) # Concatenacion

my_new_line_string = "Este es un string con salto de linea \n jajajajaja" # Salto de linea
print(my_new_line_string)

my_new_tab_string = "Este es un string con tabulacion \t jajajajaja" # Tabulacion
print(my_new_tab_string)

my_scape_string = "\\tEste es un string con escape \n jajajajaja" # Escape \\
print(my_scape_string)


# Formateo 

name, last_name, edad = 'Luis', 'Garcia', 23

# Sin format 
print('Mi nombre es %s %s y tengo %d anos' % (name, last_name, edad))

#Con format 
print('Mi nombre es {} {} y tengo {} anos'.format(name, last_name, edad))

#Inferencia de datos 

print(f'Mi nombre es {name} {last_name} y tengo {edad} anos') 

## Desempaquetado de caracteres ##
language = 'Python'
a, b, c, d, e, f = language
print(a, b, c, d, e, f)


## Division 

language_slice = language[1:3] # Desde la posicion 1 hasta la 3
print(language_slice)

language_slice = language[1:] # Desde la posicion 1 hasta el final
print(language_slice)

language_slice = language[:3] # Desde la posicion 0 hasta la 3
print(language_slice)

language_slice = language[:] # Desde la posicion 0 hasta el final
print(language_slice)

first_slice = language[0] # Imprime el primer caracter de la cadena
print(first_slice)

lastone_slice = language[-1] # Imprime el ultimo caracter de la cadena
print(lastone_slice)

reversed_slice = language[::-1] # Imprime la cadena al reves
print(reversed_slice)


# Funciones 

print(len(my_string)) # Longitud de la cadena
print(my_string.upper()) # Convierte a mayusculas
print(my_string.lower()) # Convierte a minusculas
print(my_string.capitalize()) # Convierte la primera letra a mayuscula
print(my_string.count('l')) # Conta las veces que aparece la letra
print(my_string.replace('l', 'p')) # Reemplaza la letra por otra
print(my_string.split(' ')) # Divide la cadena en una lista separada por espacios
print(my_string.isnumeric()) # Comprueba si la cadena es numerica 
print(my_string.upper().isupper()) # Comprueba si la cadena es mayuscula
print(my_string.strip()) # Elimina los espacios en blanco al principio y al final
print(my_string.lstrip()) # Elimina los espacios en blanco al principio
print(my_string.rstrip()) # Elimina los espacios en blanco al final
print(my_string.endswith('d')) # Comprueba si la cadena termina con la letra
print(my_string.startswith('H')) # Comprueba si la cadena empieza con la letra
print(my_string.find('l')) # Busca la posicion de la letra
print(my_string.join(' ')) # Junta la cadena con el caracter especificado

