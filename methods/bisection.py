# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 105torus_2019
## File description:
## bisection.py
##

import sys
from math import pow

def bisection(coefficients, n):
    a0 = coefficients[0]
    a1 = coefficients[1]
    a2 = coefficients[2]
    a3 = coefficients[3]
    a4 = coefficients[4]
    f = lambda x: (a4 * pow(x, 4)) + (a3 * pow(x, 3)) + (a2 * pow(x, 2)) + (a1 * x) + a0

    a = 0
    b = 1
    if ((f(a) < 0 and f(b) > 0) or (f(a) > 0 and f(b) < 0)) is False:
        sys.exit(84)
    p = pow(10, -n)
    solutions = list()
    while (b - a) >= p:
        m = (a + b) / 2
        if 0 <= m <= 1:
            solutions.append(m)
        else:
            sys.exit(84)
        if f(m) < 0:
            a = m
        else:
            b = m
    for x in solutions:
        print("x = {0}".format(round(x, n)))