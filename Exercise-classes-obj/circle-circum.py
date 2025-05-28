class circle:
  pi=3.14
  def __init__(self,radius):
    self.radius=radius
  def circumference_circle(self):
    return 2* circle.pi *self.radius
circle_1=circle(5)
print(circle_1.circumference_circle())
