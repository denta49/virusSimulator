from turtle import color, setpos, write




def table_data(population_lst, margin_x, margin_y):
    sick_people = 0
    healthy_people = 0
    distanced_people = 0
    color("black")
    setpos(-margin_x + 200, margin_y + 10)

    for person in population_lst:
        if person[1] == "brown":
            sick_people += 1

        elif person[1] == "green":
            healthy_people += 1

        elif person[2] == 0 and person[3] == 0:
            distanced_people += 1

    write(("Zarażeni = ", sick_people, "Ozdrowieńcy = ", healthy_people, "Dystansujący = ", distanced_people), False,
          "center", ("Arial", 10, "normal"))
