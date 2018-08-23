#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : parse-eos.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 08/23/2018
#
# This file is part of SceneGraphParser.
# Distributed under terms of the MIT license.
# https://github.com/vacancy/SceneGraphParser

import re


def main():
    import sys

    text = '\n'.join(sys.stdin.readlines())
    groups = re.findall("<b eza[\s\S]*?>(.*?)<\/b>", text, re.MULTILINE)

    if len(groups) == 0:
        print('Error to get the page.')

    current = groups[len(groups) // 3 * 2][0].lower()
    print('Current', current, file=sys.stderr)

    for g in groups:
        g = g.lower()
        if not g.startswith(current):
            print('Filter: ', g, file=sys.stderr)
        else:
            print(g)


if __name__ == '__main__':
    main()

