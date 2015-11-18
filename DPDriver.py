#!/usr/bin/env python
# -*- coding: utf-8 -*-

import driver
import copy


class DPDriver(driver.Driver):

    def __init__(self, start, adjacent_matrix):
        super(DPDriver, self).__init__(start, adjacent_matrix)

    def minimum_cost_path(self, start, remained_set):
        remained_length = len(remained_set)
        if remained_length == 1:
            self.path = [start, remained_set[0]]
            return self.cost(start, remained_set[0])
        else:
            for j in range(0, remained_length):
                select_city = remained_set[j]
                rest_set = copy.deepcopy(remained_set)
                rest_set.remove(select_city)
                self.min_cost = min(self.min_cost, self.minimum_cost_path(
                    select_city, rest_set) + self.cost(start, select_city)
                )
            return self.min_cost
