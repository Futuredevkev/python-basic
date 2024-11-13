## loops ## 



#WHILE Mientras la condicion sea menor a 10 el codigo se repite

my_condition = 0

while my_condition < 10: 
  print(my_condition)
  my_condition += 1 
else: 
  print('Mi condicion es mayor o igual a 10')
  
  while my_condition < 20: 
    my_condition += 1
    if my_condition == 15: # podemos poner if dentro del while
      print('se ddetiene la ejecucion')
      break # Esto detiene la ejecucion
    
    
    
    
    # For lo que hace es recorrer un conjunto de datos
  
    my_list = [1, 2, 3, 4, 5]
    
    for element in my_list:
      print(element)
    
    
    my_dict = {
   "name": "Luis", "last_name": "Garcia", "age": 23, "Lenguajes": {"Python", "Java", "C++"},
   1:1.77
      
  }
    
    for element in my_dict:
      print('a', element)
      if element == "age": # podemos poner if dentro del for
        break # Esto detiene la ejecucion
    else: 
      print('el bucle for a finalizado')

    my_set = {"Brais", "Moure", 1.77}

    for element in my_set:
      print('a2', element)
    else: 
      print('el bucle for a finalizado')

    my_tuple = (35, 1.77, "brais")
    
    for element in my_tuple:
      print('a3', element)
    else: 
      print('el bucle for a finalizado')