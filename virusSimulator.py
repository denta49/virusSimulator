from turtle import *

from population.create_population import create_population
from visuals.background.background import background
from visuals.health.recovering import recovering
from visuals.health.recovering_switch import recovering_switch
from visuals.movement.margin_bouncing import margin_bouncing
from visuals.movement.movement import movement
from visuals.movement.self_bouncing import self_bouncing
from visuals.positioning.movement_counter import movement_counter
from visuals.table.table_data import table_data

window_height = 500
window_width = 500
margin_x = 450
margin_y = 450


def main():
    population_list = []

    number_of_healthy = 20
    number_of_sick = 6
    number_of_distanced = 3

    dot_size = 20
    duration = 10000

    population = create_population(number_of_healthy, number_of_sick, number_of_distanced,
                                   population_list, margin_x, margin_y)

    for i in range(duration):
        clear()

        background(margin_x, margin_y)  # tworzenie tła

        movement_counter(population)  # ile tur pozostało do ruchu

        movement(population, dot_size)  # poruszanie się

        margin_bouncing(population, margin_x, margin_y)

        self_bouncing(population, dot_size)

        recovering(population)  # ile tur pozostało do wyzdrowienia

        recovering_switch(population)

        table_data(population, margin_x, margin_y)

        update()


ht()
penup()
tracer(0, 0)
speed(0)

main()

done()
