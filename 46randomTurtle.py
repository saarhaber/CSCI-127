#Saar Haber
#17 April 2018
#program 46

import turtle
import random

tom = turtle.Turtle()
tom.speed(10)

for i in range(100):
  tom.forward(10)
  a = random.randrange(0,360)
  tom.right(a)


