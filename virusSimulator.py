
from turtle import *
from random import *
from math import sqrt

################################################### DANE OKNA ##########################################################

window_height = 500
window_width = 500
margx = 450 #marginesy boczne
margy = 450 #marginesy górny i dolny

################################################ FUNKCJE TECHNICZE #####################################################


def hop(dlugosc_x, dlugosc_y):
    penup()
    fd(dlugosc_x)
    rt(90)
    fd(dlugosc_y)
    lt(90)
    pendown()


#RYSOWANIE TŁA I MIEJSCA NA WIADOMOSC
def tlo():

    #TŁO
    seth(90)
    penup()
    setpos(-margx-10, -margy-10)
    color("silver")
    begin_fill()
    pendown()

    for i in range(20):
        fd(20 + margy*2)
        rt(90)
        fd(20 + margx*2)
        rt(90)

    end_fill()
    penup()

    #MIEJSCE NA WIADOMOŚĆ
    setpos(-margx-10, margy+30)
    color("bisque")
    pendown()
    begin_fill()

    rt(90)
    fd(20 + margx*2)
    rt(90)
    fd(20)
    rt(90)
    fd(20 + margx*2)

    end_fill()
    penup()


#NARZĘDZIE DO ZMIANY KORTKI W LISTĘ
def wypakowanie_do_listy(lista, indeks):
    return list(lista[indeks][0])


#ZAMIENIANIE WSPÓŁRZĘDNYCH DANEJ OSOBY W LISTĘ
def zmiana_krotka_lista(lista):

    for i in range(len(lista)):

        wypakowanie_do_listy(lista, i)
        wspolzedne = wypakowanie_do_listy(lista, i)
        lista[i][0] = wspolzedne


################################################ FUNKCJE TWORZĄCE CECHY OSÓB ###########################################


#TWORZENIE LOSOWEGO POŁOŻENIA
def polozenie(x, y):

    penup()
    x = randrange(-margx, margx)
    y = randrange(-margy, margy)


    setpos(x, y)
    return x, y


#TWORZENIE STANU BYCIA CHORYM
def chora(color):

    color = "brown"
    return color


#TWORZENIE STANU BYCIA NIE-CHORYM
def niechora(color):

    color = "yellow"
    return color


#ZDROWIENIE OSOBY
def zdrowienie(lista_populacji):

    for osoby in lista_populacji:

        if osoby[1] == "brown" and osoby[7] == 1: #jeśli jesteś chora a twój licznik chorowania spadł do 1, to...
            osoby[1] = "green"  #...zdrowiej



################################################ FUNKCJE LICZĄCE #######################################################


#LICZNIK MÓWIĄCY CO ILE KOLEJEK MA RUSZYĆ SIĘ OSOBA O USTALONY WEKTOR PRĘDKOŚCI
def licznik_ruchu(co_ile_ruch):

    co_ile_ruch = randrange(1, 5) #każda osoba ma przypisaną losową liczbę tur, co które ma się ruszyć
    return co_ile_ruch


#LICZNIK MÓWIĄCY ILE TRWA CZAS TRWANIA CHOROBY
def licznik_choroby(za_ile_zdrowie):

    za_ile_zdrowie = 3000 #ile tur musi upłynąć aby osoba była zdrowa
    return za_ile_zdrowie


#SPADEK WARTOŚCI LICZNIKA RUCHU O 1 CO TURĘ
def odliczanie_ruch(lista):

    for osoby in lista:
        osoby[5] -= 1 #odejmowanie od indeksu, pod którym znajduje się licznik ruchu

        if osoby[5] == 0: #wracanie licznika do stanu początkowego po jego wyzerowaniu
            osoby[5] = osoby[4]

    return osoby


#SPADEK WARTOŚCI LICZNIKA CHOROBY O 1 CO TURĘ
def odliczanie_choroba(lista):

    for osoby in lista:
        osoby[7] -= 1 #odejmowanie od indeksu, pod którym znajduje się licznik trwania w chorobie

    return osoby


