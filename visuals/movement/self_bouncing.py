from math import sqrt


def self_bouncing(list_of_dots, dot_size) :

    next_idx = -1
    previous_idx = -1

    for osoby in list_of_dots:

        if osoby[5] == 1:

            # porównywanie indeksów
            next_idx = -1
            previous_idx += 1

            for i in list_of_dots:

                next_idx += 1

                if next_idx == previous_idx:  # jeśli porównujemy tę samą osobę z tą samą osobą
                    continue

                if next_idx == len(list_of_dots):  # jeśli porównujemy osobę z osobą nie z jej świata
                    break

                # przypisz wartości indeksów do zmiennych
                x1 = list_of_dots[previous_idx][0][0]
                x2 = list_of_dots[next_idx][0][0]
                y1 = list_of_dots[previous_idx][0][1]
                y2 = list_of_dots[next_idx][0][1]

                # podstaw zmienne do wzoru na obliczanie odległości między punktami w układzie kartezjańskim
                odleglosc = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

                if odleglosc <= dot_size:  # jeśli odległość jest mniejsza niż wielkosc kulki, to...

                    # ...jeśli pierwsza porównywana jest chora, a druga nie miała wcześniej styczności z wirusem, to...
                    if list_of_dots[previous_idx][1] == "brown" and list_of_dots[next_idx][1] == "yellow":

                        list_of_dots[next_idx][1] = "brown"  # ...zaraź tę drugą...
                        list_of_dots[next_idx][7] = list_of_dots[next_idx][
                            6]  # ... i każ jej chorować tyle ile ma w liczniku...

                        # ...oraz każ jej się odbić (zmień wektor prędkości)...

                        list_of_dots[previous_idx][2] = -list_of_dots[previous_idx][2]
                        list_of_dots[previous_idx][3] = -list_of_dots[previous_idx][3]


                    else:  # ...a jeśli nie spotkała się chora z nie-chorą to niech się po prostu odbiją.

                        list_of_dots[previous_idx][2] = -list_of_dots[previous_idx][2]
                        list_of_dots[previous_idx][3] = -list_of_dots[previous_idx][3]
    return next_idx, previous_idx
