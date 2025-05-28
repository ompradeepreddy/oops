class instructor:
  def __init__(self,name,address):
    self.name=name
    self.address=address
  def display(self,subject_name):
    print(f"Hello i am {self.name} i will teach {subject_name}")
instructor_1=instructor("ram","ap")
instructor_2=instructor("raj","up")
print(instructor_1.name)
instructor_1.display("python")