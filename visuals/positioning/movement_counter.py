def movement_counter(lst):
    for person in lst:
        person[5] -= 1
        if person[5] == 0:
            person[5] = person[4]

    return person
