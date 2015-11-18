#!/usr/bin/env python
# -*- coding: utf-8 -*-

import helpers
import DPDriver
import numpy as np

if __name__ == "__main__":
    # Initialize city map

    # city_graph, cities_set = helpers.initialize_cities(4)
    # print("City Grapy is:")
    # print city_graph

    city_graph = np.array([
        [0, 84, 27, 40],
        [84, 0, 50, 43],
        [27, 50,  0, 49],
        [40, 43, 49, 0]
    ])

    cities_set = [0, 1, 2, 3]

    dp_driver = DPDriver.DPDriver(0, city_graph)
    cities_set.remove(0)
    print dp_driver.minimum_cost_path(0, cities_set)
