class Human:
  def __init__(self,num_heart):
    self.num_eyes=2
    self.num_nose=1
    self.num_heart=num_heart
  def eat(self):
    print("i can eat")
  def work(self):
    print("i can work")
class male(Human):
  def __init__(self,name,heart):
    super().__init__(heart)
    self.name=name
  def run(self):
    print("i can run")
male_1=male("ram",1)
print(male_1.num_eyes)
print(male_1.num_heart)