class instructor:
  def __init__(self,name,address):
    self.name=name
    self.address=address
  def display(self):
    print("Hello")
instructor_1=instructor("ram","ap")
instructor_2=instructor("raj","up")
instructor_1.display()
print(instructor_1.name)