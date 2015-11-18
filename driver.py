#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Driver(object):

    def __init__(self, start, adjacent_matrix):

        self._start = start
        self._adjacent_matrix = adjacent_matrix
        self.path = []

        self.min_cost = 9999999

    def cost(self, start, end):
        return self._adjacent_matrix[start][end]
