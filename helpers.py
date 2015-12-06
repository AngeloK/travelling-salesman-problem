#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def initialize_cities(map_size, is_directed=False):
    # Initialize a city map randomly and store data into an adjacent matrix.
    # Adjancent matrix is a symmetric matrix if the graph is an undirected
    # graph. if is_directed is equal to 'True', then this function will create
    # a directed graph.
    cities_set = []
    init_maxtrix = np.random.random_integers(
        1, 100, size=(
            map_size, map_size))
    if not is_directed:
        init_maxtrix = (init_maxtrix+init_maxtrix.T)/2
    for i in range(0, map_size):
        cities_set.append(i)
        init_maxtrix[i][i] = 0
    return init_maxtrix, cities_set


def draw_map(adjacent_matrix):
    pass


def draw_shortest_path(adjacent_matrix, driver):
    pass
