## Exception Handling ## 

numberOne, numberTwo = 5, 1
numberTwo = "1"

# try except

try:
  print(numberOne + numberTwo)
except:
  print("Se ha producido un error")
  
  
  
  # try except else finally
try:
  print(numberOne + numberTwo)
except:
  # Esto se ejecuta si hay error
  print("Se ha producido un error")
else:
  # Esto se ejecuta si no hay error
  print("La ejecucion continuo correctamente")
finally:
  # Esto se ejecuta siempre
  print('la ejecucion termino')
  
  
  
# Exepciones por tipo
try:
  print(numberOne + numberTwo)
except TypeError: # Solo captura excepciones de tipo TypeError
  print("Se ha producido un error de tipo")
except ValueError: # Solo captura excepciones de tipo ValueError
  print("Se ha producido un error de valor")
  
  
  
#Captura de la informacion del error
try:
  print(numberOne + numberTwo)
except ValueError as error: # Solo captura excepciones de tipo ValueError y caputura el error en la variable e
  print("Se ha producido un error de valor", error)
  