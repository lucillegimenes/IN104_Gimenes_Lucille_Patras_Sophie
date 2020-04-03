class Person:
  def __init__(self,name,age,nationality):
    self.name=name
    self.age=age
    self.nationality=nationality
class Child(Person):
  def __init__(self, school, favorite_color):
    self.school=school
    self.favorite_color=favorite_color
  def school(self):
    print("I go to",self.school)
  def presentation(self)
    print("Hello my name is",self.name,"I'm",self.age,"years old and my favorite color is",self.favorite_color) 
  
class Adult(Person):
  def __init__(self, job, bank_account):
    self.job=job
    self.bank_account=bank_account
  def working(self)
    print("I work as a",self.job)
  def money(self)
    print("My bank account is",bank_account)
    
#main
if __name__ == '__main__':
  Robert=Adult.Person('Robert',40,'American')
  Leo=Child.Person('Leo',7,'British')
  Robert.working
  Robert.money
  Leo.school
  Leo.presentation
