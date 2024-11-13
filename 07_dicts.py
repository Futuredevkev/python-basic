## Dicts a diferencia de sets y tuples los diccionarios son mutables y tienen la representacion parecida a un json ##

my_dict = dict()
my_other_dict = {}

print(type(my_dict))

my_other_dict =  {"name": "Luis", "last_name": "Garcia", "age": 23, 1: "Python"}

my_dict = {
  "name": "Luis", "last_name": "Garcia", "age": 23, "Lenguajes": {"Python", "Java", "C++"},
  1:1.77
      
}

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["name"]) # Entrar a ver el valor de una clave 

my_dict["name"] = "Brais" # Cambiar el valor de una clave
print(my_dict["name"])

my_dict["Colores"] = {"Rojo", "Azul", "Verde"} # Agregar una nueva clave
print(my_dict)

del my_dict["Colores"] # Eliminar una clave
print(my_dict)

print("Python" in my_dict["Lenguajes"]) # Comprobar si una clave existe
print("name" in my_dict) # Comprobar si una clave existe
print("Python" not in my_dict["Lenguajes"]) # Comprobar si una clave no existe

print(my_dict.items()) # Devuelve una lista de tuplas
print(my_dict.keys()) # Devuelve una lista de claves
print(my_dict.values()) # Devuelve una lista de valores

my_new_dict = dict.fromkeys(("name", 1, "Piso")) # Crea un nuevo dict con las claves especificadas, para mas adelante podemos asignarle un valor
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) # Crea un nuevo dict solo con las claves de my_dict completo original, ESTO SI PUEDE SER MUY UTIL, despues ya te encargas vos de meter datos o hacer lo que sea.
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict, ("Brais", "Moure")) # Añadimos valos predefinidos a todas las claves
print(my_new_dict)