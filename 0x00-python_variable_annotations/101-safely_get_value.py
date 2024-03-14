#!/usr/bin/env python3
"""list module"""
from typing import Sequence, Union, Any, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ More involved type annotations """
    if key in dct:
        return dct[key]
    else:
        return default
