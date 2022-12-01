from random import randrange
from turtle import penup, setpos


def set_position(margin_x, margin_y):
    penup()
    x = randrange(-margin_x, margin_x)
    y = randrange(-margin_y, margin_y)
    setpos(x, y)
    return x, y
