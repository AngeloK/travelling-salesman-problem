#!/usr/bin/env python
# -*- coding: utf-8 -*-

from driver import Driver
from path import Path
from itertools import permutations
import numpy as np
import math
import progressbar
import random


class Random_path_driver(Driver):

    def __init__(self, start, adjacent_matrix):
        super(Random_path_driver, self).__init__(start, adjacent_matrix)

    def solve_tsp(self, start, remained_set):
        print "------------------------------------"
        print "Solve using random city choosing algorithm..."

        remained_set = remained_set - {start}
        path = [start]
        next_vertext = 0
        total_min_cost = 0

        # bar = progressbar.ProgressBar(
            # maxval=self.total_problems, widgets=[
                # progressbar.Bar(
                    # '=', '[', ']'), ' ', progressbar.Percentage()]).start()

        while remained_set:
            next_vertext = random.sample(remained_set, 1)[0]
            total_min_cost += self.cost(path[-1], next_vertext)
            path.append(next_vertext)
            remained_set = remained_set - {next_vertext}

        total_min_cost += self.cost(path[-1], start)
        path.append(start)
        print total_min_cost
        print path

        print "End!"
        print "------------------------------------"
