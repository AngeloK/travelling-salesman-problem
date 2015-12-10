#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from pandas import read_csv
import matplotlib
import matplotlib.pyplot as plt


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


def draw_performance(csv_file, title):
    # Draw performance graph using csv file.
    data = read_csv(csv_file).set_index("size")
    data.plot()
    plt.title(title)
    plt.show()


def draw_multi_performance(csv_file):

    data = read_csv(csv_file)

    graph_of_cost = data[[" cost_of_gd", " cost_of_dp", " cost_of_random"]]
    gragh_of_time = data[[" time_gd", " time_of_dp", " time_of_random"]]

    fig, axes = plt.subplots(nrows=2, ncols=1)
    graph_of_cost.plot(ax=axes[0], title="Cost with size=50", figsize=(8,8))
    gragh_of_time.plot(ax=axes[1], title="Time with size=50", figsize=(8,6))
    plt.show()


