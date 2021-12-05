#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun(opr):
    def culc(a, b):
        if opr == 0:
            return f'Площадь триуголника: {0.5 * a * b}'
        elif opr == 1:
            return f'Площадь прямоуголника: {a * b}'
        else:
            return "Ошибка"
    return culc
