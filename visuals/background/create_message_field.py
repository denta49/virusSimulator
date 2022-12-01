from turtle import penup, setpos, color, begin_fill, pendown, fd, rt, end_fill

background_color = 'bisque'


def create_message_field(margin_x, margin_y):
    setpos(-margin_x - 10, margin_y + 30)
    color(background_color)
    pendown()
    begin_fill()
    rt(90)
    fd(20 + margin_x * 2)
    rt(90)
    fd(20)
    rt(90)
    fd(20 + margin_x * 2)
    end_fill()
    penup()
