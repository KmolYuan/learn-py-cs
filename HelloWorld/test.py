# -*- coding: utf-8 -*-
from os.path import abspath, join, dirname
from sys import path
pwd = dirname(abspath(__file__))
path.append(join(pwd, "bin", "Debug"))
import clr
clr.AddReference("HelloWorld")
from HelloWorld import Launcher


def main():
    l = Launcher()
    l.Main()


if __name__ == '__main__':
    main()
