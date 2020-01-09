# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 105torus_2019
## File description:
## newton.py
##

import sys
from math import pow
from error_handling.error_handler import error_handler

def newton(coefficients, n) :
    a0 = coefficients[0]
    a1 = coefficients[1]
    a2 = coefficients[2]
    a3 = coefficients[3]
    a4 = coefficients[4]
    f = lambda x: (a4 * pow(x, 4)) + (a3 * pow(x, 3)) + (a2 * pow(x, 2)) + (a1 * x) + a0
    derivated = lambda x: (4 * a4 * pow(x, 3)) + (3 * a3 * pow(x, 2)) + (2 * a2 * x) + a1

    xn = 0.5
    print("x = {}".format(xn))
    save = derivated(xn)
    if save == 0 :
        return
    xnext = xn - (f(xn) / save)
    while round(xn, n) != round(xnext, n):
        save = derivated(xn)
        if save == 0 :
            break
        xn -= f(xn) / save
        save = derivated(xn)
        if save == 0 :
            break
        xnext -= f(xn) / save
        try:
            if (xn * pow(10, n)) % 10 > 0 :
                value = "x = {0:." + str(n) + "f}"
            else:
                value = "x = {0}"
        except OverflowError:
            error_handler()
        print(value.format(round(xn, n)))