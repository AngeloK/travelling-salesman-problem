#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy


class Path(object):

    '''Path object is used to store the cost of travelling and its path.
    '''

    def __init__(self, cost):
        self._path = []
        self.cost = cost

    def join_path(self, start, last_path):
        self._path = deepcopy(last_path)
        if last_path:
            self._path.insert(0, start)
        else:
            self._path = [start, 0]
        return self

    @property
    def path(self):
        return self._path

    def path_cost(self):
        return self.cost

    def __repr__(self):
        return "Path<%d> {%s}" % (self.cost, self._path)
