## Funciones ## 

def my_function ():
  print('Hello World')
  
my_function ()

def sum_two_values(a, b): # funcion con argumentos que no retorna nada
  print(a + b)
  
sum_two_values(1, 2)

def sum_two_values_with_return(a, b): # funcion que retorna un valor
  return a + b

result = sum_two_values_with_return(1, 2)
print(result)

def print_name(name, last_name): # Recibir argumentos
  print(f"{name} {last_name}")
  
print_name(last_name="Moreira", name="Kevin")


def print_name_with_default(name, alias="Garciase"): # Establecer un valor por defecto
  print(f"{name} {alias}")
  
print_name_with_default("Kevin") 

def print_texts(*text): # pasar infinitos argumentos
  print(text)
  
print_texts("Hello World", "Pija")

def mayus_texts(*texts): # pasar infinitos argumentos
  for text in texts:
    print(text.upper())
    
mayus_texts("Hello World", "Pija")
  