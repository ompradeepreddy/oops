class Human:
  def eat(self):
    print("i can eat")
  def work(self):
    print("i can work")
class male(Human):
  def run(self):
    print("i can run")
male_1=male()
male_1.run()
male_1.eat()