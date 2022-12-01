from turtle import penup, fd, rt, lt, pendown


def jump(length_x, length_y):
    penup()
    fd(length_x)
    rt(90)
    fd(length_y)
    lt(90)
    pendown()
