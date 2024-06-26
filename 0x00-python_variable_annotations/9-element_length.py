#!/usr/bin/env python3
'''
Defines a function that gets the length of a list
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Computes the length of a list of sequence'''
    return [(i, len(i)) for i in lst]
