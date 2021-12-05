#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Решить индивидуальное задание лабораторной работы 2.6,
оформив каждую команду в виде
отдельной функции.
'''

from mod import add, select, show, help


def main():
    stations = []

    while True:
        command = input(">>> ").lower()
        if command == "exit":
            break
        elif command == "add":
            add(stations)
        elif command == "select":
            select(stations)
        elif command == "show":
            show(stations)
        elif command == "help":
            help()


if __name__ == '__main__':
    main()
