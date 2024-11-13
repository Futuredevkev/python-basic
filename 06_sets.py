## Sets, la diferencia con los tuples es que los sets no son ordenados y no se pueden duplicar los items dentro, tambien son mutables los sets  ## 

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Brais", "Moure", 1.77}

print(type(my_other_set)) # Imprime el tipo de dato de my_other_set)

print(len(my_other_set)) # Imprime la longitud de my_other_set

# print(my_other_set[0]) # Esto no se puede hacer porque my_other_set es un set

my_other_set.add("Luis") 
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Luis") 
print(my_other_set) # Un set no admite elementos duplicados 

#Comprobar que un elemento existe en el set
print("Luis" in my_other_set)

#Comprobar que un elemento no existe en el set
print("Luis" not in my_other_set)

my_other_set.remove("Luis") # Eliminar un elemento del set
print(my_other_set)

my_other_set.clear() # Eliminar todos los elementos del set
print(my_other_set)

my_set = {"Brais", "Moure", 1.77}

my_other_set = {"Brais3", "Moure33", 1.72}

my_new_set = my_set.union(my_other_set).union({"Luisito"}) # Unir dos sets y tambien se puede agregar un item
print(my_new_set)

print(my_new_set.difference(my_set)) # Diferencia entre dos sets, devuelve los elementos que estan en my_new_set pero no en my_set
