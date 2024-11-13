## clases ## 

class MyEmptyPerson:
  pass


class Person:
    def __init__(self, name, surname, age, gender, alias= "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"
        self.age = age
        self.gender = gender
        
    def walk(self):
      print(f'{self.full_name} Esta caminando')
     
my_person = Person("Luis", "Garcia", 23, "Masculino")
print(f"{my_person.full_name} {my_person.age} {my_person.gender}")
my_person.walk()

my_other_person = Person("Brais", "Moure", 23, "Masculino", "El piti")
print(f"{my_other_person.full_name} {my_other_person.age} {my_other_person.gender}")
my_other_person.walk()

#Tambien podemos reasignar los atributos de la clase
# my_other_person.full_name = "Luis Garcia"