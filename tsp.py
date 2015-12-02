#!/usr/bin/env python
# -*- coding: utf-8 -*-

import helpers
from dp_driver import DPDriver
from brute_force_tsp import Brute_force_driver
from greedy_driver import GreedyDriver
import numpy as np
import profile

if __name__ == "__main__":
    # Initialize city map

    city_graph, cities_set = helpers.initialize_cities(15)
    print("City Grapy is:")
    print city_graph
    # city_graph = np.array([
        # [0, 38, 72, 40],
        # [38, 0, 68, 55],
        # [72, 68, 0, 78],
        # [40, 55, 78, 0]]
    # )
    # cities_set = [0,1,2,3]
    cities_set = frozenset(cities_set)
    dp_driver = DPDriver(0, city_graph)
    profile.run("dp_driver.solve_tsp(0, cities_set)")

    # bf_driver = Brute_force_driver(0, city_graph)
    # profile.run("bf_driver.solve_tsp(0)")

    gd_driver = GreedyDriver(0, city_graph)
    profile.run("gd_driver.solve_tsp(0, cities_set)")
