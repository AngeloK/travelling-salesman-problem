#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


class Driver(object):

    def __init__(self, start, adjacent_matrix):

        self._start = start
        self._adjacent_matrix = adjacent_matrix
        self._cities_set = frozenset(
            [i for i in range(0, len(adjacent_matrix[0]))])
        self._cities_set_without_start = frozenset(
            [i for i in range(1, len(adjacent_matrix[0]))])

    @property
    def start(self):
        return self._start

    @property
    def cities_set_without_start(self):
        return self._cities_set_without_start

    @property
    def cities_length(self):
        return len(self._cities_set)

    def cost(self, start, end):
        return self._adjacent_matrix[start][end]
