import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.hat = kwargs
    self.contents = []
    self.replace_contents = []
    for color in self.hat:
      quantity = self.hat[color]
      for i in range(quantity):
        self.contents.append(color)
        self.replace_contents.append(color)
    
  def draw(self,draws):
    draw = []
    if draws > len(self.contents) - 1:
      self.contents = copy.copy(self.replace_contents)
    if draws > len(self.replace_contents) - 1:
      return self.contents
    for i in range(draws):
      random_num = random.randint(0,len(self.contents) - 1)
      draw.append(self.contents.pop(random_num))
      
    return draw  

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  expected_balls_list = []
  successful_draws = []
  successful_draw_length = len(expected_balls_list)
  for color in expected_balls:
    quantity = expected_balls[color]
    for i in range(quantity):
      expected_balls_list.append(color)
  for i in range(num_experiments):
    balls_drawn = hat.draw(num_balls_drawn)
    for ball in expected_balls_list:
      try:
        successful_draws.append(balls_drawn.pop(balls_drawn.index(ball)))
      except ValueError:
        pass
    if len(successful_draws) == len(expected_balls_list):
      success += 1
    successful_draws = []
    
  return success / num_experiments