# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 105torus_2019
## File description:
## secant.py
##

import sys
from math import pow

def secant(coefficients, n) :
    a0 = coefficients[0]
    a1 = coefficients[1]
    a2 = coefficients[2]
    a3 = coefficients[3]
    a4 = coefficients[4]
    f = lambda x: (a4 * pow(x, 4)) + (a3 * pow(x, 3)) + (a2 * pow(x, 2)) + (a1 * x) + a0

    x0 = 0
    x1 = 1
    x = 0
    x2 = -1
    while round(x2, n) != round(x, n):
        x = x2
        x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))
        try:
            if (x2 * pow(10, n)) % 10 > 0:
                value = "x = {0:." + str(n) + "f}"
            else:
                value = "x = {0}"
        except OverflowError:
            sys.exit(84)
        print(value.format(round(x2, n)))
        x0 = x1
        x1 = x2
