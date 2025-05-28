class instructor:
  followers=0
  def __init__(self,name,address):
    self.name=name
    self.address=address
  def display(self,subject_name):
    print(f"Hello i am {self.name} i will teach {subject_name}")
  def update_followers(self,followers_name):
    self.followers+=1
instructor_1=instructor("ram","ap")
instructor_2=instructor("raj","up")
print(instructor_1.name)
instructor_1.display("python")
instructor_1.update_followers("raj")
print(instructor_1.followers)
instructor_2.update_followers("raj")
print(instructor_2.followers)