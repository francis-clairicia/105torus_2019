# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 105torus_2019
## File description:
## newton.py
##

import sys
from math import pow

def newton(coefficients, n):
    a0 = coefficients[0]
    a1 = coefficients[1]
    a2 = coefficients[2]
    a3 = coefficients[3]
    a4 = coefficients[4]
    f = lambda x: (a4 * pow(x, 4)) + (a3 * pow(x, 3)) + (a2 * pow(x, 2)) + (a1 * x) + a0
    derivated = lambda x: (4 * a4 * pow(x, 3)) + (3 * a3 * pow(x, 2)) + (2 * a2 * x) + a1

    xn = 0.5
    solutions = [xn]
    try:
        xnext = xn - (f(xn) / derivated(xn))
    except ZeroDivisionError:
        sys.exit(84)
    p = pow(10, -n)
    while abs(xnext - xn) >= p:
        try:
            xn -= f(xn) / derivated(xn)
            xnext -= f(xn) / derivated(xn)
            if (0 <= xn <= 1) is False:
                sys.exit(84)
        except ZeroDivisionError:
            sys.exit(84)
        else:
            solutions.append(xn)
    for x in solutions:
        value = round(x, n)
        if value == x:
            v_format = "x = {0}"
        else:
            v_format = "x = {0:." + str(n) + "f}"
        print(v_format.format(value))
