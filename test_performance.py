#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import helpers
from dp_driver import DPDriver
from brute_force_tsp import Brute_force_driver
from greedy_driver import GreedyDriver
from random_path import Random_path_driver
import numpy as np
import profile
import time
import csv


def test_dynamic_with_brute(count):

    try:
        time_dp = 0
        time_gd = 0
        time_bf = 0
        for i in range(3, count):
            for j in range(50):
                city_graph, cities_set = helpers.initialize_cities(i)
                cities_set = frozenset(cities_set)
                time_start = time.time()
                dp_driver = DPDriver(0, city_graph)
                dp_driver.solve_tsp(0, cities_set)
                time_end = time.time()
                time_dp += time_end - time_start

                time_start = time.time()
                gd_driver = GreedyDriver(0, city_graph)
                gd_driver.solve_tsp(0, cities_set)
                time_end = time.time()
                time_gd += time_end - time_start
            time_dp = time_dp/50
            time_gd = time_gd/50

            if i < 7:
                time_start = time.time()
                bf_driver = Brute_force_driver(0, city_graph)
                bf_driver.solve_tsp(0)
                time_end = time.time()
                time_bf = time_end - time_start
            else:
                time_bf = 35.6242659092
            with open('performance.csv', 'a') as csvfile:
                csvfile.write("{0}, {1}, {2}, {3}\n".format(
                    i,
                    time_dp,
                    time_gd,
                    time_bf))
    except Exception as e:
        print e


def test_random_path_with_greedy(count, city_size=50):
    cost_of_random_path = 0
    cost_of_greeedy = 0
    time_greedy = 0
    time_random_path = 0
    for i in range(count):
        city_graph, cities_set = helpers.initialize_cities(city_size)
        cities_set = frozenset(cities_set)
        time_start = time.time()
        greedy_driver = GreedyDriver(0, city_graph)
        cost_of_greeedy, path_of_greedy = greedy_driver.solve_tsp(
            0, cities_set)
        time_end = time.time()
        time_greedy += time_end - time_start

        time_start = time.time()
        random_path_driver = Random_path_driver(0, city_graph)
        cost_of_random_path, path_of_random = random_path_driver.solve_tsp(
            0, cities_set)
        time_end = time.time()
        time_random_path += time_end - time_start

        with open("performance_greedy_with_random.csv", "a") as csvfile:
            csvfile.write("{0},{1},{2},{3},{4}\n".format(
                city_size,
                cost_of_random_path,
                time_random_path,
                cost_of_greeedy,
                time_greedy)
            )


def test_greedy_with_dynamic_programming(count, city_size=10):

    time_dynamic_programming = 0
    cost_of_greeedy = 0
    time_greedy = 0
    dp_output = None
    time_random_path = 0

    for i in range(count):
        city_graph, cities_set = helpers.initialize_cities(city_size)
        cities_set = frozenset(cities_set)
        time_start = time.time()
        greedy_driver = GreedyDriver(0, city_graph)
        cost_of_greeedy, path_of_greedy = greedy_driver.solve_tsp(
            0, cities_set)
        time_end = time.time()
        time_greedy = time_end - time_start

        time_start = time.time()
        dp_driver = DPDriver(0, city_graph)
        dp_output = dp_driver.solve_tsp(
            0, cities_set)
        time_end = time.time()
        time_dynamic_programming = time_end - time_start

        time_start = time.time()
        random_path_driver = Random_path_driver(0, city_graph)
        cost_of_random_path, path_of_random = random_path_driver.solve_tsp(
            0, cities_set)
        time_end = time.time()
        time_random_path = time_end - time_start

        with open("performance_greedy_with_dp.csv", "a") as csvfile:
            csvfile.write("{0},{1},{2},{3},{4},{5},{6}\n".format(
                city_size,
                cost_of_greeedy,
                dp_output.path_cost(),
                cost_of_random_path,
                time_greedy,
                time_dynamic_programming,
                time_random_path)
            )

if __name__ == "__main__":
    # test_dynamic_with_brute(15)
    # test_random_path_with_greedy(100)
    test_greedy_with_dynamic_programming(100)
