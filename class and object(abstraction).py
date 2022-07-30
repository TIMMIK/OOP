# en ---> In object-oriented programming , a class is a template definition of the method s and variable s in a particular kind of object . Thus, an object is a specific instance of a class; it contains real values instead of variables. 
# en ---> The class is one of the defining ideas of object-oriented programming.

# ru ---> В объектно-ориентированном программировании класс — это шаблон определения метода s и переменной s в объекте определенного типа. 
# ru ---> Таким образом, объект — это конкретный экземпляр класса; он содержит реальные значения вместо переменных. Класс является одной из определяющих идей объектно-ориентированного программирования.
# создание класса в Питоне
class ClassName:
# функция __init__() нужна для присвоения значений свойствам объекта или других операций, которые необходимо выполнить при создании объекта
# A B S T R A C T I O N
  def __init__(self,name, surname, birth_year):
    self.name = name
    self.surname = surname
    self.birth_year = birth_year
    
  def anyName(self):
    print(f"Ismim {self.name} {self.surname}, {self.birth_year} da tug'ilganman")
    
first = ClassName('Timur','Tursunov',2005)
print(first.anyName())