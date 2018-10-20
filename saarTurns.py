#name Saar Haber
#date 22 February 2018
#A program that asks the user for 5 whole (integer) numbers.
#   For each number, turn the turtle left
#    the degrees entered and then the turtle should move forward 100.

import turtle

tom = turtle.Turtle()

for i in range (5):
    m=input("Enter a number ")
    tom.left(int(m))
    tom.forward(100)
