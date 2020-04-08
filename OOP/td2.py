
class Person:
  def __init__(self,name,age,nationality):
    self.name=name
    self.age=age
    self.nationality=nationality
class Child(Person):
  def __init__(self,school,favorite_color):
    self.school=school
    self.favorite_color=favorite_color
  def whichSchool(self):
    print("I go to",self.school)
  def presentation(self):
    print("My favorite color is",self.favorite_color) 
  
class Adult(Person):
  def __init__(self,job,nb_children):
    self.job=job
    self.nb_children=nb_children
  def working(self):
    print("I work as a ",self.job)
  def children(self):
      print("I have",self.nb_children,"children")
    

if __name__ == '__main__':
  Robert=Person("Robert",40,'American')
  Leo=Person('Leo',7,'British')
  Robert=Adult("Teacher",3)
  Leo=Child("The Great School", "blue")
  Robert.working()
  Robert.children()
  Leo.presentation()
  Leo.whichSchool()
