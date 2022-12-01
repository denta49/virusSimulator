def recovering_switch(lst_of_population):

    for person in lst_of_population:

        if person[1] == "brown" and person[7] == 1:
            person[1] = "green"
