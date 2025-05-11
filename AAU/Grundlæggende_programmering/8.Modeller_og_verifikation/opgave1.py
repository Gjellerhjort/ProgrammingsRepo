# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 9:31:12 2024

@author: Mads Gørup Gjellerod Christiansen
"""

import math

def f(x):
    """
    

    Parameters
    ----------
    x : int.

    Returns
    -------
    int.

    """
    return x**2-1


def g(x,y):
    """
    

    Parameters
    ----------
    x : int
    y : int
        DESCRIPTION.

    Returns
    -------
    int.

    """
    return math.sqrt(x**2+y**2)

def h(x):
    """
    

    Parameters
    ----------
    x : int
        DESCRIPTION.

    Returns
    -------
    int.

    """
    if x <= 0:
        return 0
    else:
        return 1

   
if __name__ == '__main__':
    import doctest
    doctest.testmod()