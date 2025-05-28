class circle:
  pi=3.14
  def __init__(self,radius):
    self.radius=radius
  def circumference_circle(self):
    return 2* circle.pi *self.radius
  def area_circle(self):
    return circle.pi * (self.radius)**2
circle_1=circle(5)
print(circle_1.circumference_circle())
print(circle_1.area_circle())