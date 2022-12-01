

def margin_bouncing(population_lst, margin_x, margin_y):
    for person in population_lst:

        if person[5] == 1:

            if person[0][0] >= margin_x or person[0][0] <= -margin_x:
                person[2] = -person[2]

            if person[0][1] >= margin_y or person[0][1] <= -margin_y:
                person[3] = -person[3]
