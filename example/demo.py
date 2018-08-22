#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : demo.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 08/22/2018
#
# This file is part of SceneGraphParser.
# Distributed under terms of the MIT license.
# https://github.com/vacancy/SceneGraphParser

"""
A small demo for the scene graph parser.
"""

import sng_parser


def demo(sentence):
    print('Sentence:', sentence)

    # Here we just use the default parser.
    sng_parser.tprint(sng_parser.parse(sentence), show_entities=False)

    print()


def main():
    demo('A woman is playing the piano in the room.')
    demo('A woman playing the piano in the room.')
    demo('A piano is played by a woman in the room.')
    demo('A woman is playing the space craft at NASA.')

if __name__ == '__main__':
    main()

