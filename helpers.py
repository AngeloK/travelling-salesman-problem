#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def initialize_cities(map_size):
    # Initialize a city map randomly and store data into an adjacent matrix.
    # Adjancent matrix is a symmetric matrix if the graph is an undirected
    # graph.
    cities_set = []
    init_maxtrix = np.random.random_integers(
        1, 100, size=(
            map_size, map_size))
    symm_matrix = (init_maxtrix+init_maxtrix.T)/2
    for i in range(0, map_size):
        cities_set.append(i)
        symm_matrix[i][i] = 0
    return symm_matrix, cities_set


def draw_map(adjacent_matrix):
    pass


def draw_shortest_path(adjacent_matrix, driver):
    pass
