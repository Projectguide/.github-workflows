class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Pooja", "Dave")
x.printname()
y=10
print(y)

class Student(Person):
  pass
x = Student("Mike", "Dison")
x.printname()
y=20
print(y)