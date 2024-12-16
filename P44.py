from os import system
system("cls")
from turtle import *
def square(district):
    for x in range (4):
        fd(float(district))
        lt(90)
for y in range (100,181,20):
    square(district=y)
done()