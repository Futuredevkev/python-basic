## LISTS ## 

my_list  = list()
my_other_list = []

my_list = [30, 40, 50, 60 , 35]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Braisi", "Noure"]

print(my_other_list[0]) # Acceder a un elemento de la lista
print(my_other_list[1]) # Acceder a un elemento de la lista
print(my_other_list[-1]) # Acceder al ultimo elemento de la lista
print(my_other_list.count("Braisi")) # Contar las veces que aparece un elemento de la lista

my_other_list.append("Luis") # Agregar un elemento a la lista al final
print(my_other_list)

my_other_list.insert(0, "Luis") # Agregar un elemento a la lista en una posicion especifica
print(my_other_list)

my_other_list.remove("Luis") # Eliminar un elemento de la lista
print(my_other_list)

del my_other_list[0] # Eliminar un elemento de la lista en una posicion especifica
print(my_other_list)

my_other_list.pop() # Eliminar el ultimo elemento de la lista
print(my_other_list)

my_pop_element = my_list.pop(2) # Eliminar un elemento de la lista en una posicion especifica
print(my_pop_element)
print(my_list)

my_other_list.sort() # Ordenar una lista
print(my_other_list)

my_other_list.reverse() # Invertir una lista
print(my_other_list)

my_other_list[0] = 100 # Modificar un elemento de la lista
print(my_other_list)

my_new_list = my_other_list.copy() # Copiar una lista
print(my_new_list)


age, height, name, surname = my_other_list # Desempaquetar una lista
print(age, height, name, surname)

my_list = "Hello World"

#Hacer sublistas de una lista
sub_list = my_list[1:4] # Desde la posicion 1 hasta la 4
print(sub_list)