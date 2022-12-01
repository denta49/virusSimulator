from turtle import seth, penup, setpos, color, begin_fill, pendown, fd, rt, end_fill

from visuals.background.create_message_field import create_message_field

background_height = 90
background_color = 'silver'


def background(margin_x, margin_y):
    seth(background_height)
    penup()
    setpos(-margin_x - 10, -margin_y - 10)
    color(background_color)
    begin_fill()
    pendown()

    for i in range(20):
        fd(20 + margin_y * 2)
        rt(90)
        fd(20 + margin_x * 2)
        rt(90)

    end_fill()
    penup()

    create_message_field(margin_x, margin_y)
