# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 105torus_2019
## File description:
## bisection.py
##

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
    p = pow(10, -n)
    while (b - a) > p:
        m = (a + b) / 2
        if f(m) < 0:
            a = m
        else:
            b = m
        if (m * pow(10, n)) % 10 > 0:
            print("x = {0:.6f}".format(round(m, n)))
        else:
            print("x = {0}".format(round(m, n)))