#FUNKCJA LICZĄCA I WYPISUJĄCA STAN POPULACJI
def wypisanie(lista_populacji):

    zarazeni = 0
    ozdrowiency = 0
    dystansujacy = 0
    color("black")
    setpos(-margx+200, margy+10)

    for osoby in lista_populacji:
        if osoby[1] == "brown": #sprawdź, czy osoba jest zarażona
            zarazeni += 1


        elif osoby[1] == "green": #sprawdź, czy jest ozdrowieńcem
            ozdrowiency += 1


        elif osoby[2] == 0 and osoby[3] == 0: #sprawdź, czy jest dystansującą się
            dystansujacy += 1

    #wypisz stan
    write(("Zarażeni = ", zarazeni,"Ozdrowieńcy = ", ozdrowiency,"Dystansujący = ", dystansujacy), False,
          "center", ("Arial", 10, "normal"))


################################################## FUNKCJE RUCHU #######################################################


#PORUSZANIE SIĘ OSÓB
def ruch(lista_populacji, wielkosc_kulki):

    for osoby in lista_populacji:

        if osoby[5] == 1: #gdy wartość pod indeksem z odliczaniem do ruchu wyniesie 1, to...

            osoby[0][0] += osoby[2] #dodaj wektor prękości poziomej do pozycji poziomej
            osoby[0][1] += osoby[3] #dodaj wektor prędkości pionowej do pozycji pionowej
            setpos(osoby[0][0], osoby[0][1]) #idź tam
            dot(wielkosc_kulki, osoby[1]) #zacznij istnieć

        else: #jeśli się nie ruszasz, nadal musisz istnieć
            setpos(osoby[0][0], osoby[0][1])
            dot(wielkosc_kulki, osoby[1])


#WEKTOR PRĘDKOŚCI POZIOMEJ
def predkosc_x(x):

    x = 1 #o ile pixeli w poziomie porusza się osoba
    predkosc_x = x

    return predkosc_x


#WEKTOR PRĘDKOŚCI PIONOWEJ
def predkosc_y(y):

    y = 1 #o ile pixeli porusza się osoba w pionie
    predkosc_y = y

    return predkosc_y


#ODBIJANIE OSÓB OD MARGINESÓW
def odbijanie_od_marginesow(lista_populacji, margx, margy):

    for osoby in lista_populacji:

        if osoby[5] == 1: #jeśli licznik ruchu spadnie do 1, to...


            if (osoby[0][0] >= margx or osoby[0][0] <= -margx): #...jeśli jesteś na maginesie poziomym...

                osoby[2] = -osoby[2] #zmień wektor prędkości poziomej na ujemny


            if (osoby[0][1] >= margy or osoby[0][1] <= -margy): #...jeśli jesteś na marginesie pionowym...

                osoby[3] = -osoby[3] #...zmień wektor prędkości pionowej na ujemny


#ODBIJANIE OSÓB OD SIEBIE
def odbijanie_od_siebie(lista, wielkosc_kulki):

    ind_kolejnej = -1
    ind_poprzedniej = -1

    for osoby in lista:

        if osoby[5] == 1:


            #porównywanie indeksów
            ind_kolejnej = -1
            ind_poprzedniej += 1

            for osoby in lista:


                ind_kolejnej += 1

                if ind_kolejnej == ind_poprzedniej: #jeśli porównujemy tę samą osobę z tą samą osobą
                    continue

                if ind_kolejnej == len(lista): #jeśli porównujemy osobę z osobą nie z jej świata
                    break

                #przypisz wartości indeksów do zmiennych
                x1 = lista[ind_poprzedniej][0][0]
                x2 = lista[ind_kolejnej][0][0]
                y1 = lista[ind_poprzedniej][0][1]
                y2 = lista[ind_kolejnej][0][1]

                #podstaw zmienne do wzoru na obliczanie odległości między punktami w układzie kartezjańskim
                odleglosc = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


                if odleglosc <= wielkosc_kulki: #jeśli odległość jest mniejsza niż wielkosc kulki, to...


                    #...jeśli pierwsza porównywana jest chora, a druga nie miała wcześniej styczności z wirusem, to...
                    if lista[ind_poprzedniej][1] == "brown" and lista[ind_kolejnej][1] == "yellow":

                        lista[ind_kolejnej][1] = "brown" #...zaraź tę drugą...
                        lista[ind_kolejnej][7] = lista[ind_kolejnej][6]#... i każ jej chorować tyle ile ma w liczniku...

                        #...oraz każ jej się odbić (zmień wektor prędkości)...

                        lista[ind_poprzedniej][2] = -lista[ind_poprzedniej][2]
                        lista[ind_poprzedniej][3] = -lista[ind_poprzedniej][3]


                    else: #...a jeśli nie spotkała się chora z nie-chorą to niech się po prostu odbiją.

                        lista[ind_poprzedniej][2] = -lista[ind_poprzedniej][2]
                        lista[ind_poprzedniej][3] = -lista[ind_poprzedniej][3]

    return ind_kolejnej, ind_poprzedniej


