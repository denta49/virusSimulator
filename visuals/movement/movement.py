from turtle import setpos, dot


def movement(lista_populacji, wielkosc_kulki):
    for person in lista_populacji:

        if person[5] == 1:  # gdy wartość pod indeksem z odliczaniem do ruchu wyniesie 1, to...

            person[0][0] += person[2]  # dodaj wektor prękości poziomej do pozycji poziomej
            person[0][1] += person[3]  # dodaj wektor prędkości pionowej do pozycji pionowej
            setpos(person[0][0], person[0][1])  # idź tam
            dot(wielkosc_kulki, person[1])  # zacznij istnieć

        else:  # jeśli się nie ruszasz, nadal musisz istnieć
            setpos(person[0][0], person[0][1])
            dot(wielkosc_kulki, person[1])
