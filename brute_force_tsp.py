#!/usr/bin/env python
# -*- coding: utf-8 -*-


from driver import Driver
from path import Path
from itertools import permutations
import numpy as np
import math
import progressbar


class Brute_force_driver(Driver):

    def __init__(self, start, adjacent_matrix):
        super(Brute_force_driver, self).__init__(start, adjacent_matrix)
        self._all_path = []
        self.total_problems = math.factorial(self.cities_length-1)

    def find_all_paths(self):
        return permutations(
            self.cities_set_without_start, len(
                self.cities_set_without_start))

    def add_start_and_end(self, path):
        return (self.start,) + path + (self.start,)

    def calculate_cost(self, path):
        path = self.add_start_and_end(path)
        cost = 0
        for i in range(1, self.cities_length+1):
            cost += self.cost(path[i], path[i-1])
        return cost, path

    def solve_tsp(self, start):
        '''
        Emulerate all possibilities from start vertex to this vertex using
        remained vertices
        '''
        print "------------------------------------"
        print "Solve using brute force algorithm..."
        min_cost = np.inf
        min_path = []
        subproblem_count = 0
        bar = progressbar.ProgressBar(
            maxval=self.total_problems, widgets=[
                progressbar.Bar(
                    '=', '[', ']'), ' ', progressbar.Percentage()]).start()
        for path in self.find_all_paths():
            subproblem_count+=1
            bar.update(subproblem_count)
            if self.calculate_cost(path)[0] < min_cost:
                min_cost, min_path = self.calculate_cost(path)
        bar.finish()
        print min_cost
        print min_path
        print "End!"
        print "------------------------------------"
        return min_cost, min_path
