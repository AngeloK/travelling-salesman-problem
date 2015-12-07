#!/usr/bin/env python
# -*- coding: utf-8 -*-

import helpers
from dp_driver import DPDriver
from brute_force_tsp import Brute_force_driver
from greedy_driver import GreedyDriver
from random_path import Random_path_driver
import numpy as np
import profile

if __name__ == "__main__":
    # Initialize city map

    try:
        city_size = int(raw_input("Please input the city size: (Default=10) "))
    except:
        city_size = 10
    finally:
        if city_size > 60:
            print "City size is out of range, please choose a smaller number and try again."
            exit(1)
    print "City Size = %d\n" % city_size
    try:
        is_directed = int(
            raw_input("Directed or undirected? 1.Directed 0.Undirected(Default=0)")) or 0
        if is_directed not in [0, 1]:
            is_directed = 0
    except:
        is_directed = 0
    if is_directed:
        print "You chose directed graph.\n"
    else:
        print "You chose undirected graph.\n"
    city_graph, cities_set = helpers.initialize_cities(city_size, is_directed=is_directed)
    cities_set = frozenset(cities_set)
    print("City Grapy is:\n")
    print city_graph

    try:
        method = int(raw_input(
            "Which algorithms to use (Default=4)?\n 1). Dynamic Programming\n 2).Greedy Algorithm.\n 3). Brute Force\n 4) All of Them\n ")) or 4
        if method not in [1,2,3,4]:
            method = 4
    except:
        method = 4

    if method == 1:
        dp_driver = DPDriver(0, city_graph)
        profile.run("dp_driver.solve_tsp(0, cities_set)")

    if method == 2:
        gd_driver = GreedyDriver(0, city_graph)
        # gd_driver.solve_tsp(0, cities_set)
        profile.run("gd_driver.solve_tsp(0, cities_set)")
    if method == 3:
        bf_driver = Brute_force_driver(0, city_graph)
        profile.run("bf_driver.solve_tsp(0)")

    if method == 4:
        dp_driver = DPDriver(0, city_graph)
        dp_driver.solve_tsp(0, cities_set)

        gd_driver = GreedyDriver(0, city_graph)
        gd_driver.solve_tsp(0, cities_set)

        bf_driver = Brute_force_driver(0, city_graph)
        bf_driver.solve_tsp(0)
