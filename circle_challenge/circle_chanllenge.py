from objects import Circle, Point
from clean_console import clear_console

def change_circle_center():
  """
  Function to change circle center
  """
  clear_console()
  validate = True
  while validate:
    try:
      print('No: 0, Sí:1')
      question = input('¿Desea cambiar el centro del círculo?: ')

      if question == '1':
        x_0 = input('Ingrese el centro en coordenada x: ')
        y_0 = input('Ingrese el centro en coordenada Y: ')
        return (int(x_0), int(y_0))
        
      else:
        clear_console()
        print('El centro del círculo por defecto es (0,0)')
        return (0,0)
      
    except:
      print('Coordenadas no válidas')
      clear_console()


def point_in_circle(point, circle):
  """
  Function to recive a point and cicle
  and retun true if the point is inner on a cirle
  """

  # Normlice center:
  x = abs(point.x - circle.x_0)
  y = abs(point.y - circle.y_0)
  hyp = (x*x + y*y)**0.5
  if hyp < circle.radious:
    return (True, "ESTÁ")
  else:
    return (False, "NO ESTÁ")

def run():
  validate = True
  while validate:
    try:
      x = int(input('Ingrese coordenada en X: '))
      y = int(input('Ingrese coordenada en Y: '))  
      radious = float(input('Ingrese el radio del círculo: '))
      center = change_circle_center()
      validate = False
    except:
      print('Falló')
      clear_console()
  
  circle = Circle(radious, center)
  point = Point(x, y)
  is_in = point_in_circle(point, circle)
  clear_console()
  print(point)
  print(circle)
  print(f'El punto {is_in[1]} en el círculo')

if __name__ == '__main__':
  run()