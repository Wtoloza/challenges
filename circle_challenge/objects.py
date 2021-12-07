class Circle:
  """
  Circle maker
  """

  def __init__(self, radious, center=(0,0)):
    self.radious = radious
    self.x_0, self.y_0 = center
  
  def __str__(self):
    return f'Circle -> radious:{self.radious}, center:{self.x_0},{self.y_0} '

class Point:
  """
  Point maker
  """
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __str__(self):
    return f'Point -> x:{self.x}, y:{self.y}'