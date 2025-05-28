class Rectangle:
  def __init__(self,length,width):
    self.length=length
    self.width=width
    self.area=length*width
  #def area_rec(self):
   # return self.length*self.width
rec_1=Rectangle(5,10)
print(rec_1.area)