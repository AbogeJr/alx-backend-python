#!/usr/bin/env python3

from typing import List

"""
A type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: List[float]) -> float:
    """Computes the sum of a list of floating-point numbers."""
    return float(sum(input_list))