################################################## TWORZENIE POPULACJI #################################################


def tworzenie_populacji(ile_osob_niezarazonych,ile_osob_zarazonych, ile_osob_dystansujacych, lista_populacji):

    osoby_zarazone = [i for i in range(ile_osob_zarazonych)] #tworzenie osób zarażonych
    osoby_niezarazone = [i for i in range(ile_osob_niezarazonych)] #tworzenie osób niezarażonych
    osoby_dystansujace = [i for i in range(ile_osob_dystansujacych)] #tworzenie osób dystansujących się

    #zerowanie zmiennych
    x = 0
    y = 0
    co_ile_ruch = 0
    za_ile_zdrowie = 0
    oczekiwanie_na_ruch = 0
    oczekiwanie_na_zdrowie = 0

    #tworzenie osoby zarażonej (przypisywanie jej cech)
    for osoba_zarazona in osoby_zarazone:

        osoba_zarazona = [polozenie(x, y), chora(color), predkosc_x(x), predkosc_y(y), licznik_ruchu(co_ile_ruch),
                          oczekiwanie_na_ruch, licznik_choroby(za_ile_zdrowie), oczekiwanie_na_zdrowie]

        lista_populacji.append(osoba_zarazona) #dodawanie stworzonej osoby do populacji

        zmiana_krotka_lista(lista_populacji) #zmienianie jej położenia z krotki na listę

    #tworzenie osoby niezarażonej(przypisywanie jej cech)
    for osoba_niezarazona in osoby_niezarazone:

        osoba_niezarazona = [polozenie(x, y), niechora(color), predkosc_x(x), predkosc_y(y), licznik_ruchu(co_ile_ruch),
                             oczekiwanie_na_ruch, licznik_choroby(za_ile_zdrowie), oczekiwanie_na_zdrowie]

        lista_populacji.append(osoba_niezarazona) #jw.

        zmiana_krotka_lista(lista_populacji) #jw.

    #tworzenie osoby dystansującej się (przypisywanie jej cech)
    for osoba_dystansujaca in osoby_dystansujace:

        osoba_dystansujaca = [polozenie(x, y), niechora(color), 0, 0, licznik_ruchu(co_ile_ruch), oczekiwanie_na_ruch,
                              licznik_choroby(za_ile_zdrowie), oczekiwanie_na_zdrowie] #ma się nie ruszać więc ma prędkość 0

        lista_populacji.append(osoba_dystansujaca) #jw.

        zmiana_krotka_lista(lista_populacji) #jw.

    #ustawianie liczników na stan początkowy
    for osoby in lista_populacji:
        osoby[5] = osoby[4]
        osoby[7] = osoby[6]

    return lista_populacji


################################################## TWORZENIE SYMULACJI #################################################


def main():
    lista_populacji = [] #zerowanie listy populacji

    ile_osob_niezarazonych = 20
    ile_osob_zarazonych = 6
    ile_osob_dystansujacych = 3

    #czas trwania choroby można ustawić w funkcjach liczących, w funkcji o nazwie "licznik choroby"

    wielkosc_kulki = 20
    liczba_kolejek = 10000

    #wybieranie populacji
    populacja = tworzenie_populacji(ile_osob_niezarazonych,ile_osob_zarazonych, ile_osob_dystansujacych, lista_populacji)

    for i in range(liczba_kolejek):

        clear()

        tlo() #tworzenie tła

        odliczanie_ruch(populacja) #ile tur pozostało do ruchu

        ruch(populacja, wielkosc_kulki) #poruszanie się

        odbijanie_od_marginesow(populacja, margx, margy)

        odbijanie_od_siebie(populacja, wielkosc_kulki)

        odliczanie_choroba(populacja) #ile tur pozostało do wyzdrowienia

        zdrowienie(populacja)

        wypisanie(populacja)

        update()


ht()
penup()
tracer(0, 0)
speed(0)

main()

done()









