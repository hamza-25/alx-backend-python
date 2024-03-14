#!/usr/bin/env python3
"""annotate Module
"""
from typing import Callable, List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function return values with the appropriate types """
    return [(i, len(i)) for i in lst]
