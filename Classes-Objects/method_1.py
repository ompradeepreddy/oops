class instructor:
  def __init__(self,name,address):
    self.name=name
    self.address=address
  def display(self):
    print(f"Hello i am {self.name}")
instructor_1=instructor("ram","ap")
instructor_2=instructor("raj","up")
print(instructor_1.name)
instructor_1.display()