# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 105torus_2019
## File description:
## secant.py
##

import sys
from math import pow

def secant(coefficients, n):
    a0 = coefficients[0]
    a1 = coefficients[1]
    a2 = coefficients[2]
    a3 = coefficients[3]
    a4 = coefficients[4]
    f = lambda x: (a4 * pow(x, 4)) + (a3 * pow(x, 3)) + (a2 * pow(x, 2)) + (a1 * x) + a0

    x0 = 0
    x1 = 1
    solutions = list()
    p = pow(10, -n)
    while abs(x1 - x0) >= p:
        try:
            x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))
            if (0 <= x2 <= 1) is False:
                sys.exit(84)
        except ZeroDivisionError:
            sys.exit(84)
        solutions.append(x2)
        x0 = x1
        x1 = x2
    for x in solutions:
        value = round(x, n)
        if value == x:
            v_format = "x = {0}"
        else:
            v_format = "x = {0:." + str(n) + "f}"
        print(v_format.format(value))
