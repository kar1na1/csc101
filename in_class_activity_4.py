# -*- coding: utf-8 -*-
"""In_Class_Activity_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fzz6UQjUWIspADy0mw12s8085Jm7-JL4

**Question 1:**
"""

def display_info ():
  print('Title: Percy Jackson, The Lightning Theif')
  print('Author: Rick Riordan')
  print('Publication Year: 2005')
  print('Brief Description:\nTwelve-year-old Percy Jackson, discovers he\'s a demigod and is accused of stealing Zeus\'s lightning bolt.'"\nOn a quest to clear his name, he faces mythological monsters and learns about friendship and his true identity.")



print('My favorite book is:')

display_info()

"""**Question 2:**"""

travel_destinations = 'London, Paris or New York'

def London ():
  print('The London Eye')
  print('The Tower of London')

def Paris ():
  print('The Eiffel Tower')
  print('The Louvre Museum')

def New_York ():
  print('The Empire State Building')
  print('Rockefeller Center')


print('Travel destinations are:')
print(travel_destinations)
print('\nTop 2 attractions are:\n')
print('London:')
London()
print('\nParis:')
Paris()
print('\nNew York:')
New_York()

"""**Question 3:**"""

!pip3 install ColabTurtle
from ColabTurtle.Turtle import *
initializeTurtle()
import ColabTurtle.Turtle as turtle

def draw_square ():
  for i in range(4):
    turtle.forward(100)
    turtle.right(90)
draw_square ()

turtle.penup()
turtle.goto (200,250)
turtle.pendown()
draw_square ()

turtle.penup()
turtle.goto (600,250)
turtle.pendown()
draw_square ()

"""**Question 4:**"""

def find_even_numbers():
  for i in range(0,11):
    if i % 2 == 0:
      print(i)

print('Even Numbers between 0 and 10 are:')
find_even_numbers()