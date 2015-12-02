#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import helpers
from dp_driver import DPDriver
from brute_force_tsp import Brute_force_driver
from greedy_driver import GreedyDriver
import numpy as np
import profile
import time
import csv


def iterate_test(count):

    try:
        # with open("performance.csv", "rw") as f:
        with open('performance.csv', 'w') as csvfile:
            fieldnames = ['size', 'time_dp', 'time_gd', 'time_bf']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            time_dp = 0
            time_gd = 0
            for i in range(3, count+10):
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

                if i < 8:
                    time_start = time.time()
                    bf_driver = Brute_force_driver(0, city_graph)
                    bf_driver.solve_tsp(0)
                    time_end = time.time()
                    time_bf = time_end - time_start
                else:
                    time_bf = "Over %s" % str(time_bf)
                writer.writerow({'size': i, 'time_dp': time_dp, 'time_gd': time_gd, 'time_bf': time_bf})
    except Exception as e:
        print e


def compute_time(func):

    time_start = time.time()
    func()
    time_end = time.time()
    return time_end - time_start


if __name__ == "__main__":
    iterate_test(10)
