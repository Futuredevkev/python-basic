## tuples a diferencia con list los tuplas son inmutables ##

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "brais")

print(my_tuple)
print(len(my_tuple))

print(my_tuple.count(35)) # Contar la cantidad de veces que aparece un elemento
print(my_tuple.index(1.77)) # Buscar la posicion de un elemento

# del my_tuple # Eliminar la tupla, esto se hace pero elimina la variable directamente, no se puede eliminar un item en concreto
# my_tuple[1] = "luis" #Esto no se puede hacer, No se puede modificar la tupla