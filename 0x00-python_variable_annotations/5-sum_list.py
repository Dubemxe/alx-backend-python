#!/usr/bin/env python3
'''Defines a function that sums up a list
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Returns the sum of a list of floating-point numbers.
    '''
    return float(sum(input_list))
