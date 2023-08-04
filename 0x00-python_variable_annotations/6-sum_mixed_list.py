#!/usr/bin/env python3
from typing import Union

"""
A type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """Computes the sum of a list of mixed integers and floating-point
    numbers."""
    return float(sum(mxd_lst))
