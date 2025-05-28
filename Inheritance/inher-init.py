class Human:
  def __init__(self):
    self.num_eyes=2
    self.num_nose=1
  def eat(self):
    print("i can eat")
  def work(self):
    print("i can work")
class male(Human):
  def run(self):
    print("i can run")
male_1=male()
print(male_1.num_eyes)