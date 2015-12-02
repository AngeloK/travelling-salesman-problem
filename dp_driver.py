#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import driver
from path import Path
from itertools import combinations
import numpy as np
import progressbar
import time

################################################################################
# Solve Travelling Salesman Problem using Dynamic Programming
################################################################################


class DPDriver(driver.Driver):

    def __init__(self, start, adjacent_matrix):
        super(DPDriver, self).__init__(start, adjacent_matrix)
        self._subproblems = {}

    def calculate_total_problems(self):
        n = len(self.cities_set_without_start)
        total_problems = n*np.power(2, n-1)+1
        print "Total subproblems is %d" % total_problems
        return total_problems

    def solve_tsp(self, start, remained_set):
        print "Solve using dynamic programming..."
        print "------------------------------------"
        set_length = len(remained_set)
        remained_set = remained_set - {0}
        subproblem_count = 0

        bar = progressbar.ProgressBar(
            maxval=self.calculate_total_problems(), widgets=[
                progressbar.Bar(
                    '=', '[', ']'), ' ', progressbar.Percentage()]).start()

        # Solve subproblems from bottom to top
        for l in range(1, set_length+1):
            for subset in combinations(remained_set, l):
                for element in subset:
                    key = (element, frozenset(subset)-{element})
                    if key not in self._subproblems:
                        self._subproblems[
                            key] = self.find_optimal_subproblem(key)

                        # Update progress bar
                        subproblem_count += 1
                        bar.update(subproblem_count)
        bar.finish()
        # Solve final problem using subproblems solved before.
        main_problem_key = (0, remained_set)
        self._subproblems[main_problem_key] = self.find_optimal_subproblem(
            main_problem_key)
        print self._subproblems[main_problem_key]
        print "End!"
        print "------------------------------------"

    def find_optimal_subproblem(self, key):
        '''Key is an tuple (start, {REM}), using the set REM to generate subsets.
        Each problem is the subproblem with minimum cost W add the distance
        between start to the start of subproblem.
        if key = (2, {3}), then cost_of_key equals to the cost from 2 to 0 only
        using vertics in set {3} plus distanc(2,3). And the path is 2->3->0.
        '''
        if len(key[1]) == 0:
            cost = self.cost(key[0], 0)
            # Generate path.
            return Path(cost).join_path(key[0], [])
        min_weight = np.inf
        min_key = 0
        for element in key[1]:
            sub_key = (element, key[1] - {element})
            if self._subproblems[sub_key].path_cost() + self.cost(key[0], element) < min_weight:
                min_weight = self._subproblems[
                    sub_key].path_cost() + self.cost(element, key[0])
                min_key = sub_key

        return Path(min_weight).join_path(
            key[0],
            self._subproblems[min_key].path)
