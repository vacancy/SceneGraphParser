#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : process-scene-nouns.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 08/23/2018
#
# This file is part of SceneGraphParser.
# Distributed under terms of the MIT license.
# https://github.com/vacancy/SceneGraphParser

import sys
import spacy

nlp = spacy.load('en')


def main():
    nouns = set()
    for line in sys.stdin:
        line, _ = line.split(' ')
        line = line.split('/')[2:]
        for x in line:
            parts = x.split('_')
            if len(parts) > 1:
                for p in parts:
                    if p not in nouns:
                        print('add', p, file=sys.stderr)
                    nouns.add(p)
            nouns.add(' '.join(parts))

    for n in sorted(nouns):
        if ' ' not in n:
            if nlp(n)[0].pos_ != 'NOUN':
                print('remove', n, file=sys.stderr)
            else:
                print(n)
        else:
            print(n)

if __name__ == '__main__':
    main()

