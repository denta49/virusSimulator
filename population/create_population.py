from logic.tuple_to_list import tuple_to_list
from visuals.health.illness_duration import illness_duration
from visuals.health.make_healthy import make_healthy
from visuals.health.make_sick import make_sick
from visuals.movement.speed_horizontal import speed_horizontal
from visuals.movement.speed_vertical import speed_vertical
from visuals.positioning.generate_random_traffic import generate_random_traffic
from visuals.positioning.set_position import set_position


def create_population(number_of_healthy, number_of_injured, number_of_distanced, population_list, margin_x, margin_y):
    injured = [i for i in range(number_of_injured)]  # tworzenie osób zarażonych
    healthy = [i for i in range(number_of_healthy)]  # tworzenie osób niezarażonych
    distanced = [i for i in range(number_of_distanced)]  # tworzenie osób dystansujących się

    # zerowanie zmiennych
    x = 0
    y = 0

    health_timer = 0
    wait_for_move = 0
    wait_for_health = 0

    # tworzenie osoby zarażonej (przypisywanie jej cech)
    for i in injured:
        injured = [set_position(margin_x, margin_y), make_sick(), speed_horizontal(x), speed_vertical(y), generate_random_traffic(),
                          wait_for_move, illness_duration(health_timer), wait_for_health]

        population_list.append(injured)  # dodawanie stworzonej osoby do populacji

        tuple_to_list(population_list)  # zmienianie jej położenia z krotki na listę

    # tworzenie osoby niezarażonej(przypisywanie jej cech)
    for i in healthy:
        osoba_niezarazona = [set_position(margin_x, margin_y), make_healthy(), speed_horizontal(x), speed_vertical(y), generate_random_traffic(),
                             wait_for_move, illness_duration(health_timer), wait_for_health]

        population_list.append(osoba_niezarazona)  # jw.

        tuple_to_list(population_list)  # jw.

    # tworzenie osoby dystansującej się (przypisywanie jej cech)
    for i in distanced:
        osoba_dystansujaca = [set_position(margin_x, margin_y), make_healthy(), 0, 0, generate_random_traffic(), wait_for_move,
                              illness_duration(health_timer),
                              wait_for_health]  # ma się nie ruszać więc ma prędkość 0

        population_list.append(osoba_dystansujaca)  # jw.

        tuple_to_list(population_list)  # jw.

    # ustawianie liczników na stan początkowy
    for i in population_list:
        i[5] = i[4]
        i[7] = i[6]

    return population_list
