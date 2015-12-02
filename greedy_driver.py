#!/usr/bin/env python
# -*- coding: utf-8 -*-

from driver import Driver
from path import Path
import numpy as np


class GreedyDriver(Driver):

    def __init__(self, start, adjacent_matrix):
        super(GreedyDriver, self).__init__(start, adjacent_matrix)


    def solve_tsp(self, start, remained_set):
        print "Solve using greedy algorithm..."
        print "------------------------------------"
        remained_set = remained_set - {start}
        path = [start]
        next_vertext = 0
        total_min_cost = 0

        while remained_set:
            min_cost = np.inf
            for vertex in remained_set:
                if self.cost(vertex, path[-1])< min_cost:
                    min_cost = self.cost(vertex, path[-1])
                    next_vertext = vertex
            total_min_cost += min_cost
            path.append(next_vertext)
            remained_set = remained_set - {next_vertext}

        total_min_cost+=self.cost(start, path[-1])
        path.append(start)
        print total_min_cost
        print path
        print "End!"
        print "------------------------------------"

