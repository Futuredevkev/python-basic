## Conditionals ##


my_condition = True 

if my_condition:
  print("Se ejecuta la condición del if")
  
  my_condition = 5 * 3
  
  if my_condition == 10:  
    print('Se ejecuta la condi')
    
  if my_condition > 10 and my_condition < 20:
      print('Es mayor que 10 y menor que 20') # si cumple esto va por aca
  elif my_condition == 1:
      print('Es igual a 1') # Si cumple este caso especial va por aca 
  else:
      print('Es menor que 10 ') # O si no cumple ninguna lanza por aca.
  
  print("La ejecución continua")
  
  
  
  my_string = ""
  
  if not my_string: # Aca estamos negando una condicion.
    print('Mi cadena de texto es vacia')
  
  if my_string == "Mi cadena de texto": # Aca lo va a imprimir porque esta el texto
    print('Estas cadenas de texto coiniciden')
  
  #ACLARACION TODO LO QUE TABULADOS CONSIDERA QUE ESTA DENTRO DEL IF O ELSE, Y LO QUE DEJAMOS DE TABULAR LO CONSIDERA OTRO BLOQUE 